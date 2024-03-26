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
    
if __name__ == "__main__":
    user = User("example_username", "example_password", "John", "Doe", "john@example.com")
    user.createWindow()

