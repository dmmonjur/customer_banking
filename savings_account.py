# savings_account.py

from Accounts import Account

def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance."""
    savings_account = Account(balance)
    interest_earned = balance * (interest_rate / 100 * months / 12)
    updated_balance = balance + interest_earned
    savings_account.set_balance(updated_balance)
    savings_account.set_interest(interest_earned)
    return updated_balance, interest_earned
