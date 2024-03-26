import datetime

class Transaction:
    def __init__(self, name, description, amount, type, date):
        self.name = name
        self.description = description
        self.amount = amount
        self.type = type
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d")

    def getName(self):
        return self.name
    
    def getDescription(self):  
        return self.description
    
    def getAmount(self):    
        return self.amount
    
    def getType(self):    
        return self.type
    
    def getDate(self):    
        return self.date