import pygame
import pygame_gui
import sys
from GUI import GUI
from user import User
from database_operation import create_tables, insert_user_data
from page_manager import PageManager

def accountCreation():
    gui = GUI()
    user = User()
    window = gui.createWindow("Account Creation")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    gui.createImage(window, 350, 50, 100, 100, "images/logo.png")
    firstNameLabel = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 100), (100, 30)),
        text="First Name",
        manager=gui.MANAGER,
        object_id="label"
    )
    lastNameLabel = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 170), (90, 30)),
        text="Last Name",
        manager=gui.MANAGER,
        object_id="label"
    )
    emailLabel = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 240), (60, 30)),
        text="Email",
        manager=gui.MANAGER,
        object_id="label"
    )
    passwordLabel = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 310), (85, 30)),
        text="Password",
        manager=gui.MANAGER,
        object_id="label"
    )
    confirmPasswordLabel = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 380), (150, 30)),
        text="Confirm Password",
        manager=gui.MANAGER,
        object_id="label"
    )

    firstNameInput = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((20, 130), (300, 40)),
        manager=gui.MANAGER,
        object_id="text_input"
    )
    lastNameInput = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((20, 200), (300, 40)),
        manager=gui.MANAGER,
        object_id="text_input"
    )
    emailTextInput = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((20, 270), (300, 40)),
        manager=gui.MANAGER,
        object_id="text_input"
    )
    passwordTextInput = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((20, 340), (300, 40)),
        manager=gui.MANAGER,
        object_id="text_input"
    )
    passwordTextInput.set_text_hidden(True)

    showPasswordButton = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((330, 345), (33, 22)),
    text="",
    manager=gui.MANAGER,
    object_id="show_password_button"
    )
    confirmPasswordTextInput = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((20, 410), (300, 40)),
        manager=gui.MANAGER,
        object_id="text_input"
    )
    confirmPasswordTextInput.set_text_hidden(True)

    showConfirmPasswordButton = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((330, 415), (33, 22)),
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
    exit = False
    showPassword = False
    while exit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == showPasswordButton:
                        if not showPassword:
                            # Show password
                            passwordTextInput.set_text_hidden(False)
                            showPassword = True
                        else:
                            # Hide password
                            passwordTextInput.set_text_hidden(True)
                            showPassword = False
                        showPasswordButton.pressed = False
                    if event.ui_element == showConfirmPasswordButton:
                        if not showPassword:
                            # Show password
                            confirmPasswordTextInput.set_text_hidden(False)
                            showPassword = True
                        else:
                            # Hide password
                            confirmPasswordTextInput.set_text_hidden(True)
                            showPassword = False
                    if event.ui_element == loginButton:
                        exit = True                            
                        PageManager.show_connection_page()
                    elif event.ui_element == registerButton:
                        hashPassword = user.hashPassword(passwordTextInput.get_text())
                        if user.register(firstNameInput.get_text(), lastNameInput.get_text(), emailTextInput.get_text(), passwordTextInput.get_text(), confirmPasswordTextInput.get_text()) == True:
                            create_tables()                                                                                             # Create the users table if it doesn't exist            
                            insert_user_data(firstNameInput.get_text(), lastNameInput.get_text(), emailTextInput.get_text(), hashPassword)  # Insert user data into the database
                            firstNameInput.set_text("")
                            lastNameInput.set_text("")
                            emailTextInput.set_text("")
                            passwordTextInput.set_text("")
                            confirmPasswordTextInput.set_text("")
                            exit = True                         
                            PageManager.show_connection_page()
                        else:
                            error_message = "<b>Registration failed. Please make sure all fields are filled and passwords meet the criteria. Password must be:\n- At least 10 characters long\n- Contain at least one uppercase letter\n- Contain at least one lowercase letter\n- Contain at least one digit\n- Contain at least one special character<b>"
                            pygame_gui.windows.UIMessageWindow(
                                rect=pygame.Rect((50, 100), (300, 350)),
                                html_message= error_message,
                                window_title='Registration Error',
                                object_id="message_box",
                                manager=gui.MANAGER
                            )
            gui.MANAGER.process_events(event)

        window.fill(gui.BACKGROUND)  
        gui.MANAGER.update(uiRefreshRate)
        gui.createImage(window, 350, 50, 100, 100, "images/logo.png")
        gui.MANAGER.draw_ui(window)
        pygame.display.update()
    print("While loop exited.")

if __name__ == "__main__":
    accountCreation()