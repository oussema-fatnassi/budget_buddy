import pygame
import pygame_gui
import sys

class GUI:
    def __init__(self):                                                                             # Constructor to initialize the GUI object
        self.windowWidth = 400
        self.windowHeight = 600
        self.BACKGROUND = (234, 234, 234)
        self.BUTTON = (0, 171, 179)
        self.TEXT = (60, 64, 72)
        clock = pygame.time.Clock()
        self.uiRefreshRate = clock.tick(60) / 10000.0
        self.MANAGER = None
        self.textInput = None
        self.label = None
        self.dropDown = None
        self.passwordInput = None

    def createWindow(self, windowTitle):                                                                         # Method to create the window
        pygame.init()
        pygame.display.set_caption(windowTitle)
        window = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        window.fill(self.BACKGROUND)
        self.MANAGER = pygame_gui.UIManager((self.windowWidth, self.windowHeight))
        return window


    def createTextInput(self, window, pos_x, pos_y, width, height, id):                                 # Method to create the text input field
        self.textInput = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((pos_x, pos_y), (width, height)),
            manager=self.MANAGER,
            object_id = id
        )

    def createImage(self, window, pos_x, pos_y, width, height, image):                              # Method to create the image
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        window.blit(self.image, self.rect)

    def createButton(self, window, pos_x, pos_y, width, height, text):                              # Method to create the button
        self.button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((pos_x, pos_y), (width, height)),
            text=text,
            manager=self.MANAGER,
            object_id="button"
        )

    def createLabel(self, window, pos_x, pos_y, width, height, text):                               # Method to create the label
        self.label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((pos_x, pos_y), (width, height)),
            text=text,
            manager=self.MANAGER,
            object_id="label"
        )

    def createDropDown(self, window, pos_x, pos_y, width, height, options):                         # Method to create the drop down menu
        self.dropDown = pygame_gui.elements.UIDropDownMenu(
            relative_rect=pygame.Rect((pos_x, pos_y), (width, height)),
            options_list=options,
            starting_option=options[0],
            manager=self.MANAGER,
            object_id="drop_down"
        )
        self.dropDown.expand_on_option_click=False
    
    def createSelectionList(self, window, pos_x, pos_y, width, height, options, bool):
            self.selectionList = pygame_gui.elements.UISelectionList(
                relative_rect=pygame.Rect((pos_x, pos_y), (width, height)),
                item_list=options,
                allow_double_clicks=True,
                manager=self.MANAGER,
                object_id="selection_list"
            )
            # Store a dictionary mapping each item to its corresponding message
            self.item_messages = {item: f"Message for {item}" for item in options}

    
    def createPasswordInput(self, window, pos_x, pos_y, width, height):                             # Method to create the password input field
        self.passwordInput = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((pos_x, pos_y), (width, height)),
            manager=self.MANAGER,
            object_id="password_input"
        )

    def set_text_hidden(self, is_hidden=True):                                                      # Method to hide the password input field
        self.passwordInput.set_text_hidden(is_hidden)

    def createMessageBox(self, window, pos_x, pos_y, width, height, text):
        self.messageBox = pygame_gui.windows.UIMessageWindow(
            rect=pygame.Rect((pos_x, pos_y), (width, height)),
            html_message=text,  
            manager=self.MANAGER,
            window_title='Message Box',  
            object_id="message_box"
        )


    def createTextBox(self, window, pos_x, pos_y, width, height, text):                             # Method to create the text box
        self.textBox = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((pos_x, pos_y), (width, height)),
            html_text=text,
            manager=self.MANAGER,
            object_id="text_box"
        )

    def get_text_entries(self):
        text_entries = {} 
        root_container = self.MANAGER.get_root_container()
        for container in root_container.get_container():
            for element in container.elements:
                if isinstance(element, pygame_gui.elements.UITextEntryLine):
                    text_entries[element.rect.topleft] = element.get_text()
        return text_entries

    def main(self):                                                                                     # Main method to run the GUI
        window = self.createWindow("GUI TEST")
        self.createTextInput(window, 50, 300, 300, 30)
        self.createButton(window, 50, 350, 100, 30, "LOGIN")
        self.createLabel(window, 50, 250, 100, 30, "Email")
        self.createDropDown(window, 50, 400, 200, 30, ["Option 1", "Option 2", "Option 3"])
        self.createPasswordInput(window, 50, 550, 300, 30)
        self.set_text_hidden(True)
        self.createImage(window, 200, 100, 100, 100, "images/Logo.png") 
        self.createSelectionList(window, 50, 450, 200, 70, ["Option 1", "Option 2", "Option 3"],True) 
        self.createTextBox(window, 50, 180, 300, 50, "YOU ARE POOR! GO TO WORK!")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.MANAGER.process_events(event)
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.button:
                            self.createMessageBox(window, 50, 50, 300, 300, "This is a message box.")
                    elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                        print("Entered text:", event.text)
                    elif event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                        if event.ui_element == self.dropDown:
                            print("Selected option:", event.text)
                    elif event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                        if event.ui_element == self.textInput:
                            print("Entered text:", event.text)
                    elif event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                        if event.ui_element == self.passwordInput:
                            print("Entered password:", event.text)
                    elif event.user_type == pygame_gui.UI_WINDOW_CLOSE:
                        if event.ui_element == self.messageBox:
                            self.messageBox.kill()
                    elif event.user_type == pygame_gui.UI_SELECTION_LIST_DOUBLE_CLICKED_SELECTION:
                        if event.ui_element == self.selectionList:
                            selected_item = event.text
                            message = self.item_messages[selected_item]
                            self.createMessageBox(window, 50, 50, 300, 300, message)

            window.fill(self.BACKGROUND)  
            self.MANAGER.update(self.uiRefreshRate)
            self.createImage(window, 200, 100, 100, 100, "images/Logo.png")  
            self.MANAGER.draw_ui(window)  
            pygame.display.update()  

if __name__ == "__main__":
    window = GUI()
    window.main()