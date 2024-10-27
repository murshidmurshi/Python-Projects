class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposite(self, dep_amt):
        self.balance += dep_amt
        print(f'You succussfully deposite {dep_amt}')

    def withdraw(self,w_amt):
        if self.balance>=w_amt:
            self.balance-=w_amt
            print(f'{w_amt} Amount succussfully withdraw')
        else:
            print('not enough money')

    def __str__(self):
        return ("Owner:{} \nBalance:{}".format(self.owner, self.balance))

A=Account('Murshid',1000)

print(A)
print(A.deposite(1000))
print(A.withdraw(5000))
