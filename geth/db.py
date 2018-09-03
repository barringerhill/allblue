from peewee import *;

db = SqliteDatabase('the.fox');

class BaseModel(Model):
    class Meta:
        database = db;

class Block(BaseModel):
    number = IntegerField();
    difficulty = IntegerField();
    gas_limit = IntegerField();
    gas_used = IntegerField();
    hash = CharField();
    size = IntegerField();
    timestamp = IntegerField();
    total_difficulty = IntegerField();
    txs_n = IntegerField();

class Tx(BaseModel):
    hash = CharField();
    input = CharField();
    
class FoxDB():

    def init(self):
        db.connect();
        db.create_tables([Block, Tx]);
        db.close();

    def start(self):
        db.connect();

    def close():
        db.close;
