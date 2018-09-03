tx = "0x4a110de8110bb9eb250bdeb772ecafd517dfa109c14ff5d93dcfb96e9c562bb8"

from web3.auto import w3;

t = w3.eth.getTransaction(tx);
print(t['blockNumber']);
