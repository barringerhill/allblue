package main;

import (
	"github.com/ethereum/go-ethereum/common"
	"github.com/ethereum/go-ethereum/ethdb"	
	"github.com/ethereum/go-ethereum/core/rawdb"
)

type Transaction struct {
	Number   uint64
	Hash     common.Hash
	Data    []byte
}

type Block struct {
	Number          uint64
	Hash            common.Hash
	Transactions    []Transaction
}

func GetBlock(db ethdb.Database, number uint64) Block {
	hash := rawdb.ReadCanonicalHash(db, number);
	block := rawdb.ReadBlock(db, hash, number);

	var txs []Transaction;
	for _, tx := range(block.Transactions()) {
		txs = append(txs, Transaction{
			Number: number,
			Hash: tx.Hash(),
			Data: tx.Data(),
		})
	}
	
	return Block{
		Number:        number,
		Hash:          hash,
		Transactions:  txs,
	}
}
