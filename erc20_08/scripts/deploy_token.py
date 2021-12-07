import time
from brownie import OurToken, network, config
from scripts.helpful_scripts import get_account, get_contract, fund_with_link
from web3 import Web3

INITIAL_SUPPLY = Web3.toWei(1000, "ether")


def deploy_token():
    account = get_account()
    token = OurToken.deploy(
        INITIAL_SUPPLY,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print(f"Deployed Token: {token.name()}")
    return token


def main():
    deploy_token()
