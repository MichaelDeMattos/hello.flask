# -*- coding: utf-8 -*-

import smtplib
import threading
import email.message
from datetime import datetime

from home.model import *

class ControllerAcounts(object):
    def __init__(self, *args):
        ...
    
    """ Check acount existent """
    def get_acount_existent(self, email):
        try:
            Acounts = Table("acounts")
            query = (Acounts.select(Acounts.c.email).where(Acounts.c.email == email))
            users = []
            [users.append(row) for row in query.execute(db)]
            if users != []:
                return {"status": 409, "error": "Acounts existent"}
            
            if users == []:
                return {"status": 200}
            
        except Exception as error:
            print(error)
            return {"status": 404, "error": error}

    """ Register new acount """
    def insert_new_acount(self, name, email):
        try:
            query = Acounts(name=name, email=email)
            query.save()
            return {"status": 200}
            
        except Exception as error:
            db.rollback()
            return {"status": 404, "error": str(error)}


class ControllerSendEmail(object):
    def __init__(self, *args):
        self.server = "br666.hostgator.com.br"
        self.port = 465
        self.origin = "tester@dotpyc.com"
        self.password = "MyPass"
        self.now = datetime.now()
    
    """ Function send email for client """
    def send_email(self, email_destiny):
        try:
            
            html = (f""" 
            <html>
                <head>
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.2/css/bulma.min.css">
                </head>
                <div class="title">
                <h3 style="margin: 10px; text-align: center;">
                    Olá {email}, agora você faz parte do mundo DotPyc</h3>
                </div>
                <p style="margin: 10px;">{self.now.strftime('%d/%m/%y, %H:%M:%S')}</p>
            </html> """)

            msg = email.message.Message()
            msg['Subject'] = "Bem-Vindo a DotPyc"
            msg['From'] = self.origin
            msg['To'] = email_destiny
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(html, charset='utf-8')
            
            """ This instace for SMTP Server """
            server_smtp = smtplib.SMTP_SSL(self.server, self.port)
            
            """ Login Credentials for sending the mail """
            server_smtp.login(msg['From'], self.password)
    
            """ Send email """
            server_smtp.sendmail(msg['From'], [msg['To']], msg.as_string())
                                                            
            """ Destroy connection """
            servidor_smtp.quit()

        except Exception as error:
            return {"status": 404, "error": str(error)}
    
    """ The function create thread """
    def create_thread(self, email):
        thread = threading.Thread(target=self.send_email, args=(email,))
        thread.start()
