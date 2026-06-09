class Atm():
    def __init__(self,a=None,b=0):
        self.atmpin=a
        self.balance=b

        self.menu()
    def menu(self):
        user_input = int(input('''
        1. create Pin
        2. Check Balance
        3. Withdraw
        4. deposit
        5. Exit
         : '''))
        if type(user_input)==int:
            if user_input == 1:
                self.create_pin()
            elif user_input == 2:
                self.check_balance()
            elif user_input == 3:
                self.withdraw()
            elif user_input == 4:
                self.deposit()
            elif user_input == 5:
                self.exit()
            else :
                print("choose within 1 to 5")
                self.menu()
        else:
            print("invalid choice")
            self.menu()
    def create_pin(self):
        pinnum=int(input("enter pin :"))
        if len(str(pinnum))<5:
           self.atmpin=pinnum
           print("pin set succesfully , now proceed or u can exit .")
           self.menu()
        else:
            print("pin is not created , pin should be of length within 5 numbers .")
            self.create_pin()
    def check_balance(self):
        if self.atmpin==None:
            print("as you have provided no pin , u have to create a pin firstly")
            self.create_pin()
        
        else:
            yourpin=int(input("enter pin no. :"))
            if type(yourpin)==int:
                if self.atmpin==yourpin:
                    print("your balance is",self.balance)
                else:
                    print("wrong pin")
                    self.menu()
            else:
                print("pin should be numeric ")
                self.check_balance()
    def withdraw(self):
        if self.atmpin==None:
            print("as you have provided no pin , u have to create a pin firstly")
            self.create_pin()
        
        else:
            yourpin=int(input("enter pin no. :"))
            if type(yourpin)==int:
                if self.atmpin==yourpin:
                    amount=int(input("enter amount : "))
                    if amount<=self.balance:
                        self.balance-=amount
                        print("withdrawal successful")
                        print("thanks for transaction .your balance is",self.balance)
                    else:
                        print("insufficient balance , go back to menu ")
                        self.menu()
                else:
                    print("wrong pin , exited the withdrawal .")
                    self.menu()
            else:
                print("pin should be numeric ")
                self.withdraw()
    def deposit(self):
        if self.atmpin==None:
            print("as you have provided no pin , u have to create a pin firstly")
            self.create_pin()
        
        else:
            yourpin=int(input("enter pin no. :"))
            if type(yourpin)==int:
                if self.atmpin==yourpin:
                    amount=int(input("enter amount you want to deposit"))
                    self.balance+=amount
                    print("withdrawal successful")
                    print(f"thanks for transaction .your balance is",{self.balance},)
                   
                else:
                    print("wrong pin")
                    self.menu()
            else:
                print("pin should be numeric ")
                self.deposit()
    def exit(self):
        print("thank you.")
sbi=Atm(b=90000)

    


        



    