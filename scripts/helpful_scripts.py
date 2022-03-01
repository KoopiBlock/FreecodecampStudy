from multiprocessing.connection import wait
from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    # if its a dev network or the ganache local ULI then use pre set account, if not use our rinkeby wallet
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    # the deploy mock function!
    print(f"the active network is: {network.show_active()}")
    print("deploying Mocks....")
    if (
        len(MockV3Aggregator) <= 0
    ):  # if the legth of the mockV3aggregator is above 0 deploy it!
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Mocks are now Deployed")
