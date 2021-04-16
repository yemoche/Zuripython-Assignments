# code referencing MukeshAngrish

import budget

food = budget.Category("food")
food.deposit(5000, "initial deposit")
food.withdraw(300, "groceries")
food.withdraw(40.89, "restaurant and more food for dessert")
clothing = budget.Category("Clothing")
food.transfer(100, clothing)
clothing.withdraw(90.67)
clothing.withdraw(300)
entertainment = budget.Category("Entertainment")
entertainment.deposit(1000, "initial deposit")
entertainment.withdraw(500)

print(food)
print(clothing)
print(entertainment)
