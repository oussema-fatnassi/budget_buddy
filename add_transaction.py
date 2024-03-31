import pygame
import pygame_gui
import sys
from GUI import GUI
from datetime import datetime
from database_operation import insert_transaction_data, create_tables
from transaction import Transaction
from user import User

def addTransaction(user):
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
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == confirmButton:
                    name = nameInput.get_text()
                    description = descriptionInput.get_text()
                    amount = float(amountInput.get_text())
                    category = categoryInput.selected_option
                    transaction_type = typeInput.selected_option
                    date = datetime.now().strftime("%Y-%m-%d")
                    
                    # Create Transaction object
                    transaction = Transaction(name, description, amount, category, transaction_type, date)
                    
                    # Insert transaction into the database
                    insert_transaction_data(user.email, transaction)
                    
                    # Optionally, you can clear the input fields after adding the transaction
                    nameInput.set_text('')
                    descriptionInput.set_text('')
                    amountInput.set_text('')
                    
                    # Provide feedback to the user
                    print("Transaction added successfully!")

        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(uiRefreshRate)
        gui.createImage(window, 50, 50, 100, 100, "images/Logo.png")  
        gui.MANAGER.draw_ui(window)   
        pygame.display.update()

if __name__ == "__main__":
    create_tables()
    user = User()
    addTransaction(user)