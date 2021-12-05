import json
import os
from solcx import compile_standard, install_solc
from web3 import Web3

def read_file(file_name):
    with open(file_name, "r") as file:
        simple_storage_file = file.read()
    return simple_storage_file

def write_sol(file_name, content):
    with open(file_name, "w") as file:
        json.dump(content, file)

def deploy_sol(compiled_sol):

    # Establish connection to ganache
    bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]
    abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]
    w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/2b86ba319eda4e03bb6a69666c58f43a"))
    chain_id = 4
    my_address = "0x6B6EF040124bA0e0dFf4Ee24E19c6B4cc0358213"
    private_key = os.getenv("PRIVATE_KEY")

    # Create the contract in Python
    print("Building contracts")
    SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

    # Get the latest transaction
    print("Getting the latest transcations")
    nonce = w3.eth.getTransactionCount(my_address)

    # 1. Build a transaction
    # 2. Sign a transaction
    # 3. Send a transcation

    print("Building a transcation")
    transaction = SimpleStorage.constructor().buildTransaction(
        {   "chainId": chain_id, 
            "gasPrice": w3.eth.gas_price,
            "from": my_address, 
            "nonce": nonce}
    )

    print("Sign our transaction")
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

    # Send this signed transaction
    print("Send our transaction")
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    print("Wait for a reciept transaction")
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    # Working with the contract, you need the:
    # Contract abi
    # Contract Address

    simple_storage = w3.eth.contract(address=tx_receipt.contractAddress,
                                     abi=abi)

    # Call -> Simulate making the call and getting a return value
    # Transact -> Actually make a state change

    # Initial value of favorite number
    print(simple_storage.functions.retrieve().call())
    
    print("Build a new transaction for store call")
    store_transcation = simple_storage.functions.store(15).buildTransaction({
        "chainId": chain_id, 
        "gasPrice": w3.eth.gas_price,
        "from": my_address, 
        "nonce": nonce + 1
    })

    print("sign store call")
    signed_store_txn = w3.eth.account.sign_transaction(
        store_transcation, private_key=private_key
    )

    print("send store call")
    send_store_tx = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
    print("wait for receipt on store call")
    tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_tx)
    print(simple_storage.functions.retrieve().call())
        

def main():
    simple_storage_file = read_file("./SimpleStorage.sol")
    compile_sol = compile_standard({
        "language": "Solidity",
        "sources": {
            "SimpleStorage.sol": {
                "content": simple_storage_file
                }
            },
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                }
            }
        }
    },
    solc_version = "0.6.0"
    )

    write_sol("compiled_code.json", compile_sol)
    deploy_sol(compile_sol)

if __name__ == "__main__":
    main()