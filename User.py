import pygame
import re

class User:

    username = ""
    password = ""
    firstName = ""
    lastName = ""
    email = ""

    def login(self, username, password):
        self.username = username
        self.password = password

    def register(self, username, password, firstName, lastName, email):
        self.username = username
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

    def logout(self):
        pass

    def __init__(self, username, password, firstName, lastName, email):
        self.username = username
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

    def check_password(password):
        if len(password) < 10:                                  # Check if password is at least 10 characters long
            print("Password must be at least 10 characters long.")
        if not re.search(r'[A-Z]', password):                   # Check if password contains at least one uppercase letter
            print("Password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', password):                   # Check if password contains at least one lowercase letter
            print("Password must contain at least one lowercase letter.")  
        if not re.search(r'[^A-Za-z0-9]', password):            # Check if password contains at least one special character
            print("Password must contain at least one special character.")
        if not re.search(r'\d', password):                      # Check if password contains at least one digit
            print("Password must contain at least one digit.")
        return True

    if check_password(password):
        print("Password meets the criteria.")
    else:
        print("Password does not meet the criteria.")

    password = input("Enter a password: ")
    print(check_password(password))
    
    def createWindow(self):
        pygame.init()
        windowWidth = 400
        windowHeight = 600
        BACKGROUND = (234, 234, 234)
        BUTTON = (0, 171, 179)
        TEXT = (60, 64, 72)
        pygame.display.set_caption("User")
        window = pygame.display.set_mode((windowWidth, windowHeight))
        window.fill(BACKGROUND)


        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()

        pygame.quit()
    
if __name__ == "__main__":
    user = User("example_username", "example_password", "John", "Doe", "john@example.com")
    user.createWindow()

