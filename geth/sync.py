import re;
import binascii;
from web3.auto import w3

# Block
class Block:
    def __getitem__(self, key):
        return getattr(self, key);

    def __setitem__(self, key, value):
        return setattr(self, key, value);
    
    def __init__(self, number = 0):
        block = w3.eth.getBlock(number);

        self.difficulty = block['difficulty'];
        self.gas_limit = block['gasLimit'];
        self.gas_used = block['gasUsed'];
        self.hash = str(block['hash'].hex());
        self.number = number;
        self.size = block['size'];
        self.timestamp = block['timestamp'];
        self.total_difficulty = block['totalDifficulty'];
        self.txs_n = len(block['transactions'])

# Tx        
class Tx():
    def __init__(self, _tx):
        tx = w3.eth.getTransaction(_tx);
        
        self.block_hash = str(tx['blockHash'].hex());
        self.gas = tx['gas']
        self.gas_price = tx['gasPrice'];
        self.hash = str(tx['hash'].hex());
        self.input = tx['input'];
        self.value = tx['value'] / 1000000000000000000;


def batch(number):
    block = w3.eth.getBlock(number);    
    orphan_txs = block['transactions'];
    decode_txs = [];
    
    for tx in orphan_txs:
        try:
            de = Tx(tx).input[2:]
            sec_de = str(binascii.unhexlify(de), 'utf8', 'ignore');
            if re.compile('\w').search(sec_de) is not None:
                print(sec_de);
                decode_txs.append(sec_de);
        except:
            pass;

    return decode_txs;
        
# test
# def test_block():
#     the = batch(3666666);

# test_block();
