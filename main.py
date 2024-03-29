import pygame
import pygame_gui
import sys
from GUI import GUI
from user import User
from connection_page import connectionPage
from home_page import homePage
from account_creation import accountCreation

def main():
    pygame.init()
    gui = GUI()
    home_page = homePage()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == homePage.loginButton:
                        print("test1")
                        connectionPage()
                    elif event.ui_element == homePage.createAccountButton:
                        print("test2")
                        accountCreation()

            gui.MANAGER.process_events(event)
        pygame.display.update()

if __name__ == "__main__":
    main()