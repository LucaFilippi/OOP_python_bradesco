print("testing project")

from Costumer import Costumer
from Account import Account


c1 = Costumer("", "555-0878")  
c1.set_name("Peter")           

account = Account("665", c1.get_name(), 0)  
account.set_balance(10)  

print(c1)
print(f"name is {c1.get_name()} and phone number is {c1.get_phone()}")
print(f"{account.owner}, number: {account.number}, current balance: {account.get_balance()}")