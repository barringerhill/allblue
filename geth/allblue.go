//
// @udtrokia
//

package allblue;

import 	(
	"regexp"
	"unicode/utf8"
	
	"github.com/ethereum/go-ethereum/ethdb"
	"github.com/ethereum/go-ethereum/common"
	"github.com/ethereum/go-ethereum/core/rawdb"
)

// Methods
func assert(err error) { if err != nil { panic(err) } }

// DataBase
type Geth struct{
	Cache      int64
	Handles    int64
	DataDir    string
	Database   ethdb.Database	
}

func New(datadir string) *Geth {
	db, err := ethdb.NewLDBDatabase(datadir, 768, 16);
	assert(err);

	return &Geth{ Database: db, DataDir: datadir };
}

func (g *Geth)  GetBlock(number uint64) Block {
	hash  := rawdb.ReadCanonicalHash(g.Database, number);
	block := rawdb.ReadBlock(g.Database, hash, number);

	var txs []Transaction;
	for _, tx := range(block.Transactions()) {
		if g.FliterTx(tx.Hash(), tx.Data()) != true { continue };
		txs = append(txs, Transaction {
			Number: number,
			Hash:   tx.Hash().Hex(),
			Data:   tx.Data(),
		})
	}
	
	return Block{
		Number:        number,
		Hash:          hash.Hex(),
		Transactions:  txs,
	}	
}

func (g *Geth) FliterTx(hash common.Hash, data []byte) bool {
    	var (emptyHex = "0x0000000000000000000000000000000000000000";)
	
	// Get Receipt
	receipt, _, _, _ := rawdb.ReadReceipt(g.Database, hash);
	logs,  contract_address := receipt.Logs, receipt.ContractAddress;

	// Fliter Contract
	if len(logs) != 0 { return false }
	if contract_address.Hex() != emptyHex {return false; }

	// Fliter Data Checkpoint 1
	if len(string(data[:])) == 0 { return false; }
	if utf8.Valid(data) == false { return false; }

	// Fliter Data Checkpoint 2
	for _, b := range(data) { if b < 10 { return false; } }

	// Fliter Data Checkpoint 3
	matched, err := regexp.MatchString(`\w`, string(data[:]));
	assert(err); if matched == false { return false; }

	// Fliter Data Checkpoint 4
	matched, err = regexp.MatchString(`^[A-Z0-9]*$`, string(data[:]));
	assert(err); if matched == true { return false; }

	return true;
}
