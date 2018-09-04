import db;
import sync;

from progress.bar import Bar;
from web3.auto import w3;

def get_local_height(t):
    table = None;
    
    if t == "b":
        try:
            table = db.Block                
            last_count = table.select().count();
            last_query = table.select()[last_count - 1];
            # if the below query is not completed, panic.
            return last_block.number + 1;
        except:
            return 0;
    
    elif t == "t":
        try:
            table = db.Tx;
            last_count = table.select().count();
            last_query = table.select()[last_count - 1].hash;
            print(last_query);
            last_number = w3.eth.getTransaction(last_query)['blockNumber'];
            return last_number + 1;
        except:
            return 46000;

    else:
        return 0;

def store():
    db.FoxDB().init();
    db.FoxDB().start();

    arg = input("(b): store block, (t): store txs: ");
    
    local_height = get_local_height(arg);
    remote_height = w3.eth.syncing.currentBlock;    

    print("local_height: ", local_height);
    
    if arg == 'b':
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

    else:
        for i in Bar('Stored Txs:').iter(range(local_height, remote_height)):
            txs = sync.batch(i);
            for tx in txs:
                db.Tx.create(
                    hash = tx['hash'],
                    input = tx['input'],
                )
                
def main():
    store();    

main();

