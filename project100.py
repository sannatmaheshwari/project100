class Atm(object):
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def withdrawl(self,amount):
        newAmount = 5000-amount
        print("you remaining balace is = "+str(newAmount))

    def checkBalance(self):
        print("your balance is 5000")

def main():
    cardnumber = input("insert your cardnumber=")
    pin = input("enter you pin = ")
    newuser = Atm(cardnumber,pin)
    print("choose Your activity")
    print("1.balance enquiry 2.withdrawl")
    activity = int(input("enter your activity number = "))
    if activity==1:
        newuser.checkBalance()
    elif activity==2:
        amount = int(input("enter the amount = "))
        newuser.withdrawl(amount)
    else:
        print("enter a valid number")
main()