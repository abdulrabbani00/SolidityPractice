from brownie import FundMe
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS

def fund():
    fund_me  = FundMe[-1]
    accounts = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": accounts, "value": entrance_fee})
    
def withdraw():
    fund_me  = FundMe[-1]
    accounts = get_account()
    fund_me.withdrawl({"from": accounts})

def main():
    fund()
    withdraw()