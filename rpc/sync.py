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
    def __getitem__(self, key):
        return getattr(self, key);

    def __setitem__(self, key, value):
        return setattr(self, key, value);
    
    def __init__(self, _tx):
        tx = w3.eth.getTransaction(_tx);

        self.hash = str(tx['hash'].hex());
        self.input = tx['input'];


def batch(number):
    block = w3.eth.getBlock(number);
    orphan_txs = block['transactions'];
    decode_txs = [];
    
    for tx in orphan_txs:
        # filter Contract Methods
        if len(w3.eth.getTransactionReceipt(tx).logs) is not 0:
            continue;

        # filter Contract Creation
        if w3.eth.getTransactionReceipt(tx).contractAddress is not None:
            continue;

        # convert hex to ascii;
        de = Tx(tx).input[2:]
        unhex = binascii.unhexlify(de);
        
        try:
            sec_de = str(unhex, 'utf8', 'ignore');
        except:
            continue;

        # filter Zero String
        if re.compile('\w').search(sec_de) is None:
            continue;

        # filter Invalid \x00
        if re.compile('\x00').search(sec_de) is not None:
            continue
        
        slim_tx = Tx(tx);
        slim_tx.input = sec_de;
        decode_txs.append(slim_tx);

    return decode_txs;
        
# test
# the = batch(6007493);
# for i in the:
#     print(i.input);
