// 
// @udtrokia
//  

package main;

import "fmt"

func main() {
	_db := database();
	defer _db.Close();	

	block := GetBlock(_db, 46214);
	fmt.Printf("Number: %v\n", block.Number);
	fmt.Printf("Hash: %x\n", block.Hash);
	fmt.Printf("Transactions: %x\n", block.Transactions[0].Hash);
}
