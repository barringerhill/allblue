package main;

import (
	"github.com/ethereum/go-ethereum/common"	
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
