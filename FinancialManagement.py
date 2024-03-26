from Transaction import Transaction
import datetime

class FinancialManagement:
    def __init__(self, user):
        self.transactions = []
        self.LoggedInUser = user

    def add_transaction(self, transaction):                 # Add a transaction
        self.transactions.append(transaction)

    def get_transactions(self):                             # Get all transactions
        return self.transactions
    
    def searchByCategory(self):                             # Sort transactions by category
        self.transactions.sort(key=lambda transaction: transaction.category)
    
    def searchByDate(self):                                 # Sort transactions by date
        self.transactions.sort(key=lambda transaction: transaction.date)
    
    def searchByType(self):                                 # Sort transactions by type (Income or Expense)
        self.transactions.sort(key=lambda transaction: transaction.type)
        
    def searchByAmountAscending(self):                      # Sort transactions by amount in ascending order
        self.transactions.sort(key=lambda transaction: transaction.amount)
        
    def searchByAmountDescending(self):                     # Sort transactions by amount in descending order
        self.transactions.sort(key=lambda transaction: transaction.amount, reverse=True)
        
    def sortByBetweenDates(self, startDate, endDate):       # Sort transactions between two dates
        self.transactions = [transaction for transaction in self.transactions if transaction.date >= startDate and transaction.date <= endDate]
        
    def getBalance(self):
        balance = 0
        for transaction in self.transactions:
            if transaction.type == "Income":                # If the transaction is an income, add the amount to the balance
                balance += transaction.amount
            else:                                           # If the transaction is an expense, subtract the amount from the balance
                balance -= transaction.amount
        return balance
    
    def getMonthlyIncome(self, month, year):                # Get the total income for a specific month
        monthlyIncome = 0
        for transaction in self.transactions:
            if transaction.type == "Income" and transaction.date.month == month and transaction.date.year == year:
                monthlyIncome += transaction.amount
        return monthlyIncome
    
    def getMonthlyExpense(self, month, year):               # Get the total expense for a specific month
        monthlyExpense = 0
        for transaction in self.transactions:
            if transaction.type == "Expense" and transaction.date.month == month and transaction.date.year == year:
                monthlyExpense += transaction.amount
        return monthlyExpense
    
    def getMonthlySummary(self, month, year):               # Get the total income and expense for a specific month
        monthlyIncome = self.getMonthlyIncome(month, year)
        monthlyExpense = self.getMonthlyExpense(month, year)
        return monthlyIncome, monthlyExpense
    
    def generateAlerts(self):                               # Generate alerts for transactions with amount greater than 1000
        alerts = []
        for transaction in self.transactions:
            if transaction.amount > 1000:
                alerts.append(transaction)
        return alerts