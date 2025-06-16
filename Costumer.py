class Costumer:
        def __init__(self, n, phone):
                self.__name = n
                self._number = phone
        
        #get method
        def get_name(self):
                return self.__name
        
        #set method
        def set_name(self, name):
                self.name = name

