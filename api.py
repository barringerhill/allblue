from lxml import etree;
import requests as r;
import json;
import re;

class Block:

    def __init__(self, height):
        self.height = height;
        self.html = None;
        self.txs_n = None;
        self.inner_txs_n = None;

    def init(self):
        self.get_html();
        self.get_txs_n();
        self.get_inner_txs_n();
        
    def get_html(self):
        txs_api = "https://etherscan.io/block/" + str(self.height);
        html = etree.HTML(r.get(txs_api).text);

        self.html = html;

    def get_txs_n(self):
        if self.html is None: self.get_html();
        html = self.html;
        txs_n = re.compile("[1-9]\d").findall(str(
            html.xpath("//a[@title = 'Click to View Transactions']//text()")
        ))[0];

        self.txs_n = txs_n;

    def get_inner_txs_n(self):
        if self.html is None: self.get_html();
        html = self.html;
        inner_txs_n = re.compile("[1-9]\d").findall(str(
            html.xpath("//a[@title = 'Click to View Internal Transactions']//text()");
        ))[0];

        self.inner_txs_n = inner_txs_n;

    def get_txs(self):
        pages = (int(self.txs_n) // 50) + 1;
        txs = html.xpath("//a[@title = 'Click to View Internal Transactions']//text()");
        print(pages);

# test
def test_block():
    block = Block(6115134);
    block.init();
    print(block.txs_n);
    print(block.inner_txs_n);

test_block();

# # # # # # # # # # # # # # # # # # 
#
# class Tx:
#     def __init__(self, txids):
#         self.txids = txids;
# 
#     def get_script(self, tx):
#         tx_api = "https://api.blockcypher.com/v1/eth/main/txs/" + tx;
#         j = r.get(tx_api).text;
#         outputs = json.loads(j).get("outputs")[0];
#         script = outputs.get("script");
#         
#         if script:
#             return script;
#         return;
# 
#     def scripts(self):
#         scripts = [];
#         for tx in txids:
#             scripts.append(self.get_script(tx));
# 
#         return scripts;
#
# # # # # # 


