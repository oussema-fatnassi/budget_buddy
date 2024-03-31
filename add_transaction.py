import pygame
import pygame_gui
import sys
from GUI import GUI

def addTransaction():
    gui = GUI()
    window = gui.createWindow("Add Transaction")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    gui.createImage(window, 50, 50, 100, 100, "images/logo.png")
    nameLabel = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((30, 120), (50, 30)),
        text="Name",
        manager=gui.MANAGER,
        object_id="label"
    )
    nameInput = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((30, 150), (300, 30)),
        manager=gui.MANAGER,
        object_id="text_input"
    )
    descriptionLabel = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((30, 180), (90, 30)),
        text="Description",
        manager=gui.MANAGER,
        object_id="label"
    )
    descriptionInput = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((30, 210), (300, 70)),
        manager=gui.MANAGER,
        object_id="text_input"
    )

    amountLabel = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((30, 280), (60, 30)),
        text="Amount",
        manager=gui.MANAGER,
        object_id="label"
    )
    amountInput = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((30, 310), (100, 30)),
        manager=gui.MANAGER,
        object_id="text_input"
    )
    typeLabel = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((30, 340), (50, 30)),
        text="Type",
        manager=gui.MANAGER,
        object_id="label"
    )
    typeInput = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((30, 370), (200, 30)),
        manager=gui.MANAGER,
        starting_option="Income",
        options_list=["Income", "Expense"]
    )
    categoryInput = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((30, 430), (200, 30)),
        manager=gui.MANAGER,
        starting_option="Others",
        options_list=["Groceries", "Rent", "Utilities", "Transportation", "Healthcare", "Entertainment", "Salary", "Hobbies", "Travel", "Restaurants", "Others"]
    )
    categoryLabel = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((30, 400), (80, 30)),
        text="Category",
        manager=gui.MANAGER,
        object_id="label"
    )

    confirmButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150, 550), (100, 30)),
        text="CONFIRM",
        manager=gui.MANAGER,
        object_id="confirm_button"
    )


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            gui.MANAGER.process_events(event)
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                print("Entered text:", event.text)
                if event.ui_element == Text1:
                    print("text input 1")
                    Text1 = event.text
                elif event.ui_element == Text2:
                    print("text input 2")
                    Text2 = event.text
                elif event.ui_element == Text3:
                    print("text input 3")
                    Text3 = event.text
                print(Text1, Text2, Text3, Drop1, Drop2)
            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                print("Selected option:", event.text)
                if event.ui_element == Drop1:
                    print("drop down 1")
                    Drop1 = event.text
                elif event.ui_element == Drop2:
                    print("drop down 2")
                    Drop2 = event.text
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == gui.button:
                        # selected_item = event.text
                        message = "Transaction added successfully! \n\nName: " + Text1 + "\nDescription: " + Text2 + "\nAmount: " + Text3 + "\nType: " + Drop1 + "\nCategory: " + Drop2
                        gui.createMessageBox(window, 50, 50, 300, 300, message)

        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(uiRefreshRate)
        gui.createImage(window, 50, 50, 100, 100, "images/Logo.png")  
        gui.MANAGER.draw_ui(window)   
        pygame.display.update()

if __name__ == "__main__":
    addTransaction()