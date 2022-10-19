class User:
    def __init__(self, firstname):
        self.firstName=firstname
        self.account_balance=0

    def make_deposit(self,amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
    
    def display_balance(self):
        print(f"User {self.firstName}",f"Balance {self.account_balance}" )
    
    def transfert(self,userOne,amount):
        self.account_balance -=amount
        userOne.account_balance += amount
        self.display_balance()
        userOne.display_balance()
        return self     

Vladimir = User('Vladimir')
Isak = User('Isak')
Flaka = User('Flaka')

Vladimir.make_deposit(300).make_deposit(200).make_deposit(500).make_withdrawal(300).transfert(Isak,300).display_balance()
Flaka.make_withdrawal(100).display_balance()
Isak.transfert(Vladimir,300)

