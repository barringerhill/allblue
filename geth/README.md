### GET DATA FROM LEVEL DB



### Find The Code.



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
  
  // <-- GetBlockByNumber -->
  func (bc *BlockChain) GetBlockByNumber(number uint64) *types.Block {
  	hash := rawdb.ReadCanonicalHash(bc.db, number)
    // raw.db.ReadCanonicalHash(db.db, num);
    // This line get the block hash from the num.
    // What db do is offering `bc.db`
    
  	if hash == (common.Hash{}) {
  		return nil
  	}
  	return bc.GetBlock(hash, number)
  }
  
  // <-- GetBlock -->
  func (bc *BlockChain) GetBlock(hash common.Hash, number uint64) *types.Block {
  	// Short circuit if the block's already in the cache, retrieve otherwise
  	if block, ok := bc.blockCache.Get(hash); ok {
  		return block.(*types.Block)
  	}
  	block := rawdb.ReadBlock(bc.db, hash, number)
  	if block == nil {
  		return nil
  	}
  	// Cache the found block for next time and return
  	bc.blockCache.Add(block.Hash(), block)
  	return block
  }
  ```





#### Transaction

+ Interface

  ```go
  interface{
    GetTransactionByHash(db ethdb.Database, hash common.hash) tx
  }
  ```


+ internal/ethapi/api.go

  ```go
  func (s *PublicTransactionPoolAPI) GetTransactionByHash(ctx context.Context, hash common.Hash) *RPCTransaction {
  	// Try to return an already finalized transaction
  	if tx, blockHash, blockNumber, index := rawdb.ReadTransaction(s.b.ChainDb(), hash); tx != nil {
  		return newRPCTransaction(tx, blockHash, blockNumber, index)
  	}
    // ...
  }
  ```


