import pygame
import pygame_gui
import sys
from GUI import GUI
from pygame_gui.core import ObjectID
from page_manager import PageManager
import database_operation

def sortByType(retrieved_user):
    gui = GUI()
    window = gui.createWindow("Sort By Type")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    logo = gui.createImage(window, 50, 50, 50, 50, "images/logo.png")
    label = gui.createLabel(window, -50, 100, 300, 50, "Sort by type")
    labelTransactionList = gui.createLabel(window, -40, 200, 300, 50, "Transaction List")

    lastTransactionsList = pygame_gui.elements.UISelectionList(
        relative_rect=pygame.Rect((50, 250), (300, 150)),
        item_list=[],
        manager=gui.MANAGER,
        object_id=ObjectID("selection_list")
    )
    typeList = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((50, 150), (300, 50)),
        options_list=["Income", "Expense"],
        starting_option="Income",
        manager=gui.MANAGER,
        object_id=ObjectID("drop_down")
    )
    
    confirmButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150, 500), (100, 30)),
        text='CONFIRM',
        manager=gui.MANAGER,
        object_id=ObjectID("confirm_button")
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
                        selected_type = typeList.selected_option.upper()
                        transactions = database_operation.get_transactions_by_type(retrieved_user[0], selected_type)
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
    sortByType()