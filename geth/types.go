//
// @udtrokia
//

package allblue;

type Transaction struct {
	Number   uint64 `gorm: "not null"`
	Hash     string `gorm: "not null"`
	Data     []byte `gorm: "not null; unique; index;"`
}

type Block struct {
	Number          uint64
	Hash            string
	Transactions    []Transaction
}
