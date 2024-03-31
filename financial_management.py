from transaction import Transaction
import datetime

class FinancialManagement:
    def __init__(self, user):
        self.transactions = []
        self.LoggedInUser = user

    def addTransaction(self, transaction):                 # Add a transaction
        self.transactions.append(transaction)

    def getTransactions(self):                             # Return all transactions
        return [transaction.name for transaction in self.transactions]
    
    def searchByCategory(self,Category):                    # Return only transactions matching the category
        # self.transactions.sort(key=lambda transaction: transaction.category)   Sort the list of transactions by category in ascending order
        return [transaction.name for transaction in self.transactions if transaction.category == Category]
    
    def searchByDate(self,date):                            # Return only transactions matching the date
        # self.transactions.sort(key=lambda transaction: transaction.date)      Sort the list of transactions by date in ascending order
        return [transaction.name for transaction in self.transactions if transaction.date == date]
    
    def searchByType(self,type):                            # Return only transactions matching the type (Income or Expense)
        # self.transactions.sort(key=lambda transaction: transaction.type)      Sort the list of transactions by type in ascending order
        return [transaction.name for transaction in self.transactions if transaction.type == type]
        
    def sortByAmountAscending(self):                        # Sort transactions by amount in ascending order
        self.transactions.sort(key=lambda transaction: transaction.amount)
        
    def sortByAmountDescending(self):                       # Sort transactions by amount in descending order
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
    
# TESTINGS
# Transaction1 = Transaction("salary", "monthly salary", 5000, "income", "Income", "2024-03-22")
# Transaction2 = Transaction("rent", "monthly rent", 1000, "expense", "Expense", "2024-03-25")
# Transaction3 = Transaction("loto", "lottery won", 2000, "games", "Income", "2024-03-28")
# Transaction4 = Transaction("groceries", "monthly groceries", 500, "food", "Expense", "2024-03-30")
# Transaction5 = Transaction("league", "new league skin", 200, "games", "Expense", "2024-03-31")

# Bank = FinancialManagement("Baptiste")
# Bank.addTransaction(Transaction1)
# Bank.addTransaction(Transaction2)
# Bank.addTransaction(Transaction3)
# Bank.addTransaction(Transaction4)
# Bank.addTransaction(Transaction5)
# print("Bank balance : ",Bank.getBalance())
# print(Bank.getTransactions())
# print(Bank.searchByCategory("games"))
# print(Bank.getTransactions())
# Bank.sortByAmountAscending()
# print(Bank.getTransactions())
# Bank.sortByAmountDescending()
# print(Bank.getTransactions())
# print(Bank.getMonthlySummary(3,2024))