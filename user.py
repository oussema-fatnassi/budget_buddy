import re
import pygame
import hashlib
import pygame_gui
from GUI import GUI

class User:
    def __init__(self):                                                                 # Constructor to initialize the User object
        self.email = ""
        self.password = ""
        self.firstName = ""
        self.lastName = ""
        self.id = 0

    def getEmail(self):
        return self.email
    
    def getPassword(self):
        return self.password
    
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
    
    def getId(self):
        return self.id
    
    def setEmail(self, email):
        self.email = email
        
    def setPassword(self, password):
        self.password = password
        
    def setFirstName(self, firstName):
        self.firstName = firstName
        
    def setLastName(self, lastName):
        self.lastName = lastName

    def setId(self, id):
        self.id = id

    def login(self, email, password):                                                   # login method to log in the user                    
            if email == self.email and self.password == self.hashPassword(password):
                print("Logged in successfully.")
            else:
                print("Login failed. Invalid email or password.")

    def register(self, firstName, lastName, email, password, confirmed_password):                           # register method to register the user
        if email == "" or password == "" or firstName == "" or lastName == "" or confirmed_password == "":
            print("All fields are required.")
            pygame_gui.windows.UIMessageWindow(
                rect=pygame.Rect((50, 100), (300, 100)),
                html_message="All fields are required.",
                )
            return
        elif self.checkPassword(password) == False:
            passwordText = "Password must be:\n- At least 10 characters long\n- Contain at least one uppercase letter\n- Contain at least one lowercase letter\n- Contain at least one digit\n- Contain at least one special character"
            pygame_gui.windows.UIMessageWindow(
                rect=pygame.Rect((25, 50), (350, 350)),
                html_message=passwordText,
                window_title='Password Criteria',
                object_id="message_box"
            )
            return False
        elif self.checkPassword(password) == True:
            if password == confirmed_password:
                self.email = email
                self.password = self.hashPassword(password)                                     # hash the password before storing it
                self.firstName = firstName
                self.lastName = lastName
                print("Registration successful.")
                print("Email:", self.email, "Password:", self.password, "First Name:", self.firstName, "Last Name:", self.lastName)
                return True
            elif password != confirmed_password:
                print("Passwords do not match.")
                return False

            
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
