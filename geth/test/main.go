//
// @udtrokia
//

package main;

import (
	"fmt"
	"github.com/udtrokia/allblue"
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/postgres"
)

type Tx struct {
	Number  uint64  `gorm:"not null;"`
	Hash    string  `gorm:"not null;"`
	Data    string  `gorm:"not null;unique;unique_index;"`
}



func main() {
	// PostgreSQL
	pg, err := gorm.Open("postgres", "host=127.0.0.1 port=5432 dbname=allblue sslmode=disable");
	if err != nil { panic(err) }; defer pg.Close();

	pg.AutoMigrate(&Tx{});
	pg.LogMode(false);
	
	// AllBlue
	geth := allblue.New("/path/to/Ethereum/geth/chaindata");
	defer geth.Database.Close();

	
	// -------
	var _tx Tx;
	pg.Raw("select MAX(number) number from txes;").Scan(&_tx);
	fmt.Printf("Last pointer: %v\n", _tx.Number);
	for ptr := _tx.Number; ; ptr++ {
		block := geth.GetBlock(ptr);
		for _, tx := range block.Transactions {
			err := pg.Create(&Tx{
				Number: tx.Number,
				Hash:   tx.Hash,
				Data:   string(tx.Data[:]),
			});
			if err != nil { continue }

		}
		fmt.Printf("\rSync Block: %v", block.Number);
	}
}
