class Card():
    def __init__(self, id):
        self.id = id

class ATM():
    def __init__(self):
        self.users = {} # maps user ids to user

    def inputCard(self, card):
        if card.id in self.users:
            pin = input("input pin: ")
            if self.checkPIN(self.users[card.id], pin):
                return self.users[card.id]
            else:
                raise Exception("invalid pin")
        else:
            raise Exception("invalid card")
    
    def checkPIN(self, user, pin):
        if user.pin == pin:
            return True
        return False

class User():
    def __init__(self, id, pin):
        self.id = id
        self.pin = pin
        self.accounts = {} # maps account type to account
    
    def createAccount(self, type):
        self.accounts[type] = Account(type, 0)

    def selectAccount(self, type):
        return self.accounts[type]

class Account():
    def __init__(self, type, balance):
        self.type = type
        self.balance = balance
    
    def seeBalance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            raise Exception("insufficient balance")
        else:
            self.balance -= amount
