# ERC20TokenWhaleWatcher
### 
Under Construction/ Python 3.6
### 
Tracking Ethereum Token Whales<br />
### 
This script parses the data found in etherscan(Live Blockchain Explorer) and traces transactions bigger than amounts that you can customized. Then it logs and saves addresses and the exact amounts in a sqlite database.<br />
###
Run as ```python tokenWhaleWatcher.py [ERC20 Contract] [watched minimum quantity]```<br />
you can search ERC20 Contract in https://etherscan.io/tokens<br />
default token is EOS ERC20 Contract,default watched minimum quantity is 10000<br />
<br />
e.g.:
```python tokenWhaleWatcher.py 0x86fa049857e0209aa7d9e616f7eb3b3b78ecfdb0 10000```<br />
```python tokenWhaleWatcher.py```<br />

### 
Note: This is the first draft. Thanks to nikoskar,I directly fork from his.

