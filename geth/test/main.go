//
// @udtrokia
//

package main;

import (
	"fmt"
	"github.com/udtrokia/allblue"
)

func main() {
	geth := allblue.New("/path/to/Ethereum/geth/chaindata");
	defer geth.Database.Close();

	block := geth.GetBlock(46214);
	for _, tx := range block.Transactions {
		fmt.Printf("Number: %d\n", tx.Number);		
		fmt.Printf("Hash: %v\n", tx.Hash);
		fmt.Printf("Data: %s\n", tx.Data);
	}
}
