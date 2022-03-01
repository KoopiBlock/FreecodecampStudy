from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
from brownie import network, accounts, exceptions
import pytest


def test_can_fund_and_withdraw():  # test function
    account = get_account()  # acoount variable
    fund_me = deploy_fund_me()  # varibale for deploying fund_me
    entrance_fee = fund_me.getEntranceFee()
    # a variable for the entrance fee(deploying fund_me with entrance fee)
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    # transaction variable to fund with the value of the entrance fee
    tx.wait(1)  # wait till it hashes 1 block
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    # chek if it funds the account with the entrance fee
    tx2 = fund_me.withdraw({"from": account})  # transaction variable for withdrawing
    tx2.wait  # wait till it hashes 1 block
    assert fund_me.addressToAmountFunded(account.address) == 0
    # check if it empties the account upon withdraw


def test_only_owner_can_withdraw():
    # if we are using  a local/development network we skip this test
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()

    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
