# 1. Describe the "Bank account" class, whose attributes are:
# * account name - str
# * unique id (uuid)
# * float balance
# * transactions (list)
# Methods
# * deposit funds
# * withdraw funds
# * get balance
# When changing the balance, write in transactions
# (amount, operation type, current_date)
# * Optional: add and account for bank fees (1%)
import datetime
from uuid import uuid4


class BankAccount:

    def __init__(self, account_name: str, balance: float):
        self.account_name = account_name
        self.unique_id = uuid4()
        self.balance = round(balance, 2)
        self.transaction = []
        self.banking_fees = 0.01

    def deposit_funds(self, deposit: float):
        self.balance += round(deposit - deposit * self.banking_fees, 2)
        self.transaction.append(f'{"Deposit: "}'
                                f'{round(deposit - deposit * self.banking_fees, 2)}{"; "}'
                                f'{"Balance: "}{self.balance}{"; "}'
                                f'{"Date: "}{datetime.datetime.now().strftime("%d %B, %Y %H:%M:%S")}')

    def withdrawal_of_funds(self, withdrawal: float):
        self.balance -= round(withdrawal + withdrawal * self.banking_fees, 2)
        self.transaction.append(f'{"Withdrawal: "}'
                                f'{round(withdrawal + withdrawal * self.banking_fees, 2)}{"; "}'
                                f'{"Balance: "}{self.balance}{"; "}'
                                f'{"Date: "}{datetime.datetime.now().strftime("%d %B, %Y %H:%M:%S")}')

    def check_balance(self):
        return self.balance


my_bank = BankAccount('MyBank', 7589)
my_bank.deposit_funds(253)
my_bank.withdrawal_of_funds(459)
my_bank.deposit_funds(1584)
my_bank.withdrawal_of_funds(129.50)

print("List of Your transactions is: ", *my_bank.transaction, sep="\n")
print(f'Your balance is: {my_bank.check_balance()}')
