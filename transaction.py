import datetime

class Transaction:                              # Class to represent a transaction     
    def __init__(self, name, description, amount, category, type, date):
        self.name = name
        self.description = description
        self.amount = amount
        self.category = category
        self.type = type                        # Income or Expense
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d")

    def getName(self):                          # Get the name of the transaction
        return self.name
    
    def getDescription(self):                   # Get the description of the transaction
        return self.description
    
    def getAmount(self):                        # Get the amount of the transaction
        return self.amount
    
    def getCategory(self):                      # Get the category of the transaction
        return self.category
    
    def getType(self):                          # Get the type of the transaction (Income or Expense)
        return self.type
    
    def getDate(self):                          # Get the date of the transaction
        return self.date