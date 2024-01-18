from atm import *

atm = ATM()
user = User('1', '123456')
user.createAccount('checking')
atm.addUser(user)

card = user.getCard()
access_user = atm.inputCard(card)

account = access_user.selectAccount('checking')
account.seeBalance()

account.deposit(500)
account.seeBalance()

account.withdraw(200)
account.seeBalance()