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
		if g.FliterTx(tx.Hash(), tx.Data()) != true { continue };
		txs = append(txs, Transaction {
			Number: number,
			Hash:   tx.Hash().Hex(),
			Data:   tx.Data(),
		})
	}
	
	return Block{
		Number:        number,
		Hash:          hash.Hex(),
		Transactions:  txs,
	}	
}

func (g *Geth) FliterTx(hash common.Hash, data []byte) bool {
	var (emptyHex = "0x0000000000000000000000000000000000000000";)
	
	// Receipt
	receipt, _, _, _ := rawdb.ReadReceipt(g.database, hash);
	logs,  contract_address := receipt.Logs, receipt.ContractAddress

	// Fliter Contract
	if len(logs) != 0 { return false };
	if contract_address.Hex() != emptyHex {return false };

	// Fliter Data
	if len(data) == 0 { return false };
	for _, b := range(data){
		if b <= 21 { return false}
	}
	fmt.Printf("Data: %v;\nLength: %v\n", data, len(string(data[:])));
	fmt.Printf("Data String: %x\n, Hash: %x\n", data, hash);
	return true;
}
