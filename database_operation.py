import mysql.connector

def create_tables():                                                                # create_tables method to create the users and transactions tables in the database
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="O*9GU9A9",
            database="budget_buddy"
        )

        cursor = connection.cursor()

        # Define the SQL query to create the users table if it doesn't exist
        create_users_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            INDEX email_index (email)
        )ENGINE=InnoDB;
        """

        cursor.execute(create_users_table_query)

        # Define the SQL query to create the transactions table if it doesn't exist
        create_transactions_table_query = """
        CREATE TABLE IF NOT EXISTS transaction (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            name VARCHAR(255) NOT NULL,
            description VARCHAR(255),
            amount DECIMAL(10, 2) NOT NULL,
            category ENUM ('Groceries', 'Rent', 'Utilities', 'Transportation', 'Healthcare', 'Entertainment', 'Salary', 'Hobbies', 'Travel', 'Restaurants', 'Others') NOT NULL,
            type ENUM('Income', 'Expense') NOT NULL,
            date DATE NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )ENGINE=InnoDB;
        """

        cursor.execute(create_transactions_table_query)

        print("Tables created successfully.")

    except mysql.connector.Error as error:
        print("Error creating tables in MySQL:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

def insert_user_data(first_name, last_name, email, password):                           # insert_user_data method to insert user data into the database       
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="O*9GU9A9",
            database="budget_buddy"
        )

        cursor = connection.cursor()

        sql = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"      # Define the SQL query to insert user data into the database
        cursor.execute(sql, (first_name, last_name, email, password))                                   # Execute the query with user data

        connection.commit()
        print("User data inserted successfully.")

    except mysql.connector.Error as error:
        print("Error inserting user data into MySQL table:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

def verify_user(email, password):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="O*9GU9A9",
            database="budget_buddy"
        )

        cursor = connection.cursor()

        sql = "SELECT * FROM users WHERE email = %s AND password = %s"                                      # Define the SQL query to verify user data       
        
        cursor.execute(sql, (email, password))
        
        result = cursor.fetchone()

        if result:                                                                                          # Check if the user exists and the password is correct            
            print("User verified successfully.")
            return True
        else:
            print("User not found or incorrect credentials.")
            return False

    except mysql.connector.Error as error:
        print("Error verifying user in MySQL:", error)
        return False

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

def get_user_data(email):                                                               # get_user_data method to retrieve user data from the database
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="O*9GU9A9",
            database="budget_buddy"
        )
        cursor = connection.cursor()

        sql = "SELECT * FROM users WHERE email = %s "                                   # SQL query to retrieve user data based on email
        
        cursor.execute(sql, (email,))                                                   # Execute the query with user data             
        
        result = cursor.fetchall()                                                      # Fetch all the results           
        return result[0]

    except mysql.connector.Error as error:
        print("Error getting user in MySQL:", error)
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

def insert_transaction_data(user_id, transaction):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="O*9GU9A9",
            database="budget_buddy"
        )

        cursor = connection.cursor()

        cursor.execute("SELECT id FROM users WHERE id = %s", (user_id,))                        # Define the SQL query to retrieve the user's ID based on their email
        result = cursor.fetchone()
        print(result)
        print(user_id)
        if result:                                                                              # Check if the user exists
            sql = "INSERT INTO transaction (user_id, name, description, amount, category, type, date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (user_id, transaction.name, transaction.description, transaction.amount, transaction.category, transaction.type, transaction.date))
            connection.commit()
            print("Transaction data inserted successfully.")

    except mysql.connector.Error as error:
        print("Error inserting transaction data into MySQL table:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

def get_last_transactions(user_id, limit=5):                                                    # get_last_transactions method to retrieve the last transactions of the user
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="O*9GU9A9",
            database="budget_buddy"
        )
        cursor = connection.cursor()

        sql = "SELECT name FROM transaction WHERE user_id = %s ORDER BY date DESC LIMIT %s"
        cursor.execute(sql, (user_id, limit))

        result = cursor.fetchall()
        return [row[0] for row in result]  # Extracting just the transaction names

    except mysql.connector.Error as error:
        print("Error getting last transactions from MySQL:", error)
        return []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

def get_transaction_details(transaction_name, user_id):                                         # get_transaction_details method to retrieve transaction details from the database
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="O*9GU9A9",
            database="budget_buddy"
        )
        cursor = connection.cursor()

        # Define the SQL query to retrieve details of the transaction using its name and user ID
        sql = "SELECT * FROM transaction WHERE name = %s AND user_id = %s"
        cursor.execute(sql, (transaction_name, user_id))
        
        transaction_details = cursor.fetchone()
        
        # If transaction_details is not None, return it
        if transaction_details:
            details_dict = {
                'name': transaction_details[2],
                'description': transaction_details[3],
                'amount': transaction_details[4],
                'category': transaction_details[5],
                'type': transaction_details[6],
                'date': transaction_details[7]
            }
            return details_dict
        else:
            return None

    except mysql.connector.Error as error:
        print("Error retrieving transaction details:", error)
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

def get_current_amount(user_id):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="O*9GU9A9",
            database="budget_buddy"
        )
        cursor = connection.cursor()

        # Retrieve total income
        cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM transaction WHERE user_id = %s AND type = 'Income'", (user_id,))
        income_result = cursor.fetchone()[0]
        income = income_result if income_result else 0

        # Retrieve total expenses
        cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM transaction WHERE user_id = %s AND type = 'Expense'", (user_id,))
        expenses_result = cursor.fetchone()[0]
        expenses = expenses_result if expenses_result else 0

        return income - expenses

    except mysql.connector.Error as error:
        print("Error getting current amount from MySQL:", error)
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

def get_all_transactions(user_id):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="O*9GU9A9",
            database="budget_buddy"
        )
        cursor = connection.cursor()

        # Define the SQL query to retrieve all transaction names of the user
        sql = "SELECT name FROM transaction WHERE user_id = %s"
        cursor.execute(sql, (user_id,))
        
        # Fetch all the transaction names
        result = cursor.fetchall()

        # Extract transaction names from the result and return them as strings
        transaction_names = [row[0] for row in result if row[0]]
        
        return transaction_names

    except mysql.connector.Error as error:
        print("Error retrieving transactions:", error)
        return []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

def get_transactions_by_date(user_id, selected_date):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="O*9GU9A9",
            database="budget_buddy"
        )
        cursor = connection.cursor()

        # Define the SQL query to retrieve transactions for the selected date
        sql = "SELECT name FROM transaction WHERE user_id = %s AND DATE(date) = %s"
        cursor.execute(sql, (user_id, selected_date))
        
        # Fetch all the transaction names
        result = cursor.fetchall()

        # Extract transaction names from the result and return them as strings
        transaction_names = [row[0] for row in result if row[0]]
        
        return transaction_names

    except mysql.connector.Error as error:
        print("Error retrieving transactions by date:", error)
        return []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

def get_transactions_by_category(user_id, selected_category):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="O*9GU9A9",
            database="budget_buddy"
        )
        cursor = connection.cursor()
        sql = "SELECT name FROM transaction WHERE user_id = %s AND category = %s"
        cursor.execute(sql, (user_id, selected_category))
        result = cursor.fetchall()
        transaction_names = [row[0] for row in result if row[0]]
        return transaction_names

    except mysql.connector.Error as error:
        print("Error retrieving transactions by category:", error)
        return []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

def get_transactions_by_type(user_id, selected_type):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="O*9GU9A9",
            database="budget_buddy"
        )
        cursor = connection.cursor()
        sql = "SELECT name FROM transaction WHERE user_id = %s AND type = %s"
        cursor.execute(sql, (user_id, selected_type))
        result = cursor.fetchall()
        transaction_names = [row[0] for row in result if row[0]]
        return transaction_names

    except mysql.connector.Error as error:
        print("Error retrieving transactions by type:", error)
        return []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

def get_transactions_by_amount_asc(user_id, selected_sort_order):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="O*9GU9A9",
            database="budget_buddy"
        )
        cursor = connection.cursor()
        
        if selected_sort_order.upper() == "ASCENDING":
            sql = "SELECT name FROM transaction WHERE user_id = %s ORDER BY amount ASC"
        elif selected_sort_order.upper() == "DESCENDING":
            sql = "SELECT name FROM transaction WHERE user_id = %s ORDER BY amount DESC"
            
        cursor.execute(sql, (user_id,))
        
        # Fetch all the transaction names
        result = cursor.fetchall()
        
        # Extract transaction names from the result and return them as a list of strings
        transaction_names = [row[0] for row in result if row[0]]
        
        return transaction_names

    except mysql.connector.Error as error:
        print("Error retrieving transactions by amount:", error)
        return []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

def get_transactions_between_dates(user_id, start_date, end_date):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="O*9GU9A9",
            database="budget_buddy"
        )
        cursor = connection.cursor()

        # Define the SQL query to retrieve transactions between two dates
        sql = "SELECT name FROM transaction WHERE user_id = %s AND date BETWEEN %s AND %s"
        cursor.execute(sql, (user_id, start_date, end_date))
        
        # Fetch all the transaction names
        result = cursor.fetchall()

        # Extract transaction names from the result and return them as strings
        transaction_names = [row[0] for row in result if row[0]]
        
        return transaction_names

    except mysql.connector.Error as error:
        print("Error retrieving transactions between dates:", error)
        return []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

def get_monthly_transactions(user_id, selected_month, selected_year):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="O*9GU9A9",
            database="budget_buddy"
        )
        cursor = connection.cursor()

        # Define the SQL query to retrieve transactions for the selected month/year
        sql = "SELECT name, amount, type FROM transaction WHERE user_id = %s AND MONTH(date) = %s AND YEAR(date) = %s"
        cursor.execute(sql, (user_id, int(selected_month), int(selected_year)))
        
        # Fetch all the transactions
        result = cursor.fetchall()

        # Extract transaction names, calculate total income and expenses
        transaction_names = []
        total_income = 0
        total_expenses = 0
        for row in result:
            transaction_names.append(row[0])
            if row[2] == 'Income':
                total_income += row[1]
            else:
                total_expenses += row[1]
        
        return transaction_names, total_income, total_expenses

    except mysql.connector.Error as error:
        print("Error retrieving monthly transactions:", error)
        return [], 0, 0

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

def get_transactions_by_category_period(user_id, selected_month, selected_year):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="O*9GU9A9",
            database="budget_buddy"
        )
        cursor = connection.cursor()
        sql = "SELECT category, SUM(amount) FROM transaction WHERE user_id = %s AND MONTH(date) = %s AND YEAR(date) = %s GROUP BY category"
        cursor.execute(sql, (user_id, selected_month, selected_year))
        result = cursor.fetchall()
        
        categories = []
        amounts = []
        for row in result:
            categories.append(row[0])
            amounts.append(row[1])
                
        return categories, amounts

    except mysql.connector.Error as error:
        print("Error retrieving transactions by category:", error)
        return [], []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")








