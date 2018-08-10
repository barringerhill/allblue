from lxml import etree;
from progressbar import *

import requests as r;

import json;
import random;
import re;
import time;

class Block:

    def __init__(self, height):
        self.height = height;
        self.time = None;
        self.txs = None;        
        self.txs_n = None;
        self.inner_txs_n = None;

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
        txs_n = re.compile("[1-9]\d").findall(str(
            html.xpath("//a[@title = 'Click to View Transactions']//text()")
        ))[0];

        # inner_txs_n
        inner_txs_n = re.compile("[1-9]\d").findall(str(
            html.xpath("//a[@title = 'Click to View Internal Transactions']//text()")
        ))[0];

        self.time = str(time);
        self.txs_n = txs_n;
        self.inner_txs_n = inner_txs_n;

    def __get_txs(self):
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
        progress = ProgressBar();
        
        for tx in progress(self.txs):
            html = etree.HTML(r.get(tx_api + str(self.txs[0])).text);
            input_data = html.xpath("//span[@id = 'rawinput']//text()");
            contents.append(str(input_data[0]));
            time.sleep(math.floor(random.random() * 5));
            
        return contents;

# test
def test_block():
    block = Block(6115134);
    block.init_tx();
    print(block.height);
    print(block.time);    
    print(block.txs_n);
    print(block.inner_txs_n);
    print(block.get_contents());

test_block();
