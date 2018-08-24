from peewee import *;

db = SqliteDatabase('the.fox');

class BaseModel(Model):
    class Meta:
        database = db;

class Block(BaseModel):
    # id = IntegerField();
    difficulty = IntegerField();
    gas_limit = IntegerField();
    gas_used = IntegerField();
    hash = CharField(unique = True);
    number = IntegerField(unique = True);
    size = IntegerField();
    timestamp = IntegerField();
    total_difficulty = IntegerField();
    txs_n = IntegerField();
    finished = IntegerField();

class Tx(BaseModel):
    # id = IntegerField();
    block_hash = IntegerField(unique = True);
    gas = IntegerField();
    gas_price = IntegerField();
    hash = CharField(unique = True);
    input = CharField();
    value = FloatField();
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
