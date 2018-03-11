import time
import os
import sys
import re
import requests
from bs4 import BeautifulSoup as bs

from dataBase import dataBase




def main(contractaddress, sqlname, minsize):
    data = []
    try:
        # send the request to the site and check for download errors with
        # raise_for_status()
        req = requests.get('https://etherscan.io/token/generic-tokentxns2?contractAddress=' +
                           str(contractaddress) + '&a=&mode=')
        req.raise_for_status()
    except Exception as e:
        print(e)
    else:
        soupdata = bs(req.text, "html.parser")
        # the data list represents the table as taken from the html code of
        # https://etherscan.io/token/generic-tokentxns2?contractAddress={ERC20 Contract}&a=&mode=
        # It's a list containing lists. Each nested list represents a row from the
        # table. Every list has size = 50, except the first one is col name,  and contains the following info:
        # [TxHash, Age, From, To, Quantity]
        table = soupdata.select('table')
        # print(table)
        rows = table[0].select('tr')
        # print(rows)
        for row in rows:
            # the first one shoud be except
            if(row.select('th')):
                continue
            cols = row.select('td')
            # get age ,we want accurate time,now it is UTC time
            colex = str(cols[1].find('span', attrs={"title": re.compile(r"(\s\w+)?")})['title'])
            # except age
            cols = [ele.text.strip() for ele in cols if(ele != cols[1])]
            # add time to the end of data
            data.append([ele for ele in cols if ele] + list((colex,)))
            # Get rid of empty values
            # this is optional and not necessary. Could be used for future data analysis

    # Time to spot some whales. You can change the condition to your preference
    # I use 10K as a flag cause i have noticed that whales tend to split the big
    # amounts to 10-20K transactions and spread them to multiple wallets.
    for i in data:
        txHash, send, rev, amount, time = i
        # except the thousandth
        stramount = str(amount).replace(',', '')
        if (float(stramount)) > float(minsize) and dataBase.read(sqlname, str(txHash))==None:
            dataBase.write(sqlname, txHash, time, send, rev, amount)
            print(time + " " + 5 * "." + " " + rev + " " + 5 * "." + " " + str(amount))

# set sys.argv with default value
def default_argv(pos,default_value):
    return sys.argv[int(pos)] if len(sys.argv) > int(pos) else str(default_value)
if __name__ == '__main__':

    try:
        print(sys.argv)
        contractaddress = default_argv(1, "0x86fa049857e0209aa7d9e616f7eb3b3b78ecfdb0")
        minsize = default_argv(2, 10000)
        # auto create table as your input ERC20 Contract,
        # usually,the sql name I just get the the  last 6 places,before it ,add just letter from -12 to -6
        # as the sql table first place is only just letter.
        sqlname = re.sub("[^A-Za-z]", "", str(contractaddress)[-12:-6]) + str(contractaddress)[-6:]
        dataBase.create(sqlname)
    except Exception as e:
        print(e)
    else:
        print("[+]Hello! Welcome to ERC20TokenWhaleWatcher!")
        # time.sleep(3)
        print("[+]This script traces ERC20 token whales parsing info from etherscan.io")
        print("[+]ERC20 token(search in https://etherscan.io/tokens) : " + contractaddress)
        print("[+]Watched minimum quantity : " + str(minsize))
        # time.sleep(3)
        print("[+]You can terminate the script anytime by pressing CTRL-Z")
        # time.sleep(3)
        # input("[+]If you are ready to find some whales press RETURN")

        while 1:
            # default token is EOS ERC20 Contract,default watch min size is 10000
            main(contractaddress, sqlname, minsize)
            # extract data from the source with a 15s time difference
            time.sleep(15)
