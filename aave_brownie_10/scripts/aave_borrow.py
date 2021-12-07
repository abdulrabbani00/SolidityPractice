from brownie import network, config
from scripts.helpful_scripts import get_account
from scripts.get_weth import get_weth


def main():
    account = get_account()
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    if network.show_active() in ["mainnet-fork"]:
        get_weth()

    lending_pool - get_lending_pool()


def get_lending_pool():
    # ABI
    # Address