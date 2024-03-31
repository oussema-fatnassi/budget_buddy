import mysql.connector

def create_tables():
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

def insert_user_data(first_name, last_name, email, password):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="O*9GU9A9",
            database="budget_buddy"
        )

        cursor = connection.cursor()

        # Define the SQL query to insert user data into the database
        sql = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
        # Execute the query with user data
        cursor.execute(sql, (first_name, last_name, email, password))

        # Commit changes to the database
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

        # Define the SQL query to select user data based on email and password
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"
        
        # Execute the query with user data
        cursor.execute(sql, (email, password))
        
        # Fetch the result
        result = cursor.fetchone()

        # Check if result is not empty, indicating successful verification
        if result:
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

def insert_transaction_data(email, transaction):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="O*9GU9A9",
            database="budget_buddy"
        )

        cursor = connection.cursor()

        # Retrieve the user's ID based on their email
        cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
        result = cursor.fetchone()

        if result:  # Check if a user with the given email exists
            user_id = result[0]
            # Define the SQL query to insert transaction data into the database
            sql = "INSERT INTO transaction (user_id, name, description, amount, category, type, date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            # Execute the query with transaction data
            cursor.execute(sql, (user_id, transaction.name, transaction.description, transaction.amount, transaction.category, transaction.type, transaction.date))
            # Commit changes to the database
            connection.commit()
            print("Transaction data inserted successfully.")
        else:
            print("User with email {} not found.".format(email))

    except mysql.connector.Error as error:
        print("Error inserting transaction data into MySQL table:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

