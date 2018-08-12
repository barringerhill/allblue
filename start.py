import tx;
import db;

def fetch_block(height):
    block = tx.Block(height);
    block.init_tx();
    return block;

def fetch_tx(block):
    block.get_contents();
    return block;

def fetch():
    db.FoxDB().init();    
    db.FoxDB().start();
    
    local_height = db.Block.select().count();
    remote_height = int(tx.Block().get_last()[0]);    
    
    for i in range(local_height, remote_height):
        print(i);
        block = fetch_block(i);
        db.Block.create(
            height = block.height,
            time = block.time,
            txs_n = block.txs_n,
            inner_txs_n = block.inner_txs_n,
            txs = block.txs,
            finished = 1,
        )
        print(block.height);

fetch();

def test():
    t = db.Block.select();
    for i in t:
        print(i.time)

test();
