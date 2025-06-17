class Account:
    def __init__(self, number, owner, balance):
        self.number = number
        self.owner = owner
        self.__balance = 0 
        self.set_balance(balance) 
        
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        if balance < 0:
            print("The balance can't be under 0")
            self.__balance = 0
        else: 
            self.__balance = balance