# import
# from solc import compile_standard,compile_source, compile_files, link_code
import os
import json
from dotenv import load_dotenv
from eth_account import account
from eth_utils.currency import to_wei
from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider, contract, eth
from web3.types import SignedTx


load_dotenv()
node_provider = os.environ['NODE_PROVIDER_LOCAL']
w3 = Web3(Web3.HTTPProvider(node_provider))

w3.geth.personal.unlockAccount(w3.eth.accounts[0],os.environ['PASSWORD_1'],10000)

# setup the default account
w3.eth.defaultAccount = w3.eth.accounts[0]

private_key = os.environ['PRIVATE_KEY_1']

# Get the nonce & Build the transaction
nonce = w3.eth.getTransactionCount(w3.eth.accounts[0])
tx = {
    'chainId': 110501,
    'nonce': nonce,
    'to':w3.eth.accounts[1],
    'value': w3.toWei(1,'ether'),
    'gas': 100000,
    'gasPrice': w3.toWei(20,'gwei')
}
# Sign the transaction
signed_tx = w3.eth.account.signTransaction(tx, private_key)
# Send the transaction
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
# Get the transaction hash
print(tx_hash)