import mysql.connector

def create_user_table():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="O*9GU9A9",
            database="budget_buddy"
        )

        cursor = connection.cursor()

        # Define the SQL query to create the users table if it doesn't exist
        sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )ENGINE=InnoDB;
        """
        print(sql)
        # Execute the query to create the table
        cursor.execute(sql)

        print("Users table created successfully.")

    except mysql.connector.Error as error:
        print("Error creating users table in MySQL:", error)

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