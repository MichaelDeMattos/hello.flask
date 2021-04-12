# -*- coding: utf-8 -*-

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