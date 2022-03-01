from brownie import FundMe
from scripts.helpful_scripts import get_account

# this is a fund function
def fund():
    fund_me = FundMe[-1]  # use the latest contract
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()  # minimum entrance fee
    print(entrance_fee)
    print(f"The Current entry fee is {entrance_fee}")
    print("funding")
    fund_me.fund({"from": account, "value": entrance_fee})  # fund with the entance fee


def withdraw():  # withdraw from account
    fund_me = FundMe[-1]
    account = get_account()
    print("withdrawing")
    fund_me.withdraw({"from": account})


def main():  # main function wich activates all the privius functions!
    fund()
    withdraw()
