import pygame
import pygame_gui
import sys
from GUI import GUI
from page_manager import PageManager
import database_operation
import datetime

def sortBetweenTwoDates(retrieved_user):                                                                               # Function to filter transactions between two dates              
    gui = GUI()
    window = gui.createWindow("Filter Transactions Between Two Dates")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    logo =gui.createImage(window, 50, 50, 75, 50, "images/Logo.png")
    titleLable = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((50, 80), (300, 50)),
        text="Select two dates to filter by",
        manager=gui.MANAGER,
        object_id="label"
    )
    labelFromDate = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((35, 145), (100, 30)),
        text="From Date",
        manager=gui.MANAGER,
        object_id="label"
    )
    labelToDate = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((30, 220), (100, 30)),
        text="To Date",
        manager=gui.MANAGER,
        object_id="label"
    )

    lastTransactionsList = pygame_gui.elements.UISelectionList(
        relative_rect=pygame.Rect((50, 300), (300, 150)),
        item_list=[],
        manager=gui.MANAGER,
        object_id="selection_list"
    )
    dayList1 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((50, 175), (70, 30)),
        options_list=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"],
        starting_option="1",
        manager=gui.MANAGER,
        object_id="day_list1"
    )
    monthList1 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((125, 175), (120, 30)),
        options_list=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        starting_option="January",
        manager=gui.MANAGER,
        object_id="month_list1"
    )
    yearList1 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((250, 175), (90, 30)),
        options_list=["2024","2023","2022","2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010"],
        starting_option="2024",
        manager=gui.MANAGER,
        object_id="year_list1"
    )
    dayList2 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((50, 250), (70, 30)),
        options_list=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"],
        starting_option="1",
        manager=gui.MANAGER,
        object_id="day_list2"
    )
    monthList2 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((125, 250), (120, 30)),
        options_list=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        starting_option="January",
        manager=gui.MANAGER,
        object_id="month_list2"
    )
    yearList2 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((250, 250), (90, 30)),
        options_list=["2024","2023","2022","2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010"],
        starting_option="2024",
        manager=gui.MANAGER,
        object_id="year_list2"
    )
    confirmButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150, 500), (100, 30)),
        text='CONFIRM',
        manager=gui.MANAGER,
        object_id="confirm_button",
        tool_tip_text="Display transactions for the selected date"
    )
    closeButton = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((150, 550), (100, 30)),
    text="CLOSE",
    manager=gui.MANAGER,
    object_id="close_button",
    tool_tip_text="Return to filter page"
    )

    all_transactions = database_operation.get_all_transactions(retrieved_user[0])                                       # Get all transactions for the user 
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
                        transaction_details = database_operation.get_transaction_details(selected_item, retrieved_user[0])          # Get transaction details
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
                        day1 = int(dayList1.selected_option)
                        month1 = monthList1.selected_option
                        year1 = int(yearList1.selected_option)
                        day2 = int(dayList2.selected_option)
                        month2 = monthList2.selected_option
                        year2 = int(yearList2.selected_option)

                        month_number1 = datetime.datetime.strptime(month1, "%B").month                                          # Convert month name to number                 
                        start_date = datetime.date(year1, month_number1, day1)                                               # Format the selected date   
                        month_number2 = datetime.datetime.strptime(month2, "%B").month                                        
                        end_date = datetime.date(year2, month_number2, day2)   

                        transactions = database_operation.get_transactions_between_dates(retrieved_user[0], start_date, end_date)
                        lastTransactionsList.remove_items(all_transactions)                                                     # Remove all transactions from the list
                        lastTransactionsList.add_items(transactions)                                                            # Get transactions for the selected date
                    if event.ui_element == closeButton:
                        PageManager.show_filter_page(retrieved_user)

        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(gui.uiRefreshRate)
        logo =gui.createImage(window, 50, 50, 75, 50, "images/Logo.png")
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

if __name__ == "__main__":
    sortBetweenTwoDates()
