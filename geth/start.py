import tx;
import db;
from progress.bar import Bar;

def fetch_block(height):
    block = tx.Block(height);
    block.init_tx();
    return block;

def fetch_tx(block):
    block.get_contents();
    return block;

def mix_height():
    local_height = db.Block.select().count();
    remote_height = int(tx.Block().get_last()[0]);    

    if db.Block.get(db.Block.height == local_height).finished == 1:
        local_height += 1;

    return (local_height, remote_height);

def store_blocks():
    db.FoxDB().init();    
    db.FoxDB().start();
    
    (local_height, remote_height) = mix_height();

    for i in Bar('Stored Blocks:').iter(range(local_height, remote_height)):
        block = fetch_block(i);
        db.Block.create(
            height = block.height,
            time = block.time,
            txs_n = block.txs_n,
            inner_txs_n = block.inner_txs_n,
            txs = block.txs,
            finished = 1,
        )


def main():
    while True:
        try:
            store_blocks();
        except:
            continue;

# main();

# TEST
def test():
    t = db.Block.select();
    for b in t:
        print(b.txs_n)

test();
