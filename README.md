# ERC20TokenWhaleWatcher
### 
Under Construction/ Python 3.6
### 
Tracking Ethereum Token Whales<br />
### 
This script parses the data found in etherscan(Live Blockchain Explorer) and traces currentTokenHolders or currentTokenTransfers.<br />
## currentTokenTransfersWatcher
Run as ```python currentTokenTransfersWatcher.py [ERC20 Contract] [watched minimum quantity]```<br />
you can search ERC20 Contract in https://etherscan.io/tokens<br />
default token is EOS ERC20 Contract,default watched minimum quantity is 10000<br />
e.g.<br />
```python currentTokenTransfersWatcher.py 0x86fa049857e0209aa7d9e616f7eb3b3b78ecfdb0 10000```<br />
```python currentTokenTransfersWatcher.py```<br />

## currentTokenHoldersWatcher
Run as ```python currentTokenHoldersWatcher.py [ERC20 Contract] [watch max top holders]```<br />
you can search ERC20 Contract in https://etherscan.io/tokens<br />
default token is EOS ERC20 Contract,default watched top holders number is 100(the max value is 10000)<br />
e.g.<br />
```python currentTokenHoldersWatcher.py 0x86fa049857e0209aa7d9e616f7eb3b3b78ecfdb0 100```<br />
```python currentTokenHoldersWatcher.py```<br />

### 
Note: This is the first draft. Thanks to nikoskar,I directly fork from him.

