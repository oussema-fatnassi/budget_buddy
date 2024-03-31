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
        return False

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

