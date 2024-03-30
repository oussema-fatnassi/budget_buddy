import pygame
import pygame_gui
import sys
from GUI import GUI
from user import User

def connectionPage():
    gui = GUI()
    window = gui.createWindow("Connection Page")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    gui.createImage(window, 200, 100, 100, 100, "images/logo.png")
    gui.createLabel(window, 20, 250, 100, 30, "Email")
    gui.createLabel(window, 30, 350, 100, 30, "Password")
    user = User()

    emailInput = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((50, 300), (300, 30)),
        manager=gui.MANAGER,
        object_id="email_input"
    )
    passwordInput = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((50, 400), (300, 30)),
        manager=gui.MANAGER,
        object_id="password_input"
    )
    passwordInput.set_text_hidden(True)

    loginButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150, 500), (100, 30)),
        text="LOGIN",
        manager=gui.MANAGER,
        object_id="login_button"
    )
    registerButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150, 550), (100, 30)),
        text="REGISTER",
        manager=gui.MANAGER,
        object_id="register_button"
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
                        user.login(emailInput.get_text(), passwordInput.get_text())
                        print("Email: ", user.getEmail())
                        print("Password: ", user.getPassword())
                    elif event.ui_element == registerButton:
                        print("Register button pressed")
                if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    if event.ui_element == emailInput:
                        print("Email entered: ", emailInput.get_text())
                    elif event.ui_element == passwordInput:
                        print("Password entered: ", passwordInput.get_text())

            gui.MANAGER.process_events(event)
        gui.MANAGER.update(uiRefreshRate)
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

if __name__ == "__main__":
    connectionPage()