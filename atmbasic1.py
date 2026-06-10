class Atm():
    counter=1
    # static/class variable
    def __init__(self):
        self.__atmpin=""
        self.__balance=0
        # instance variable
        print(id(self))
        self.sno=Atm.counter
        Atm.counter+=1

        # self._sno
    def get_pin(self):
        return self.__atmpin
    def set_pin(self,new_pin):
        if type(new_pin)==str:
           self.__atmpin=new_pin
        else:
            print("invalid pin")
    def __menu(self):
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
                self.__menu()
        else:
            print("invalid choice")
            self.__menu()

    def create_pin(self):
        pinnum=input("enter pin :")
        self.__atmpin=pinnum
        print("pin create succesfully")
        self.__menu()
    def deposit(self):
        temp=input("enter the pin :")
        if temp==self.__atmpin:
           amount=int(input("enter amount you want to deposit"))
           self.__balance+=amount
           print(f"amount deposited .{self.__balance}")
           self.__menu()
        else:
            print("wrong pin")
            self.__menu()
    def check_balance(self):
        temp=input("enter the pin :")
        if temp==self.__atmpin:
           print(f"your balance is {self.__balance}")
        else:
            print("wrong pin")
            self.__menu()
    def withdraw(self):
        temp=input("enter the pin :")
        if temp==self.__atmpin:
            amount=int(input("enter amount you want to withdraw"))
            if amount<=self.__balance:
                self.__balance-=amount
                print(f"your balance is {self.__balance}")
                self.__menu()
            else:
                print("insufficient balance")
                self.__menu()
        else:
            print("wrong pin")
            self.__menu()
    def exit(self):
        print("thank you")

# sbi=Atm()
# here sbi is reference variable , it has the address of the object being made using atm()
# l[:] to clone list , ids will change .
# objects are mutable in a class , and object can be used in loop to

c1=Atm()
c2=Atm()
c3=Atm()
c1.sno
c2.sno
c3.sno