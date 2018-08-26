import db;

def insert():
    db.Tx.create(
        block_number = 1,
        hash = '1',
        input = '1',
        finished = 1,
    );
    print("Insert Succeed!")

def read():
    print("total query: [", db.Tx.select().count(), "]")
    for t in db.Tx.select():
        print(t.hash, "input:", t.input)

arg = input("choose function: (1) insert data  (2) read data :  ");
if arg == str(1):
    insert();
else:
    read();
