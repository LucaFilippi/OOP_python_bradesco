class Main:
    pass
print ("testing project")

from Costumer import Costumer
from Account import Account

c1 = Costumer("Peter", "555-0878")
account = Account("665", c1.name, 0)

print(c1)
print(f"name is {c1.name} and phone number is {c1.number}")
print(f"{account.owner}, number: {account.number}, current balance: {account.balance}")
