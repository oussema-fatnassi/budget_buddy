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

    def getEmail(self):                                                                 # getEmail method to get the email of the user
        return self.email
    
    def getPassword(self):                                                              # getPassword method to get the password of the user
        return self.password
    
    def getFirstName(self):                                                             # getFirstName method to get the first name of the user
        return self.firstName
    
    def getLastName(self):                                                              # getLastName method to get the last name of the user
        return self.lastName
    
    def getId(self):                                                                    # getId method to get the id of the user                    
        return self.id
    
    def setEmail(self, email):                                                          # setEmail method to set the email of the user
        self.email = email
        
    def setPassword(self, password):                                                    # setPassword method to set the password of the user
        self.password = password
        
    def setFirstName(self, firstName):                                                  # setFirstName method to set the first name of the user
        self.firstName = firstName
        
    def setLastName(self, lastName):                                                    # setLastName method to set the last name of the user
        self.lastName = lastName

    def setId(self, id):                                                                # setId method to set the id of the user
        self.id = id

    def login(self, email, password):                                                 # login method to log in the user                    
            if email == self.email and self.password == self.hashPassword(password):
                print("Logged in successfully.")
            else:
                print("Login failed. Invalid email or password.")

    def register(self, firstName, lastName, email, password, confirmed_password):       # register method to register the user
        if email == "" or password == "" or firstName == "" or lastName == "" or confirmed_password == "":
            print("All fields are required.")
            pygame_gui.windows.UIMessageWindow(
                rect=pygame.Rect((50, 100), (300, 100)),
                html_message="All fields are required."
                )
            return
        elif self.checkPassword(password) == False:                                     # check if the password meets the criteria
            passwordText = "Password must be:\n- At least 10 characters long\n- Contain at least one uppercase letter\n- Contain at least one lowercase letter\n- Contain at least one digit\n- Contain at least one special character"
            pygame_gui.windows.UIMessageWindow(
                rect=pygame.Rect((25, 50), (350, 350)),
                html_message=passwordText,
                window_title='Password Criteria',
                object_id="message_box"
            )
            return False
        elif self.checkPassword(password) == True:                                      # if the password meets the criteria check if the passwords match
            if password == confirmed_password:
                self.email = email
                self.password = self.hashPassword(password)                             # hash the password before storing it
                self.firstName = firstName
                self.lastName = lastName
                return True
            elif password != confirmed_password:
                return False
            
    def logout(self):                                                                   # logout method to log out the user      
        self.email = ""
        self.password = ""
        self.firstName = ""
        self.lastName = ""
        print("Logged out.")

    def checkPassword(self, password):                                                  # checkPassword method to validate the password     
        if len(password) < 10:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[a-z]', password):
            return False
        if not re.search(r'[^A-Za-z0-9]', password):
            return False
        if not re.search(r'\d', password):
            return False
        return True
    
    def hashPassword(self, password):                                                   # hashPassword method to hash the password
        hasher = hashlib.sha256()
        hasher.update(password.encode('utf-8'))
        hashedPassword = hasher.hexdigest()
        return hashedPassword

if __name__ == "__main__":                                                              # Main block to test the User class     
    user = User()
