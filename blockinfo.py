# import
# from solc import compile_standard,compile_source, compile_files, link_code
import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()
node_provider = os.environ['NODE_PROVIDER_LOCAL']
w3 = Web3(Web3.HTTPProvider(node_provider))

# Check connection status
print("Connection status: ")
print(w3.isConnected())
#Search block numbers
print("Block numbers: ")
print(w3.eth.blockNumber)
#check balance
balance = w3.eth.getBalance(w3.eth.accounts[0])
print("Balance of the account 1: ")
print(w3.fromWei(balance,"ether"))

