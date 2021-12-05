from brownie import SimpleStorage, accounts, config

def read_latest_contract():
    simple_storage = SimpleStorage[-1]

    print(simple_storage.retrieve())

def main():
    read_latest_contract()