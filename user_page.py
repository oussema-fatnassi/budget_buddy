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
    logo = gui.createImage(window, 50, 50, 50, 50, "images/logo.png")

    logoutButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((325, 25), (58, 58)),
        text="",
        manager=gui.MANAGER,
        object_id="logout_button"
    )
    addTransactionButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((50, 200), (58, 58)),
        text="",
        manager=gui.MANAGER,
        object_id="add_transaction_button"
    )
    transactionListButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((175, 200), (58, 58)),
        text="",
        manager=gui.MANAGER,
        object_id="transaction_list_button"
    )
    filterButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((300, 200), (58, 58)),
        text="",
        manager=gui.MANAGER,
        object_id="filter_button"
    )
    monthlyRecapButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((50, 500), (58, 58)),
        text="",
        manager=gui.MANAGER,
        object_id="monthly_recap_button"
    )
    alertsButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((175, 500), (58, 58)),
        text="",
        manager=gui.MANAGER,
        object_id="alerts_button"
    )
    graphicsButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((300, 500), (58, 58)),
        text="",
        manager=gui.MANAGER,
        object_id="graphics_button"
    )
    lastTransactionsList = pygame_gui.elements.UISelectionList(
        relative_rect=pygame.Rect((50, 300), (300, 200)),
        item_list=[],
        manager=gui.MANAGER,
        object_id="selection_list",
        allow_double_clicks=True
    )
    currentAmount = pygame_gui.elements.UITextBox(
        relative_rect=pygame.Rect((100, 80), (200, 100)),
        html_text="",
        manager=gui.MANAGER,
        object_id="current_amount_text_box"
    )

    current_amount = database_operation.get_current_amount(retrieved_user[0])
    if current_amount is not None:
        current_amount_text = f"<b>Current Amount:</b> € {current_amount:.2f}"
        currentAmount.clear_all_active_effects()  # Clear any active effects first
        currentAmount.html_text = ""  # Clear existing text
        currentAmount.append_html_text(current_amount_text)  # Append new text

    user = User()
    # print("Retrieved user" + retrieved_user)
    user.setEmail(retrieved_user[3])                                        # Set the user's email
    user.setId(retrieved_user[0])
    user.setFirstName(retrieved_user[1])
    user.setLastName(retrieved_user[2])

    last_transactions = database_operation.get_last_transactions(retrieved_user[0])
    lastTransactionsList.add_items(last_transactions)
    print("Last transactions:" ,last_transactions)
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
                        print("Transaction details:", transaction_details)
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
                        PageManager.show_transaction_list_page()
                    if event.ui_element == filterButton:
                        PageManager.show_filter_page()
                    if event.ui_element == monthlyRecapButton:
                        PageManager.show_monthly_recap_page()
                    if event.ui_element == alertsButton:
                        PageManager.show_alerts_page()
                    if event.ui_element == graphicsButton:
                        PageManager.show_graphics_page()

            # Get the current amount from the database

        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(gui.uiRefreshRate)
        gui.createImage(window, 50, 50, 50, 50, "images/Logo.png")
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

# if __name__ == "__main__":
#     userPage()