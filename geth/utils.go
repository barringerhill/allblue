package main;

import 	(
	"fmt"
	
	"github.com/ethereum/go-ethereum/ethdb"
	"github.com/ethereum/go-ethereum/common"	
	"github.com/ethereum/go-ethereum/core/rawdb"	
)

// UTILS
func assert(err error) { if err != nil { panic(err) } }

// DATABASE
type Geth struct{
	Cache      int64
	Handles    int64
	DataDir    string
	database   ethdb.Database	
}

func Default() *Geth {
	datadir := "/Volumes/Hyperfox/Ethereum/geth/chaindata";
	db, err := ethdb.NewLDBDatabase(datadir, 768, 16);
	assert(err); 

	return &Geth{ database: db, DataDir: datadir };
}

func (g *Geth)  GetBlock(number uint64) Block {
	hash  := rawdb.ReadCanonicalHash(g.database, number);
	block := rawdb.ReadBlock(g.database, hash, number);

	var txs []Transaction;
	for _, tx := range(block.Transactions()) {
		txs = append(txs, Transaction {
			Number: number,
			Hash:   tx.Hash(),
			Data:   tx.Data(),
		})
	}
	
	return Block{
		Number:        number,
		Hash:          hash,
		Transactions:  txs,
	}	
}

func (g *Geth) FliterTx(hash common.Hash) bool {
	receipt, _, _, _ := rawdb.ReadReceipt(g.database, hash);
	logs,  contract_address := receipt.Logs, receipt.ContractAddress
	fmt.Printf("Logs: %v\n", logs);
	fmt.Printf("Contract Address: %x\n", contract_address);

	return true;
}
