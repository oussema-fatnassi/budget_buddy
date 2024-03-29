import mysql.connector
from mysql.connector import errorcode

# Connection to the MySQL database
try:
    cnx = mysql.connector.connect(user='root', password='Aliabakar', # use your mysql username,password,localhost and database name.
                                  host='127.0.0.1',
                                  database='data_app')
    cursor = cnx.cursor()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Authentication error: Please check your username and password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Specified database does not exist")
    else:
        print(err)

# Creation of tables
TABLES = {}
TABLES['users'] = (
    "CREATE TABLE IF NOT EXISTS `users` ("
    "`id` INT AUTO_INCREMENT PRIMARY KEY,"
    "`nom` VARCHAR(50) NOT NULL,"
    "`prenom` VARCHAR(50) NOT NULL,"
    "`email` VARCHAR(100) NOT NULL,"
    "`mot_de_passe` VARCHAR(255) NOT NULL"
    ") ENGINE=InnoDB")

TABLES['transactions'] = (
    "CREATE TABLE IF NOT EXISTS `transactions` ("
    "`id` INT AUTO_INCREMENT PRIMARY KEY,"
    "`user_id` INT NOT NULL,"
    "`nom` VARCHAR(100) NOT NULL,"
    "`description` TEXT,"
    "`montant` DECIMAL(10,2) NOT NULL,"
    "`type` ENUM('depense', 'revenu') NOT NULL,"
    "`date` DATE NOT NULL,"
    "FOREIGN KEY (`user_id`) REFERENCES `users`(`id`)"
    ") ENGINE=InnoDB")

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
        print("OK")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table already exists")
        else:
            print(err.msg)

# Functions to manage users
def register_user(nom, prenom, email, mot_de_passe):
    try:
        cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        if user:
            print("User already exists")
            return False
        else:
            # Inserting the user into the database
            cursor.execute("INSERT INTO users (nom, prenom, email, mot_de_passe) VALUES (%s, %s, %s, %s)",
                           (nom, prenom, email, mot_de_passe))
            cnx.commit()
            print("User successfully registered")
            return True
    except mysql.connector.Error as err:
        print("Error registering user:", err)
        return False

def login_user(email, mot_de_passe):
    try:
        cursor.execute("SELECT id FROM users WHERE email = %s AND mot_de_passe = %s", (email, mot_de_passe))
        user = cursor.fetchone()
        if user:
            print("Login successful")
            return True
        else:
            print("Incorrect email or password")
            return False
    except mysql.connector.Error as err:
        print("Error logging in user:", err)
        return False

def get_or_register_user():
    nom = input("Enter your name: ")
    prenom = input("Enter your first name: ")
    email = input("Enter your email: ")
    mot_de_passe = input("Enter your password: ")

    if register_user(nom, prenom, email, mot_de_passe):
        return email
    else:
        return email if login_user(email, mot_de_passe) else None

# Functions to manage transactions

def add_transaction(user_id, nom, description, amount, type, date):
    try:
        cursor.execute("INSERT INTO transactions (user_id, nom, description, montant, type, date) "
                       "VALUES (%s, %s, %s, %s, %s, %s)",
                       (user_id, nom, description, amount, type, date))
        cnx.commit()
        print("Transaction added successfully")
    except mysql.connector.Error as err:
        print("Error adding transaction:", err)

def get_transactions(user_id, start_date=None, end_date=None):
    try:
        query = "SELECT * FROM transactions WHERE user_id = %s"
        params = [user_id]
        if start_date and end_date:
            query += " AND date BETWEEN %s AND %s"
            params.extend([start_date, end_date])
        cursor.execute(query, params)
        transactions = cursor.fetchall()
        return transactions
    except mysql.connector.Error as err:
        print("Error retrieving transactions:", err)
        return []

# Example usage
user_email = get_or_register_user()
if user_email:
    add_transaction(1, "vraiment", "salary", 500.00, "gain", "2024-03-29")
    transactions = get_transactions(1)
    for transaction in transactions:
        print(transaction)

def get_user(user_id):
    try:
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user_data = cursor.fetchone()
        '''if user_data:
            print("User Information:")
            print("ID :", user_data[0])
            print("Name :", user_data[1])
            print("First Name :", user_data[2])
            print("Email :", user_data[3])
            # Do not print the password for security reasons
        else:
            print("User not found")'''
    except mysql.connector.Error as err:
        print("Error retrieving user data:", err)

# Example usage
get_user(2)

# Closing the connection
cursor.close()
cnx.close()
