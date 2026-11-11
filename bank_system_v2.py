import csv
class Account:

    def __init__(self, name, address, account_number, password,balance):
        self.name = name
        self.address = address
        self.account_number = account_number
        self.password = password
        self.balance = balance

class bank:
    def __init__(self):
        self.accounts = {}
    def new_account(self, name, address, account_number, password, balance):
        print("please full in your infos:")
        name = str(input("your name: "))
        address = str(input("your address: "))
        while True:
         password = (input("your password: "))
         re_password = (input("re-enter your password: "))
         try:
             password == re_password

         except Exception as e:
             "please re-enter your password"
         bank.accounts(name, address, account_number, password,balance)




 # @classmethod
 #    def get_accounts_from_the_source(cls):
 #        with open('bank_data_source.csv', newline='') as main_file:
 #           reader = csv.DictReader(main_file)
 #           for row in reader:
 #                cls(
 #                    name = row.get('name'),
 #                    address = row.get('address'),
 #                    account_number =  int(row.get('account_number')),
 #                    password = row.get('password'),
 #                    balance = int(row.get('balance'))