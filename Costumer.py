class Costumer:
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone 
        
    def get_name(self):
        return self.__name
        
    def set_name(self, name):
        self.__name = name

    def get_phone(self): 
        return self.__phone
        
    def __str__(self):
        return f"Costumer: {self.__name}, Phone: {self.__phone}"