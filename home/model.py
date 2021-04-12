# -*- coding: utf-8 -*-

from peewee import *
from datetime import datetime

db = SqliteDatabase("acounts.db")

class Acounts(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=256, null=False)
    email = CharField(max_length=256, null=False, unique=True)
    create_date = DateField(default=datetime.now())

    class Meta:
        database = db

db.connect()
db.create_tables([Acounts])
