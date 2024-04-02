import pygame
import pygame_gui
import sys
from GUI import GUI
from user import User
from page_manager import PageManager

def homePage():                                                                                 # Shows the home page of the application where the user can login or create a new account
    
    gui = GUI()
    window = gui.createWindow("Home Page")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    gui.createImage(window, 200, 175, 300, 200, "images/logo.png")

    loginButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150, 500), (100, 30)),
        text="LOGIN",
        manager=gui.MANAGER,
        object_id="login_button_hp",
        tool_tip_text="Login to your account"
    )
    createAccountButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((100, 550), (200, 30)),
        text="CREATE NEW ACCOUNT",
        manager=gui.MANAGER,
        object_id="create_account_button",
        tool_tip_text="Create a new account"
    )
    welcomeMessage = pygame_gui.elements.UITextBox(
        relative_rect=pygame.Rect((50, 350), (300, 100)),
        html_text="<font face=arial size=4 color=black>Welcome to BUDGET BUDDY, your favorite money budgeting application</font>",
        manager=gui.MANAGER,
        object_id="welcome_message"
    )
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == loginButton:
                        PageManager.show_connection_page()
                    elif event.ui_element == createAccountButton:
                        PageManager.show_account_creation_page()
                        PageManager.show_connection_page()

            gui.MANAGER.process_events(event)
        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(uiRefreshRate)
        gui.createImage(window, 200, 175, 300, 200, "images/logo.png")
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

if __name__ == "__main__":
    homePage()