// Corpyright 2018 @udtrokia
//  core/blockchain.go >> 
//
//
//
package main;

import (
	"fmt"
	"encoding/json"
	"github.com/ethereum/go-ethereum/ethdb"
	"github.com/ethereum/go-ethereum/node"
	"github.com/ethereum/go-ethereum/core/rawdb"
)

// DefaultConfig contains reasonable default settings.
// var DefaultConfig = Config{
// 	DataDir:          DefaultDataDir(),
// 	HTTPPort:         DefaultHTTPPort,
// 	HTTPModules:      []string{"net", "web3"},
// 	HTTPVirtualHosts: []string{"localhost"},
// 	WSPort:           DefaultWSPort,
// 	WSModules:        []string{"net", "web3"},
// 	P2P: p2p.Config{
// 		ListenAddr: ":30303",
// 		MaxPeers:   25,
// 		NAT:        nat.Any(),
// 	},
// }

func main() {
	// SetConfig
	var _config node.Config;
	_config = node.DefaultConfig;
	///// Reset Dir
	_config.DataDir = "/Users/mercury/tmp/Ethereum/geth/chaindata";
	fmt.Printf("DataDir: %v\n", _config.DataDir);


	// db
	var _db ethdb.Database;
	var err error;
	_db, err = ethdb.NewLDBDatabase( _config.DataDir, 768, 16);
	if err != nil { panic(err) }
	fmt.Printf("resolve path: %s\n", _config.ResolvePath(_config.DataDir));
	fmt.Printf("dbinfo: %v\n", _db);
	defer _db.Close();

	//// Find Block
	_hash := rawdb.ReadCanonicalHash(_db, 46214)
	fmt.Printf("HASH: %x\n", _hash);
	_block := rawdb.ReadBlock(_db, _hash, 46214)
	fmt.Printf("Block: %v\n", _block);
	if _data, err := json.Marshal(_block.Body()); err == nil {
		fmt.Printf("JSON: %s\n", _data);
	}
}
