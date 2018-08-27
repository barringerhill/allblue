import db;
import sync;

from progress.bar import Bar;
from web3.auto import w3;

def get_local_height():
    try:
        tx_count = db.Tx.select().count();
        print(tx_count)
        local_height = db.Tx.select()[tx_count - 1].block_number;
        
        if db.Tx.get(db.Tx.block_number == local_height).finished == 1:
            local_height += 1;
            
        return local_height
    except:
        return 0;

def store():
    db.FoxDB().init();
    db.FoxDB().start();

    local_height = get_local_height();
    remote_height = w3.eth.syncing.currentBlock;

    print("local height: ", local_height);
    for i in Bar('Stored Txs:').iter(range(local_height, remote_height)):
        txs = sync.batch(i);
        for tx in txs: 
            db.Tx.create(
                block_number = tx.block_number,
                hash = tx.hash,
                input = tx.input,
                finished = 1,
            )

    
def main():
    store();

main();
