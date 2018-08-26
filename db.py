from peewee import *;

db = SqliteDatabase('the.fox');

class BaseModel(Model):
    class Meta:
        database = db;

class Tx(BaseModel):
    block_number = IntegerField();
    hash = CharField();
    input = CharField();
    finished = IntegerField();

class FoxDB():

    def init(self):
        db.connect();
        db.create_tables([Tx]);
        db.close();

    def start(self):
        db.connect();

    def close():
        db.close;
