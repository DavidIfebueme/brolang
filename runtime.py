import os
import time
from dotenv import load_dotenv
from web3 import Web3
from eth_account import Account

load_dotenv()

PRIVATE_KEY = os.getenv("PRIVATE_KEY")
RPC_URL = os.getenv("RPC_URL")
CHAIN_ID = int(os.getenv("CHAIN_ID"))

w3 = Web3(Web3.HTTPProvider(RPC_URL))
wallet = None

def connect_wallet(address):
    global wallet
    acct = Account.from_key(PRIVATE_KEY)
    if acct.address.lower() != address.lower():
        raise ValueError("PRIVATE_KEY does not match given wallet address.")
    wallet = acct
    print(f"[+] Connected wallet: {acct.address}")

def call_contract(method, args):
    print(f"[~] Would call method '{method}' with args {args}")
    # Placeholder - add ABI + contract interaction later

def vibe_check(msg):
    print(f"[💬] {msg}")

def hodl(seconds):
    print(f"[🕒] Holding for {seconds} seconds...")
    time.sleep(seconds)

def bail():
    print("[🚪] Exiting. Paper hands mode.")
    exit()
