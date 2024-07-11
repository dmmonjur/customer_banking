# Customer Banking System

## Overview

The Customer Banking System allows users to calculate and track interest earned on savings and CD (Certificate of Deposit) accounts. Users can enter their account information, see the interest earned, and view the updated balances after a specified number of months.

## Files

- `Accounts.py`: Contains the `Account` class which defines methods to set the balance and interest for an account.
- `savings_account.py`: Contains the function to create a savings account, calculate interest earned, and update the balance.
- `cd_account.py`: Contains the function to create a CD account, calculate interest earned, and update the balance.
- `customer_banking.py`: Contains the main function that prompts the user for account details, calculates the interest, updates balances, and displays the results.

## Setup Instructions

### Prerequisites

- Python 3.x
- Git

### Steps

1. Clone the repository to your local machine:

    ```sh
    git clone https://github.com/yourusername/customer_banking.git
    cd customer_banking
    ```

2. Ensure Python 3.x is installed on your machine. You can check the version using:

    ```sh
    python --version
    ```

## Usage

1. Navigate to the project directory.

2. Run the main program:

    ```sh
    python customer_banking.py
    ```

3. Follow the prompts to enter the savings and CD account details:

    - Enter the savings account balance.
    - Enter the annual interest rate (APR) for the savings account.
    - Enter the number of months for the savings account.
    - Enter the CD account balance.
    - Enter the annual interest rate (APR) for the CD account.
    - Enter the number of months for the CD account.

4. The program will display the interest earned and the updated balance for both the savings and CD accounts.

## Example

```sh
Enter the savings account balance: 1000
Enter the annual interest rate (APR) for savings account: 3.5
Enter the number of months for savings account: 12
Savings Account: Interest Earned: $35.00, Updated Balance: $1035.00

Enter the CD account balance: 2000
Enter the annual interest rate (APR) for CD account: 5.0
Enter the number of months for CD account: 24
CD Account: Interest Earned: $200.00, Updated Balance: $2200.00

