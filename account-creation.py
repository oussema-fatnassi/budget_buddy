import pygame
import pygame_gui
import sys
from GUI import GUI

def accountCreation():
    gui = GUI()
    window = gui.createWindow("Account Creation")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    gui.createImage(window, 350, 50, 100, 100, "images/logo.png")
    gui.createLabel(window, 10, 100, 100, 30, "First Name")
    gui.createLabel(window, 10, 170, 90, 30, "Last Name")
    gui.createLabel(window, 10, 240, 60, 30, "Email")
    gui.createLabel(window, 10, 310, 85, 30, "Password")
    gui.createLabel(window, 10, 380, 150, 30, "Confirm Password")

    firstNameInput = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((20, 200), (300, 30)),
        manager=gui.MANAGER,
        object_id="text_input"
    )
    lastNameInput = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((20, 130), (300, 30)),
        manager=gui.MANAGER,
        object_id="text_input"
    )
    emailTextInput = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((20, 270), (300, 30)),
        manager=gui.MANAGER,
        object_id="text_input"
    )
    passwordTextInput = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((20, 340), (300, 30)),
        manager=gui.MANAGER,
        object_id="text_input"
    )
    passwordTextInput.set_text_hidden(True)
    
    confirmPasswordTextInput = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((20, 410), (300, 30)),
        manager=gui.MANAGER,
        object_id="text_input"
    )
    confirmPasswordTextInput.set_text_hidden(True)

    loginButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150, 500), (100, 30)),
        text="LOGIN",
        manager=gui.MANAGER,
    )
    registerButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150, 550), (100, 30)),
        text="REGISTER",
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
                        print("Login Button Pressed")
                    elif event.ui_element == registerButton:
                        print("Register Button Pressed")
                elif event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    if event.ui_element == firstNameInput:
                        print("First Name Entered:", event.text)
                    elif event.ui_element == lastNameInput:
                        print("Last Name Entered:", event.text)
                    elif event.ui_element == emailTextInput:
                        print("Email Entered:", event.text)
                    elif event.ui_element == passwordTextInput:
                        print("Password Entered:", event.text)
                    elif event.ui_element == confirmPasswordTextInput:
                        print("Confirm Password Entered:", event.text)

            gui.MANAGER.process_events(event)
        gui.MANAGER.update(uiRefreshRate)
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

if __name__ == "__main__":
    accountCreation()