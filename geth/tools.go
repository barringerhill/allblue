package main;

import 	"github.com/ethereum/go-ethereum/ethdb"

var (
	datadir = "/Users/Mercury/Library/Ethereum/geth/chaindata";
)

func assert(err error) {
	if err != nil { panic(err) }
}

func database() ethdb.Database {
	_db, err := ethdb.NewLDBDatabase(datadir, 768, 16);
	assert(err); return _db;
}

