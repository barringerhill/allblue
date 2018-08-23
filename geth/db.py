from peewee import *;

db = SqliteDatabase('the.fox');

class BaseModel(Model):
    class Meta:
        database = db;

class Block(BaseModel):
    difficulty = IntegerField();
    gas_limit = IntegerField();
    gas_used = IntegerField();
    hash = CharField(unique = True);
    number = IntegerField(unique = True);
    size = IntegerField();
    timestamp = IntegerField();
    total_difficulty = IntegerField();
    transactions = CharField();
    finished = IntegerField();

class Tx(BaseModel):
    block_hash = IntegerField(unique = True);
    hash = CharField(unique = True);
    content = CharField();
    finished = IntegerField();

class FoxDB():

    def init(self):
        db.connect();
        db.create_tables([Block, Tx]);
        db.close();

    def start(self):
        db.connect();

    def close():
        db.close;
