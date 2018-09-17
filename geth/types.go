//
// @udtrokia
//

package allblue;

type Transaction struct {
	Number   uint64 
	Hash     string 
	Data     []byte 
}

type Block struct {
	Number          uint64
	Hash            string
	Transactions    []Transaction
}
