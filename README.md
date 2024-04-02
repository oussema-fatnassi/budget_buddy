#budget_buddy
Repository of budget buddy project

This is a personal financial management application (Budget Buddy).

Project by: - Oussema FATNASSI, 
            - Baptiste APPRIOU
            - Ali ABAKAR ISSA

Requirements for the app:
Installation of - pygame
                - pygame_gui, 
                - matplotlib
                - mySQL
                - mysql-connector

You will find the code source in the root and images and fonts in the other two folders. 
To launche the app, user "home_page.py"

This personal financial management application has been designed to help users keep track of their accounts efficiently and securely. 

APPLICATION OVERVIEW
**Create an account** if you are a new user by clickin on the REGISTER button. Otherwise login with your credentials (email and password)
For the registration you will need the followinf informations:  - First Name
                                                                - Last Name
                                                                - Email
                                                                - Password
For your security your password must follow this criterias: 
- Must be at least 10 characters long
- Contain at least one uppercase letter
- Contain at least one lowercase letter
- Contain at least one digit
- Contain at least one special character
  
                                                            
After your login you will be redirected to your main page where you can have an overview of your account:
- Can add transactions (Each transaction is defined by name, description, amount and type (expense or income)
- See the list of all the transactions
- Filter transactions: - Sort by date
                       - Sort by category
                       - Sort by type (income, expense)
                       - Sort by ascending and descending amount
                       - Sort transactions arried out between two dates
- Have a monthly transaction recap - select the month and year to have the list of transactions and total Incomes and Expenses
- Alerts and notifications for important information such as overdrafts
- Graphs for a clear view of your transactions by selecting the period and type of graph

All the users data and transactions are securely stored in a database
