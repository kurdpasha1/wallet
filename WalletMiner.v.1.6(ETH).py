from web3 import Web3
import config as config
import random
import string
import os
import binascii
from time import sleep
from pystyle import Colors, Colorate
ab=[0]
fz=[0]
def genrprivkey():
    pk=binascii.hexlify(os.urandom(32)).decode()
    return pk

a=[0]
f=[0]
os.system('title        v.1.6.0  ')

color = random.randint(1,7)
if color == 1:
    color=Colors.purple_to_blue
if color == 2:
    color=Colors.cyan_to_blue
if color == 3:
    color=Colors.green_to_blue
if color == 4:
    color=Colors.green_to_yellow
if color == 5:
    color=Colors.green_to_cyan 
if color == 6:
    color=Colors.yellow_to_red
if color == 7:
    color=Colors.purple_to_red
    
#printing the banner
print(Colorate.Vertical(color,'''

██╗    ██╗ █████╗ ██╗     ██╗     ███████╗████████╗    ███╗   ███╗██╗███╗   ██╗███████╗██████╗     ██╗   ██╗  ██╗    
██║    ██║██╔══██╗██║     ██║     ██╔════╝╚══██╔══╝    ████╗ ████║██║████╗  ██║██╔════╝██╔══██╗    ██║   ██║ ███║   
██║ █╗ ██║███████║██║     ██║     █████╗     ██║       ██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝    ██║   ██║ ╚██║
██║███╗██║██╔══██║██║     ██║     ██╔══╝     ██║       ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗    ╚██╗ ██╔╝  ██║
╚███╔███╔╝██║  ██║███████╗███████╗███████╗   ██║       ██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║     ╚████╔╝██╗██║
 ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝       ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝      ╚═══╝ ╚═╝╚═╝

 
                             ╔══════════════════════════════════════════════════╗
                             ║       Discord: https://discord.gg/UjmBCCeDRU     ║
                             ╚══════════════════════════════════════════════════╝
                                                                                                                             
''',True))


def transaction(prov,miner_adress,key,adress,bal):
    web3 = Web3(Web3.HTTPProvider(prov))
    
    adress1=Web3.toChecksumAddress(adress)
    adress2=Web3.toChecksumAddress(miner_adress)

    nonce=web3.eth.getTransactionCount(adress1)
    tx = {
        'chainId': 1,
        'nonce': nonce,
        'to': adress2,
        'value': web3.toWei(bal,'ether'),
        'gas': 21000,
        'gasPrice': web3.toWei(40, 'gwei')
    }
    signed_tx=web3.eth.account.signTransaction(tx, key)
    tx_Transaction=web3.eth.sendRawTransaction(signed_tx.rawTransaction)



import threading
import web3

#info thread
def infothread():
    cps=0
    while True:
        sleep(1)
        os.system('title v.1.6 checked: '+str(a[0])+' CPS: '+str(a[0]-cps))
        cps=0
        cps=a[0]


        
def run(prov, semaphore, miner_address):
    w3 = web3.Web3(web3.HTTPProvider(prov))
    while True:
        try:
            key=genrprivkey()
            rpctest=1
            try:
                adress= w3.eth.account.privateKeyToAccount(key).address
            except:
                rpctest=0
                print('Get address from private key error')
            if rpctest==1:
                
                tx_count=w3.eth.getTransactionCount(adress)
                
                if tx_count > 0:

                    try:
                        balance1  = w3.eth.get_balance(adress)/1000000000000000000
                        balance2  = w3.eth.get_balance(adress)/1000000000000000000
                        with semaphore:
                            hitstxt = open("hits.txt", "a")
                            hitstxt.write('\n')
                            hitstxt.write(key+'  '+adress+' BAL: '+str(balance1)+' BAL: '+str(balance2))
                            hitstxt.close()
                    except:
                        print('error')
                    print(key+'  '+adress+' tx count:  '+str(tx_count)+' BAL: '+str(balance1)+' BAL: '+str(balance2))
                
                else:
                    with semaphore:
                        print(Colorate.Color(Colors.red,'tx count: '+str(tx_count)+'   '+key+'   '+adress))
                        a[0]=a[0]+1
        except:
            pass

print(Colorate.Horizontal(Colors.red_to_purple,'The input should not have spaces at the end or beginning, please consider this.'))
print('')
miner_address=input(Colorate.Horizontal(Colors.purple_to_blue,'please enter your eth address :'))


#ETH api
we3 = Web3(Web3.HTTPProvider('https://eth-mainnet.gateway.pokt.network/v1/5f3453978e354ab992c4da79'))


#checking the ETH address
try:
    mineraddrescheck=we3.eth.get_balance(miner_address)
    print(Colorate.Color(Colors.green,'eth address is valid'))
except:
    print(Colorate.Color(Colors.red,'This address is not valid'))
    sleep(2)
    exit()


semaphore = threading.Semaphore(1)
threads = []
print('')
print(Colorate.Color(Colors.red,'               -- Miner started --'))

#setting up info thread
t = threading.Thread(target=infothread, args=())
threads.append(t)
t.start()


#starting the miner
for i in range(200):
    try:
        t = threading.Thread(target=run, args=('https://eth-mainnet.gateway.pokt.network/v1/5f3453978e354ab992c4da79', semaphore, miner_address))
        threads.append(t)
        t.start()
    except:
        break

for t in threads:
    t.join()






