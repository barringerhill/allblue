### GET DATA FROM LEVELDB

### TODO

+ [ ] Format
+ [ ] Fliter
+ [ ] PSQL Interface


### Struct

```go
type Geth struct{
	Cache      int64
	Handles    int64
	DataDir    string
	Database   ethdb.Database	
}

type Block struct {
	Number          uint64
	Hash            string
	Transactions    []Transaction
}

type Transaction struct {
	Number   uint64
	Hash     string
	Data     []byte
}
```


### Methods.


```go
type Allblue interface{
	func New(datadir string) *Geth
	func (g *Geth)  GetBlock(number uint64) Block 
	func (g *Geth) FliterTx(hash common.Hash, data []byte) bool
}
```


### Example

```go
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
```

