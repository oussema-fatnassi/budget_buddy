import pygame
import pygame_gui
import sys
from pygame_gui.windows.ui_message_window import UIMessageWindow
from GUI import GUI
from page_manager import PageManager
import database_operation

def sortByCategory(retrieved_user):
    gui = GUI()
    window = gui.createWindow("Sort By Category Page")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    logo = gui.createImage(window, 50, 50, 50, 50, "images/logo.png")
    label = gui.createLabel(window, 50, 100, 300, 50, "Select the category to filter by")

    lastTransactionsList = pygame_gui.elements.UISelectionList(
        relative_rect=pygame.Rect((50, 200), (300, 280)),
        item_list=[],
        manager=gui.MANAGER,
        object_id="selection_list"
    )
    categoryList = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((50, 150), (300, 30)),
        options_list=["GROCERIES", "RENT", "UTILITIES", "TRANSPORTATION", "HEALTHCARE", "ENTERTAINMENT", "SALARY", "HOBBIES", "TRAVEL", "RESTAURANTS", "OTHERS"],
        starting_option="GROCERIES",
        manager=gui.MANAGER,
        object_id="day_list1"
    )
    confirmButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150, 500), (100, 30)),
        text='CONFIRM',
        manager=gui.MANAGER,
        object_id="confirm_button"
    )
    closeButton = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((150, 550), (100, 30)),
    text="CLOSE",
    manager=gui.MANAGER,
    object_id="close_button"
    )

    all_transactions = database_operation.get_all_transactions(retrieved_user[0])
    lastTransactionsList.add_items(all_transactions)


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
                        details_text = ""
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
                    if event.ui_element == confirmButton:
                        selected_category = categoryList.selected_option.upper()
                        transactions = database_operation.get_transactions_by_category(retrieved_user[0], selected_category)
                        lastTransactionsList.remove_items(all_transactions)
                        lastTransactionsList.add_items(transactions)

                    if event.ui_element == closeButton:
                        PageManager.show_filter_page(retrieved_user)

        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(gui.uiRefreshRate)
        gui.createImage(window, 50, 50, 50, 50, "images/Logo.png")
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

if __name__ == "__main__":
    sortByCategory()