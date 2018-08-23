from web3.auto import w3

# Block
class Block:
    def __init__(self, number = 0):
        block = w3.eth.getBlock(number);

        self.difficulty = block['difficulty'];
        self.gasLimit = block['gasLimit'];
        self.gasUsed = block['gasUsed'];
        self.hash = str(block['hash'].hex());
        self.number = number;
        self.size = block['size'];
        self.timestamp = block['timestamp'];
        self.totalDifficulty = block['totalDifficulty'];
        self.txs_n = len(block['transactions'])

# Tx        
class Tx():
    def __init__(self, _tx):
        tx = w3.eth.getTransaction(_tx);
        
        self.block_hash = str(tx['blockHash'].hex());
        self.gas = tx['gas']
        self.gas_price = tx['gasPrice'];
        self.hash = str(tx['hash'].hex());
        self.input = str(tx['input']);
        self.value = tx['value'] / 1000000000000000000;


def batch(number):
    block = w3.eth.getBlock(number);    
    orphan_txs = block['transactions'];
    wrapped_txs = [];
    
    for tx in orphan_txs:
        wrapped_txs.append(Tx(str(tx.hex())))
        
    return wrapped_txs;
        
# test
def test_block():
    # block = Block(4000000);
    tx = Tx('0xb1ed364e4333aae1da4a901d5231244ba6a35f9421d4607f7cb90d60bf45578a');
    # the_batch = batch(4000000);
    
    # print('\n', block.__dict__, '\n\n');
    print(tx.__dict__);
    # print(the_batch);
    # for b in the_batch:
    #     print(b.input)

test_block();
