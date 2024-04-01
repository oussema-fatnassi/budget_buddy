import pygame
import pygame_gui
import sys
from GUI import GUI
from user import User
from page_manager import PageManager
import database_operation 

def userPage(retrieved_user):
    gui = GUI()
    window = gui.createWindow("User Page")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    logo = gui.createImage(window, 50, 50, 75, 50, "images/logo.png")

    logoutButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((325, 25), (58, 58)),
        text="",
        manager=gui.MANAGER,
        object_id="logout_button",
        tool_tip_text="Logout"
    )
    addTransactionButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((50, 200), (58, 58)),
        text="",
        manager=gui.MANAGER,
        object_id="add_transaction_button",
        tool_tip_text="Add a new transaction"
    )
    transactionListButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((175, 200), (58, 58)),
        text="",
        manager=gui.MANAGER,
        object_id="transaction_list_button",
        tool_tip_text="View all transactions"
    )
    filterButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((300, 200), (58, 58)),
        text="",
        manager=gui.MANAGER,
        object_id="filter_button",
        tool_tip_text="Filter transactions"
    )
    monthlyRecapButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((50, 500), (58, 58)),
        text="",
        manager=gui.MANAGER,
        object_id="monthly_recap_button",
        tool_tip_text="View monthly recap"
    )
    alertsButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((175, 500), (58, 58)),
        text="",
        manager=gui.MANAGER,
        object_id="alerts_button",
        tool_tip_text="View alerts"
    )
    graphicsButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((300, 500), (58, 58)),
        text="",
        manager=gui.MANAGER,
        object_id="graphics_button",
        tool_tip_text="View graphics"
    )
    lastTransactionsList = pygame_gui.elements.UISelectionList(
        relative_rect=pygame.Rect((50, 300), (300, 150)),
        item_list=[],
        manager=gui.MANAGER,
        object_id="selection_list",
        allow_double_clicks=True
    )
    currentAmount = pygame_gui.elements.UITextBox(
        relative_rect=pygame.Rect((100, 100), (200, 80)),
        html_text="",
        manager=gui.MANAGER,
        object_id="current_amount_text_box"
    )
    userName = pygame_gui.elements.UITextBox(
        relative_rect=pygame.Rect((100, 30), (200, 50)),
        html_text="",
        manager=gui.MANAGER,
        object_id="user_name_text_box"
    )

    current_amount = database_operation.get_current_amount(retrieved_user[0])
    if current_amount is not None:
        current_amount_text = f"<b>Current Amount:</b> € {current_amount:.2f}"
        currentAmount.html_text = ""  # Clear existing text
        currentAmount.append_html_text(current_amount_text)  # Append new text

    user_data = database_operation.get_user_name(retrieved_user[3])  # Assuming the email is stored at index 3
    if user_data:
        first_name = user_data[1]  # First name is at index 1
        last_name = user_data[2]  # Last name is at index 2
        textName = f"{first_name.capitalize()} {last_name.capitalize()}"
        userName.html_text = ""  # Clear existing text
        userName.append_html_text(textName)  # Set the text of the userName textbox

    user = User()
    user.setEmail(retrieved_user[3])                                        # Set the user's email
    user.setId(retrieved_user[0])
    user.setFirstName(retrieved_user[1])
    user.setLastName(retrieved_user[2])


    last_transactions = database_operation.get_last_transactions(retrieved_user[0])
    lastTransactionsList.add_items(last_transactions)
    gui.MANAGER.update(gui.uiRefreshRate)
    gui.MANAGER.draw_ui(window)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            gui.MANAGER.process_events(event)

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_SELECTION_LIST_DOUBLE_CLICKED_SELECTION:
                    if event.ui_element == lastTransactionsList:
                        selected_item = event.text
                        transaction_details = database_operation.get_transaction_details(selected_item, retrieved_user[0])
                        if transaction_details:
                            details_text = f"<b>Name:</b> {transaction_details['name']}<br>" \
                               f"<b>Description:</b> {transaction_details['description']}<br>" \
                               f"<b>Amount: € </b> {transaction_details['amount']}<br>" \
                               f"<b>Category:</b> {transaction_details['category']}<br>" \
                               f"<b>Type:</b> {transaction_details['type']}<br>" \
                               f"<b>Date:</b> {transaction_details['date']}"
                        pygame_gui.windows.UIMessageWindow(
                            rect=pygame.Rect((50, 50), (300, 300)),
                            html_message= details_text,
                            manager=gui.MANAGER,
                            window_title='Transaction Details',
                            object_id="message_box"
                        )

                elif event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == logoutButton:
                        user.logout()
                        PageManager.show_home_page()
                    if event.ui_element == addTransactionButton:
                        PageManager.show_add_transaction_page(user, retrieved_user)
                    if event.ui_element == transactionListButton:
                        PageManager.show_transaction_list_page(retrieved_user)
                    if event.ui_element == filterButton:
                        PageManager.show_filter_page(retrieved_user)
                    if event.ui_element == monthlyRecapButton:
                        PageManager.show_monthly_recap_page(retrieved_user)
                    if event.ui_element == alertsButton:
                        PageManager.show_alerts_page(retrieved_user)
                    if event.ui_element == graphicsButton:
                        PageManager.show_graphics_page(retrieved_user)

            # Get the current amount from the database

        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(gui.uiRefreshRate)
        gui.createImage(window, 50, 50, 75, 50, "images/Logo.png")
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

# if __name__ == "__main__":
#     userPage()