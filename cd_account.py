# cd_account.py

from Accounts import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance."""
    cd_account = Account(balance)
    interest_earned = balance * (interest_rate / 100 * months / 12)
    updated_balance = balance + interest_earned
    cd_account.set_balance(updated_balance)
    cd_account.set_interest(interest_earned)
    return updated_balance, interest_earned
