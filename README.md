# ERC20TokenWhaleWatcher
### 
Under Construction/ Python 3.6
### 
Tracking Ethereum Token Whales<br />
### 
This script parses the data found in etherscan(Live Blockchain Explorer) and traces transactions bigger than amounts that you can customized. Then it logs the  
and saves addresses and the exact amounts in a sqlite database.<br />
###
Create the txt in the same directory with the script. Run as ```python whaleLogger.py  {ERC20 Contract, option} {watched minimum quantity, option}```<br />
default token is EOS ERC20 Contract,default watched minimum quantity is 10000<br />
### 
Note: This is the first draft. Thanks to nikoskar,I directly fork from his.

