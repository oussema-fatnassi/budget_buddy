import pygame
import pygame_gui
import sys
from GUI import GUI
from page_manager import PageManager
import database_operation
import datetime

def sortByDate(retrieved_user):
    gui = GUI()
    window = gui.createWindow("Filter Transactions By Date")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    logo = gui.createImage(window, 50, 50, 50, 50, "images/logo.png")
    label = gui.createLabel(window, 50, 100, 300, 50, "Select date to filter by")
    labelFromDate = gui.createLabel(window, -90, 150, 300, 50, "Date")

    lastTransactionsList = pygame_gui.elements.UISelectionList(
        relative_rect=pygame.Rect((50, 300), (300, 150)),
        item_list=[],
        manager=gui.MANAGER,
        object_id="selection_list",
        allow_double_clicks=True
    )
    dayList1 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((50, 200), (100, 30)),
        options_list=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"],
        starting_option="1",
        manager=gui.MANAGER,
        object_id="day_list1"
    )
    monthList1 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((150, 200), (100, 30)),
        options_list=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        starting_option="January",
        manager=gui.MANAGER,
        object_id="month_list1"
    )
    yearList1 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((250, 200), (100, 30)),
        options_list=["2024","2023","2022","2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010"],
        starting_option="2024",
        manager=gui.MANAGER,
        object_id="year_list1"
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
                        day = int(dayList1.selected_option)
                        month = monthList1.selected_option
                        year = int(yearList1.selected_option)
                        month_number = datetime.datetime.strptime(month, "%B").month                                        # Convert month name to number                 
                        selected_date = datetime.date(year, month_number, day)                                              # Format the selected date   
                        transactions = database_operation.get_transactions_by_date(retrieved_user[0], selected_date)        # Get transactions for the selected date
                        lastTransactionsList.remove_items(all_transactions)                                                 # Remove all transactions from the list
                        lastTransactionsList.add_items(transactions)                                                        # Add the transactions for the selected date to the list 

                    if event.ui_element == closeButton:
                        PageManager.show_filter_page(retrieved_user)

        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(gui.uiRefreshRate)
        gui.createImage(window, 50, 50, 50, 50, "images/Logo.png")
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

if __name__ == "__main__":
    sortByDate()

