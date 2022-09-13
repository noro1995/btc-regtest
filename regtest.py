
from bitcoinlib.services.bitcoind import *
from pprint import pprint
import time

bdc = BitcoindClient(base_url='http://rpc:rpc@localhost:8336')
while True:
    print("Current blockheight is %d" % bdc.proxy.getblockcount())
    address = bdc.proxy.getnewaddress()
    print("Mine 1 blocks and generate regtest coins to address %s" % address)
    bdc.proxy.generatetoaddress(1, address)
    print("Current blockheight is %d" % bdc.proxy.getblockcount())
    address2 = 'mnS1dUyAomv9Mrp1Me75KcS5VAqBBJiWFb'
    address3 = 'mydB2JmR8M2E6QjKsahMhrm6LThH1jfW4a'
    print("Send 10 rBTC to address2 %s" % address2)
    print("Send 10 rBTC to address3 %s" % address3)
    bdc.proxy.settxfee(0.00002500)
    txid1 = bdc.proxy.sendtoaddress(address2, 10)
    txid2 = bdc.proxy.sendtoaddress(address3, 10)
    print("Resulting txid1: %s" % txid1)
    print("Resulting txid2: %s" % txid2)
    tx1 = bdc.proxy.gettransaction(txid1)
    tx2 = bdc.proxy.gettransaction(txid2)
    pprint(tx1)
    pprint(tx2)
    time.sleep(30)