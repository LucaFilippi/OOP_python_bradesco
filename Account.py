class Account:
    def __init__(self, number, owner, balance):
        self.__balance = 0
        self.owner = owner
        self.number = number

    #get method
    def get_balance(self):
        return self.__balance
    
    #set method
    def set_balance(self, balance):
        if (balance < 0):
            print("The balance can't be under 0")
        else: 
            self.__balance = balance