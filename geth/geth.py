from web3 import Web3;
web3 = Web3(Web3.IPCProvider('/Volumes/HyperFox/Ethereum/geth.ipc'))

connect = web3.isConnected()

print(web3.eth.getBlock(4000000))
