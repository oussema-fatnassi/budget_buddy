import pygame
import pygame_gui
import sys
from GUI import GUI
from account_creation import accountCreation
from connection_page import connectionPage
from user import User

def homePage():
    
    gui = GUI()
    window = gui.createWindow("Home Page")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    gui.createImage(window, 200, 175, 300, 300, "images/logo.png")

    loginButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((100, 500), (200, 30)),
        text="LOGIN",
        manager=gui.MANAGER,
    )
    createAccountButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((100, 550), (200, 30)),
        text="CREATE NEW ACCOUNT",
        manager=gui.MANAGER,
    )
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == loginButton:
                        print("Login button pressed")
                        connectionPage()
                    elif event.ui_element == createAccountButton:
                        print("Create Account button pressed")
                        accountCreation()
                        connectionPage()

            gui.MANAGER.process_events(event)
        gui.MANAGER.update(uiRefreshRate)
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

if __name__ == "__main__":
    homePage()