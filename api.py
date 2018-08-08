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
        txids.extend(internal_txids);
        return txids;

class Tx:
    def tx_api(tx):
        return "https://api.blockcypher.com/v1/eth/main/txs/" + str(tx);


b = Block(3500000);
print(b.get_tx());

# res = r.get(block_api(1));
# print(res.text);
# print(json.loads(res.text).get("outputs")[0].get("script"));
