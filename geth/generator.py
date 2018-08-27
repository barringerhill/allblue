import db;

# db init
db.FoxDB().init();
db.FoxDB().start();

def insert():
    db.Block.create(
        difficulty = 1,
        gas_limit = 1,
        gas_used = 1,
        hash = 'h',
        number = 1,
        size = 1,
        timestamp = 1,
        total_difficulty = 1,
        txs_n = 1,
    );

    db.Tx.create(
        block_number = 1,
        gas = 1,
        gas_price = 1,
        hash = 'hash',
        input = 'input',
        value = '1.00',
    )
    print("Insert Succeed!")

def read():
    print("\nTotal `Block` query: [", db.Block.select().count(), "]")
    for b in db.Block.select():
        print("hash: ", b.hash, "  time:", b.timestamp)

    print("\nTotal `Tx` query: [", db.Tx.select().count(), "]")
    for tx in db.Tx.select():
        print("hash: ", tx.hash, "  input:", tx.input)

arg = input("choose function: (1) insert data  (2) read data :  ");
if arg == str(1):
    insert();
else:
    read();
