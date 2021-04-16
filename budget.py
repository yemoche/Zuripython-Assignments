import math
import datetime


newDate = datetime.datetime.now()
print('ctime:', newDate.ctime())


class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = list()
    self.balance = 0

  def __str__(self):
    statement = ""
    descripWidth = 23
    amountWidth = 7
    statement += self.name.center(descripWidth+amountWidth, "*") + "\n"
    for transaction in self.ledger:
      statement += transaction["description"][:descripWidth].ljust(descripWidth, " ") + "{:.2f}".format(transaction["amount"]).rjust(amountWidth, " ") + "\n"
    statement += "Total: {:.2f}".format(self.balance)
    return statement

  def deposit(self, amount, description=""):
    self.balance += amount
    self.ledger.append({
      "amount": amount,
      "description": description
    })

  def withdraw(self, amount, description=""):
    if self.balance-amount < 0:
      return False
    else:
      self.balance -= amount
      self.ledger.append({
      "amount": -amount,
      "description": description
    })
    return True

  def get_balance(self):
    return self.balance

  def transfer(self, amount, category):
    if self.balance-amount < 0:
      return False
    else:
      self.withdraw(amount, "Transfer to {}".format(category.name))
      category.deposit(amount, "Transfer from {}".format(self.name))
      return True

  def check_funds(self, amount):
    if self.balance < amount:
      return False
    return True   