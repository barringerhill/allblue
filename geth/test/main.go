//
// @udtrokia
//
package main;

import (
	"fmt"
	"sync"
	"time"
	"runtime"
	"crypto/md5"
	"encoding/hex"

	"github.com/udtrokia/allblue"
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/postgres"
)

type Tx struct {
	Number  uint64  `gorm:"not null;"`
	Hash    string  `gorm:"not null;"`
	Data    string  `gorm:"not null;"`
	SubHash string  `gorm:"not null;unique"`
}

var (
	mu sync.Mutex
	wait sync.WaitGroup
	geth = allblue.New("/Volumes/Hyperfox/Ethereum/geth/chaindata")
)

func main() {
	// pre-setting
	runtime.GOMAXPROCS(runtime.NumCPU());
	defer geth.Database.Close();
	
	// PostgreSQL
	pg, err := gorm.Open("postgres", "host=127.0.0.1 port=5432 dbname=allblue sslmode=disable");
	if err != nil { panic(err) }; defer pg.Close();
	
	pg.AutoMigrate(&Tx{});
	pg.LogMode(false);
	
	// -------
	var _tx Tx;
	ch := make(chan int, 4000)
	pg.Raw("select MAX(number) number from txes;").Scan(&_tx);
	fmt.Printf("Last pointer: %v\n", _tx.Number);
	for ptr := _tx.Number; ; ptr ++ {
	 	defer func(){ if r:= recover(); r != nil {} }()
		ch <- 1
	 	go insertTxs(ptr, pg, ch);
	 	fmt.Printf("\rSync Block: %v/6000000", ptr);
	}
}

func insertTxs(i uint64, pg *gorm.DB, ch chan int) {
	defer func(){ if r:= recover(); r != nil {} }()	
	block := geth.GetBlock(i);
	for _, tx := range block.Transactions {
		_hash := hash(tx.Data[:])
		pg.Create(&Tx{
			Number:     tx.Number,
			Hash:       tx.Hash,
			Data:       string(tx.Data[:]),
			SubHash:    _hash,
		});
	}
	time.Sleep(time.Second);
	<-ch
}

func hash (input []byte) string {
	hasher := md5.New()
	hasher.Write(input)
	return hex.EncodeToString(hasher.Sum(nil))
}
