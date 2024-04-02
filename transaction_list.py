import pygame
import pygame_gui
import sys
from GUI import GUI
from page_manager import PageManager
import database_operation

def transactionList(retrieved_user):                                                            # Function to display the transaction list page
    gui = GUI()
    window = gui.createWindow("Transaction List Page")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    gui.createImage(window, 50, 50, 75, 50, "images/Logo.png")
    label = gui.createLabel(window, 50, 150, 300, 50, "Double click on a transaction to view details")

    lastTransactionsList = pygame_gui.elements.UISelectionList(
        relative_rect=pygame.Rect((50, 200), (300, 250)),
        item_list=[],
        manager=gui.MANAGER,
        object_id="selection_list",
        allow_double_clicks=True
    )
    closeButton = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((150, 550), (100, 30)),
    text="CLOSE",
    manager=gui.MANAGER,
    object_id="close_button",
    tool_tip_text="Return to the user page"
    )

    all_transactions = database_operation.get_all_transactions(retrieved_user[0])               # Get all transactions from the database
    lastTransactionsList.add_items(all_transactions)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            gui.MANAGER.process_events(event)

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_SELECTION_LIST_DOUBLE_CLICKED_SELECTION:    # If the user double clicks on a transaction show the details of the transaction
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
                if event.ui_element == closeButton:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        PageManager.show_user_page(retrieved_user)

        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(gui.uiRefreshRate)
        gui.createImage(window, 50, 50, 75, 50, "images/Logo.png")
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

if __name__ == "__main__":
    transactionList()