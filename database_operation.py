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
        )
        """
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
