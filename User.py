import re
import pygame
import hashlib

class User:
    def __init__(self):                                                                 # Constructor to initialize the User object
        self.email = ""
        self.password = ""
        self.firstName = ""
        self.lastName = ""

    def getEmail(self):
        return self.email
    
    def getPassword(self):
        return self.password
    
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
    
    def setEmail(self, email):
        self.email = email
        
    def setPassword(self, password):
        self.password = password
        
    def setFirstName(self, firstName):
        self.firstName = firstName
        
    def setLastName(self, lastName):
        self.lastName = lastName

    def login(self, email, password):                                                   # login method to log in the user                    
            if email == self.email and password == self.password:
                print("Logged in successfully.")
            else:
                print("Login failed. Invalid email or password.")

    def register(self, email, password, firstName, lastName):                           # register method to register the user
        if email == "" or password == "" or firstName == "" or lastName == "":
            print("All fields are required.")
            return      
        self.email = email
        self.password = self.hashPassword(password)                                     # hash the password before storing it
        self.firstName = firstName
        self.lastName = lastName
        print("Registration successful.")
        print("Email:", self.email, "Password:", self.password, "First Name:", self.firstName, "Last Name:", self.lastName)

    def logout(self):                                                                   # logout method to log out the user      
        self.email = ""
        self.password = ""
        self.firstName = ""
        self.lastName = ""
        print("Logged out.")

    def checkPassword(self, password):                                                  # checkPassword method to validate the password     
        if len(password) < 10:
            print("Password must be at least 10 characters long.")
            return False
        if not re.search(r'[A-Z]', password):
            print("Password must contain at least one uppercase letter.")
            return False
        if not re.search(r'[a-z]', password):
            print("Password must contain at least one lowercase letter.")
            return False
        if not re.search(r'[^A-Za-z0-9]', password):
            print("Password must contain at least one special character.")
            return False
        if not re.search(r'\d', password):
            print("Password must contain at least one digit.")
            return False
        print("Password meets the criteria.")
        return True
    
    def hashPassword(self, password):                                                   # hashPassword method to hash the password
        hasher = hashlib.sha256()
        hasher.update(password.encode('utf-8'))
        hashedPassword = hasher.hexdigest()
        return hashedPassword

if __name__ == "__main__":                                                              # Main block to test the User class     
    user = User()
    user.register("john@example.com", "example_Passwod1", "John", "Doe")
    user.login("john@example.com", "example_Password1")
    user.checkPassword("example_Password1")
    user.logout()

    hashedPassword = user.hashPassword("example_Password1")
    print("Hashed password:", hashedPassword)