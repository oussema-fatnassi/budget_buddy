import pygame
import pygame_gui
import sys
from GUI import GUI
from user import User
import database_operation
from page_manager import PageManager

def connectionPage():
    gui = GUI()
    window = gui.createWindow("Connection Page")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    gui.createImage(window, 200, 150, 300, 200, "images/logo.png")
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
        object_id="show_password_button",
        tool_tip_text="Show password"
    )

    loginButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150, 500), (100, 30)),
        text="LOGIN",
        manager=gui.MANAGER,
        object_id="login_button",
        tool_tip_text="Login to your account"
    )
    registerButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150, 550), (100, 30)),
        text="REGISTER",
        manager=gui.MANAGER,
        object_id="register_button",
        tool_tip_text="Create a new account"
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
                        email = emailInput.get_text()  # Retrieve email entered by the user
                        password = user.hashPassword(passwordInput.get_text())  # Retrieve password entered by the user
                        user.login(email, password)  # Pass email and password to the login method
                        if database_operation.verify_user(email, password):
                            user_retrieved = database_operation.get_user_data(email)
                            PageManager.show_user_page(user_retrieved)
                        else:
                            pygame_gui.windows.UIMessageWindow(
                                rect=pygame.Rect((50, 50), (300, 300)),
                                manager=gui.MANAGER,
                                html_message="Login failed. Please try again.",
                                object_id="message_box"
                            )
                    elif event.ui_element == registerButton:
                        PageManager.show_account_creation_page()
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

            gui.MANAGER.process_events(event)
        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(uiRefreshRate)
        gui.createImage(window, 200, 150, 300, 200, "images/logo.png")
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

if __name__ == "__main__":
    connectionPage()
