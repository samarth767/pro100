class Atm(object):
    def __init__(self,card,pin):
        self.card=card
        self.pin=pin

    def balance(self):
        print('your balance is 50,000')
    def withdraw(self,amount):
        new=50000-amount
        print('your balance is'+str(new))

def main():
    card=input('enter card number')
    pin=input('enter pin number')
    user=Atm(card,pin)
    print('choose 1-balance 2-withdraw')
    activity=int(input('enter activity number'))
    if(activity==1):
        user.balance()
    elif(activity==2):
        amount=int(input('enter amount'))
        user.withdraw(amount)
    else:
        print('enter valid number')

main()