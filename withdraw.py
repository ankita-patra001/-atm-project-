import time
import utils # module for file read/write utils

def withdraw(account):
    """
    Perform a withdraw transaction on the account.

    Update the account balance and write transaction to file.
    """
    
    # Get current values
    current_balance = int(account['balance'])
    print(f"Your current balance is: {current_balance}")

    # Get withdraw amount
    withdraw_amount = int(input("Enter withdraw amount: "))

    # Validate amount
    if withdraw_amount > current_balance:
        print("ERROR: Cannot withdraw more than account balance")
        return

    # Update balance    
    new_balance = current_balance - withdraw_amount
    print(f"New balance is: {new_balance}")

    # Write transaction to file
    transaction = {
        'id': utils.get_next_id('transactions.txt'),
        'type': 'withdraw',
        'date': time.ctime(),
        'amount': withdraw_amount,
        'from': current_balance, 
        'to': new_balance
    }
    utils.append_to_file('transactions.txt', transaction)

    # Update account balance
    account['balance'] = new_balance

    print("Withdraw successful!")

if __name__ == '__main__':
    my_account = {'name': 'John', 'balance': 500}
    withdraw(my_account)
