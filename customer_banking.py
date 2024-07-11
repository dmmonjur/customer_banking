# customer_banking.py

from savings_account import create_savings_account
from cd_account import create_cd_account

def main():
    """This function prompts the user to enter the savings and CD account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user for savings account details
    savings_balance = float(input("Enter the savings account balance: "))
    savings_interest = float(input("Enter the annual interest rate (APR) for savings account: "))
    savings_maturity = int(input("Enter the number of months for savings account: "))

    # Calculate and display the savings account interest and updated balance
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    print(f"Savings Account: Interest Earned: ${savings_interest_earned:.2f}, Updated Balance: ${updated_savings_balance:.2f}")

    # Prompt the user for CD account details
    cd_balance = float(input("Enter the CD account balance: "))
    cd_interest = float(input("Enter the annual interest rate (APR) for CD account: "))
    cd_maturity = int(input("Enter the number of months for CD account: "))

    # Calculate and display the CD account interest and updated balance
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
    print(f"CD Account: Interest Earned: ${cd_interest_earned:.2f}, Updated Balance: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    main()
