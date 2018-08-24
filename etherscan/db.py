from peewee import *;

db = SqliteDatabase('hyper.fox');

class BaseModel(Model):
    class Meta:
        database = db;

class Block(BaseModel):
    id = IntegerField();
    height = IntegerField(unique = True);
    time = CharField();
    txs_n = IntegerField();
    inner_txs_n = IntegerField();
    txs = CharField();
    finished = IntegerField();

class Tx(BaseModel):
    id = IntegerField();
    tx_id = CharField(unique = True);
    height = IntegerField(unique = True);
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
