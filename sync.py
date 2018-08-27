import re;
import binascii;
from web3.auto import w3

class Tx():
    def __getitem__(self, key):
        return getattr(self, key);

    def __setitem__(self, key, value):
        return setattr(self, key, value);
    
    def __init__(self, _tx, number):
        tx = w3.eth.getTransaction(_tx);

        self.block_number = number;
        self.hash = str(tx['hash'].hex());
        self.input = tx['input'];

def batch(number):
    block = w3.eth.getBlock(number);
    orphan_txs = block['transactions'];
    decode_txs = [];
    
    for tx in orphan_txs:
        if len(w3.eth.getTransactionReceipt(tx).logs) is not 0:
            continue;

        if w3.eth.getTransactionReceipt(tx).contractAddress is not None:
            continue;

        de = Tx(tx, number).input[2:]
        unhex = binascii.unhexlify(de);

        try:
            sec_de = str(unhex, 'utf8');
        except:
            continue;

        if re.compile('\w').search(sec_de) is None:
            continue;

        if re.compile('\x00').search(sec_de) is not None:
            continue
            
        slim_tx = Tx(tx, number);
        slim_tx.input = sec_de;
        decode_txs.append(slim_tx);

    return decode_txs;

# test
# print('----test----')
the = batch(5490403);
