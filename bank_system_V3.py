import json
with open("bank_base.json","r") as file:
    bank_base = json.load(file)

class Bank:
    current_user = None
    accounts = []
    def __init__(self,data):
        self.data = data

        for number in data:
            Bank.accounts.append(number)
    def login(self):
        while True:
            ask_id = input("Please enter your ID: ")
            if ask_id in self.data:
                ask_password = (input("Please enter your password: "))
                if ask_password == self.data[ask_id]["password"]:
                    self.current_user = bank_base[ask_id]
                    print(f"you have logged in, mester:{self.data[ask_id]["name"]}")
                    del self.data[ask_id]
                    print(self.data)
                    UI(data_from_json).menu()

                else:
                    print("wrong id please try again")
    def sign_in(self):
        pass
        name_interring = input("Please enter your name: ")
        age_interring = input("Please enter your age: ")
        sex_interring = input("please enter your gender(M/f)")
        mobile_interring = input("please enter your mobile number:")
        account_creation = int(max(Bank.accounts)) + 1

        while True:
            pass_word = int(input(
                f"Hello mister:{name_interring} your account number is :{account_creation}\nplease make your password:"))
            re_inter_pass = int(input("please re enter your password: "))
            if pass_word == re_inter_pass:

                user = {
                    "name": name_interring,
                    "age": age_interring,
                    "sex": sex_interring,
                    "mobile": mobile_interring,
                    "balance": 0
                }

                self.data[account_creation] = user
                UI(data_from_json).menu()
            else:
                print("your first password but be the same as the second, please try again")




    def deposit(self):
        try:
           ask_deposit = int(input("Please enter your deposit: "))
           self.current_user["balance"] += float(ask_deposit)
           print(f"your total balance is {self.current_user['balance']}")
        except ValueError:
             print("wrong deposit please try again")

        UI(data_from_json).menu()
    def check_details(self):
        print(f"your details\n{self.current_user}:")


    def withdraw(self):
        while True:
         try:
            ask_withdraw = int(input("Please enter your withdrawal: "))
            if ask_withdraw > self.current_user["balance"]:
                print("you have not enough money")
            else:
                self.current_user["balance"] -= ask_withdraw
                print(f"your total balance is {self.current_user['balance']}")
         except ValueError:
                print("wrong withdraw please try again")

         UI(data_from_json).menu()


class UI:
    def __init__(self,bank):
           self.bank = bank
    def menu(self):
      if self.bank.current_user is not None:
         while True:
          menu_choice = int(input("what would you like to next:\n  #1 deposit\n #2 withdraw\n #3 check details\n #4 exit "))
          if menu_choice == 1:
           self.bank.deposit()
          elif menu_choice == 2:
           self.bank.withdraw()
          elif menu_choice == 3:
            self.bank.check_details()
          elif menu_choice == 4:
              print("Thank you for using bank_system_V3")
              break

      else:
         while True:
            account_having = input("do you have an account? (y/n): ")
            if account_having == "y":
               self.bank.login()
            elif account_having == "n":
               self.bank.sign_in()
            else:
                print("invalid input, please try again")








data_from_json = Bank(bank_base)
UI(data_from_json).menu()
#print(Bank.accounts)
# with open("bank_base.json","w") as file:
#     json.dump(,file)