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
    user = User()

    emailLabel = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 270), (60, 30)),
        text="Email",
        manager=gui.MANAGER,
        object_id="label"
    )
    passwordLabel = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 370), (85, 30)),
        text="Password",
        manager=gui.MANAGER,
        object_id="label"
    )

    emailInput = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((40, 300), (300, 30)),
        manager=gui.MANAGER,
        object_id="text_input"
    )
    passwordInput = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((40, 400), (300, 30)),
        manager=gui.MANAGER,
        object_id="text_input"
    )
    passwordInput.set_text_hidden(True)

    showPasswordButton = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 400), (33, 22)),
    text="",
    manager=gui.MANAGER,
    object_id="show_password_button"
    )

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

    showPassword = False
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
                    elif event.ui_element == showPasswordButton:
                        if not showPassword:
                            # Show password
                            passwordInput.set_text_hidden(False)
                            showPassword = True
                        else:
                            # Hide password
                            passwordInput.set_text_hidden(True)
                            showPassword = False
                        showPasswordButton.pressed = False
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