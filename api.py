import requests as r;
import json;

class Block:

    def __init__(self, height):
        self.height = height;

    def get_api(self):
        return "https://api.blockcypher.com/v1/eth/main/blocks/" + str(self.height) + "?txstart=0\u0026limit=500";
        
    def get_tx(self):
        res = r.get(self.get_api());
        info = json.loads(res.text)
        txids = info.get("txids");        
        internal_txids = info.get("internal_txids");

        if internal_txids:
            txids.extend(internal_txids);

        return txids;

class Tx:
    def __init__(self, tx):
        self.txids = txids;

    def get_api(self, tx):
        return "https://api.blockcypher.com/v1/eth/main/txs/" + tx;
        
    def get_script(self):
        print(txids);
        return r.get(self.get_api(txids[0])).text;


# test
block = Block(6109000);
txids = block.get_tx();
txs = Tx(txids);

print(txs.get_script());

