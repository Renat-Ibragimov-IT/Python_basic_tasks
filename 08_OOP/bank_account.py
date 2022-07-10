# 1. Описать класс "Банковский счет", атрибуты у которого:
#    * имя аккаунта - str
#    * уникальный id (uuid)
#    * баланс float
#    * транзакции (список)
#    Методы
#    * депозит средств
#    * вывод средств
#    * получить баланс
#    При изменении баланса записывать в транзакции (сумма, тип операции,
#    текущая_дата)
#    * доп. добавить и учитывать банковские комиссии (1%)
from uuid import uuid4
import datetime


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
print("Your balance is: ", my_bank.check_balance())
