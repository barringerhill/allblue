from lxml import etree;
from progress.bar import Bar;

import requests as r;

import json;
import random;
import re;
import time;

class Block:

    def __init__(self, height = 0):
        self.height = height;
        self.time = "";
        self.txs = 0;        
        self.txs_n = 0;
        self.inner_txs_n = 0;

    def init_tx(self):
        self.__get_txs_n();
        self.__get_txs();
        
    def __get_txs_n(self):
        txs_api = "https://etherscan.io/block/" + str(self.height);
        html = etree.HTML(r.get(txs_api).text);
        # time
        time = re.compile("\(\S*\s\S*").search(str(
            html.xpath("//div[@id = 'ContentPlaceHolder1_maintable']//div[4]//text()")
        ))[0][1:];

        # txs_n
        try:
            txs_n = re.compile("[1-9]\d").findall(str(
                html.xpath("//a[@title = 'Click to View Transactions']//text()")
            ))[0];
        except: txs_n = 0;

        # inner_txs_n
        try:
            inner_txs_n = re.compile("[1-9]\d").findall(str(
                html.xpath("//a[@title = 'Click to View Internal Transactions']//text()")
            ))[0];
        except: inner_txs_n = 0;
        
        
        self.time = str(time);
        self.txs_n = txs_n;
        self.inner_txs_n = inner_txs_n;

    def __get_txs(self):
        if self.txs_n == 0:
            self.txs = [];
            return;
        
        pages = (int(self.txs_n) // 50) + 1;
        api = "https://etherscan.io/txs?block=" + str(self.height) + "&p="
        txs = [];
        for i in range(pages):
            c_api = api + str(i + 1);
            c_html = etree.HTML(r.get(c_api).text);
            c_txs = c_html.xpath("//tr/td[1]//span[@class='address-tag']//a//text()");
            txs.extend(c_txs);

        self.txs = txs;
        
    def get_contents(self):
        tx_api = "https://etherscan.io/tx/";
        contents = [];
        
        for tx in Bar('Fetch Txs:').iter(self.txs):
            html = etree.HTML(r.get(tx_api + str(self.txs[0])).text);
            input_data = html.xpath("//span[@id = 'rawinput']//text()");
            contents.append(str(input_data[0]));
            time.sleep(math.floor(random.random() * 5));
            
        return contents;

    def get_last(self):
        api = "https://etherscan.io/";
        html = etree.HTML(r.get(api).text);
        return html.xpath("//span[@id = 'ContentPlaceHolder1_Label1']//font//text()");


# test
def test_block():
    block = Block(6115134);
    block.init_tx();
    print(block.height);
    print(block.time);    
    print(block.txs_n);
    print(block.inner_txs_n);
    print(block.get_contents());

# test_block();
