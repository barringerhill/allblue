import db;
import sync;

from progress.bar import Bar;
from web3.auto import w3;

def get_local_height():
    try:
        local_height = db.Block.select().count();
        if db.Block.get(db.Block.number == local_height).finished == 1:
            local_height += 1;
            return local_height
    except:
        return 0;

def store_blocks():
    db.FoxDB().init();
    db.FoxDB().start();

    local_height = get_local_height();
    remote_height = w3.eth.syncing.currentBlock;
    
    for i in Bar('Stored Blocks:').iter(range(local_height, remote_height)):
        block = sync.Block(i);
        db.Block.create(
            difficulty = block['difficulty'],
            gas_limit = block['gas_limit'],
            gas_used = block['gas_used'],
            hash = block['hash'],
            number = block['number'],
            size = block['size'],
            timestamp = block['timestamp'],
            total_difficulty = block['total_difficulty'],
            txs_n = block['txs_n'],
            finished = 1,
        )

def main():
    store_blocks();    
    # while True:
    #     try:
    #         store_blocks();
    #     except:
    #         continue;

main();

# TEST
# def test():
#     t = db.Block.select();
#     for b in t:
#         print(b.txs_n)
# 
# test();
