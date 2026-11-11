bank_base = {
   1000600022: {
    "name": "yousif",
    "address" :"lew gate_street",
    "mobile"   :814678687,
    "password" :559575,
    "balance" :1000000
},

}
#__________________________________________________________________________________________
#_____________________________________________________________________________________________________________________________________
def options_list(account):
    print("what do you want to do today sir?")
    while True:
        print("1.check balance")
        print("2.withdraw")
        print("3.deposit")
        print("4.exit")
        option_2 = int(input())
        if option_2 == 1:

            print(f" sir your balance is :{bank_base[account]["balance"]}\n ,any thing else sir?")
        elif option_2 == 2:
                while True:
                    withdraw_number = int(input("how much do you want to withdraw?"))
                    if withdraw_number <= bank_base[account]["balance"]:
                        print(" successful operation")
                        bank_base[account]["balance"] = bank_base[account]["balance"] - withdraw_number
                        print(f" sir your  remain balance is :{bank_base[account]["balance"]}")
                        break
                    else:
                        print(
                            f"failed operation,sorry you dont have enough money\n your balance is {bank_base[account]["balance"]} try another amount of money")
        elif option_2 == 3:
                deposit_amount = int(input("how much do you want to deposit?"))
                bank_base[account]["balance"] = bank_base[account]["balance"] + deposit_amount

                print(f"successful operation, your balance  now is {bank_base[account]["balance"]}\n any thing else for today sir?")
        elif option_2 == 4:
            print("goodbye")
            inter_face()
        else:
            print("sorry Invalid input...please try again")


#___________________________________________________________________________________________________//
def login():
        while True:
           try:
             account_check = int(input("Hello sir, enter your account number please: "))
             if account_check in bank_base:
                 tries = 3
                 while tries > 0:

                   password_check = int(input("Please enter your password: "))
                   if password_check == bank_base[account_check]["password"]:
                         print(f"Hello mister {bank_base[account_check]['name']} welcome back")
                         options_list(account_check)
                         break
                   else:
                         tries -= 1

                         if tries == 0:
                             print("Sorry you tried a lot... please try again later")
                             inter_face()
                         else:
                             print(f"Wrong password. You only have {tries} tries left")
           except Exception as e:
            print("sorry an error occurred",e)
            print("please try a valid account")











def creation ():
    print("hello sir in our bank,we are glade you chose our bank\nplease iter your ditals>>")
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    mobile = int(input("Enter your mobile: "))
    new_account = max(bank_base) + 1
    print(f"well done your account number is :{new_account} please dont share it with any one!!!\nnow set your password")
    while True:
     new_password = int(input("Enter your password: "))
     password1_check = int(input("re inter your password: : "))
     if password1_check == new_password:
         print("done...please check below your infos...and if anything not correct please let us know")
         bank_base[new_account] = {
             "name": name,
             "address": address,
             "mobile": mobile,
             "password":new_password,
             "balance": 0,
         }
         print(f"{bank_base[new_account]}\n the program will restart now!!")
         inter_face()
     else:
         print("wrong try again")



    #________________inter_face__________________________
def inter_face():
    while True:
     print("Hello and welcome to loq bank\n how can i help you sir")
     print("press{1} : if you already have an account\npress{2} to create account")
     option_1 = int(input())
     if option_1 == 1:
        login()
     elif option_1 == 2:
        creation()
     else:
         print("please enter a valid option")
print(inter_face())