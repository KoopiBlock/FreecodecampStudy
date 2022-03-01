# importing functions and variabales from our FundMe.sol
from brownie import FundMe, MockV3Aggregator, network, config

# importing the get_account function from helpfulscripts.py

from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


# defing a deploying function for Fund_me.sol
def deploy_fund_me():
    account = get_account()
    # pass the price feed address to our fundme contract
    # deploying the fund me and utilising one of the accounts( depend on what type of blockchain we are running)
    # if we are on a pressistent network(lik rinkeby) use the assosiated address
    # otherwise, use deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )  # we have in our config dev nets and active nets verifications if its for dev nets it will show false
    # if its true that it will use the price feed of the chainlink.

    print(f"Contract deployed to {fund_me.address}")
    return fund_me


# the main function of this folder is to deploy fund_me.sol
def main():
    deploy_fund_me()
