### GET DATA FROM LEVELDB

### TODO

+ [ ] METHODS
  + [ ] GetTransaction
+ [ ] Format
+ [ ] PSQL Interface



### Find The Code.

#### Config

+ go-ethereum/eth/config.go

+ go-ethereum/node/config.go


#### Database

+ Interface Rewrite

    ```go
    // go-ethereum/service.go
    func (ctx *ServiceContext) OpenDatabase(name string, cache int, handles int) (ethdb.Database, error) { ... }
    ```

#### Blockchain

+ Interface Rewrite

  ```go
  // Interface REWRITE
  interface {
      GetBlockHashByNumber(db ethdb.Database, number uint64) common.hash
      // rawdb.ReadCanonicalHash(db, number) -> hash
      
      GetBlock(db ethdb.Database, hash common.hash, number uint64) *types.Block
      // rawdb.ReadBlock(db, hash, number) -> block
  }
  ```

+ core/blockchain.go

  ```go
  // go-ethereum/core/blockchain.go
  
  // GetBlockByNumber
  func (bc *BlockChain) GetBlockByNumber(number uint64) *types.Block { ... }

  // GetBlock 
  func (bc *BlockChain) GetBlock(hash common.Hash, number uint64) *types.Block { ... }
  ```


#### Transaction

+ Interface Rewrite

  ```go
  interface{
    	GetTransactionByHash(db ethdb.Database, hash common.hash) tx
  }
  ```

+ internal/ethapi/api.go

  ```go
  func (s *PublicTransactionPoolAPI) GetTransactionByHash(ctx context.Context, hash common.Hash) *RPCTransaction { ... }
  ```
