import pygame
import pygame_gui
import sys
from GUI import GUI
from page_manager import PageManager
import database_operation
import datetime

def monthlyTransactionList(retrieved_user):
    gui = GUI()
    window = gui.createWindow("Monthly Transaction List")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    gui.createImage(window, 50, 50, 100, 100, "images/logo.png")

    selectMonthLabel = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((20, 120), (150, 30)),
        text="Select a month :",
        manager=gui.MANAGER,
        object_id="label"
    )
    monthList = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((200, 120), (100, 30)),
        options_list=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        starting_option="January",
        manager=gui.MANAGER,)
    selectYearLabel = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((15, 160), (150, 30)),
        text="Select a year :",
        manager=gui.MANAGER,
        object_id="label"
    )
    yearList = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((200, 160), (100, 30)),
        options_list=["2024","2023","2022","2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010"],
        starting_option="2024",
        manager=gui.MANAGER,)
    lastTransactionsList = pygame_gui.elements.UISelectionList(
        relative_rect=pygame.Rect((50, 300), (300, 150)),
        item_list=[],
        manager=gui.MANAGER,)
    
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

    monthlyIncome = pygame_gui.elements.UITextBox(
        relative_rect=pygame.Rect((180, 200), (150, 30)),
        html_text="",
        manager=gui.MANAGER,
        object_id="text_box"
    )
    monthlyExpense = pygame_gui.elements.UITextBox(
        relative_rect=pygame.Rect((180, 240), (150, 30)),
        html_text="",
        manager=gui.MANAGER,
        object_id="text_box"
    )
    montlyIncomeLabel = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((22, 200), (150, 30)),
        text="Monthly Income :",
        manager=gui.MANAGER,
        object_id="label"
    )
    monthlyExpenseLabel = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((26, 240), (150, 30)),
        text="Monthly Expense :",
        manager=gui.MANAGER,
        object_id="label"
    )

    all_transactions = database_operation.get_all_transactions(retrieved_user[0])
    lastTransactionsList.add_items(all_transactions)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == closeButton:
                        PageManager.show_user_page(retrieved_user)
                    elif event.ui_element == confirmButton:
                        selected_month = monthList.selected_option
                        selected_year = int(yearList.selected_option)
                        month_number = datetime.datetime.strptime(selected_month, "%B").month                                        # Convert month name to number                 
                        selected_month_year = datetime.date(selected_year, month_number,1)                                              # Format the selected date   

                        transactions, total_income, total_expenses = database_operation.get_monthly_transactions(retrieved_user[0], month_number, selected_year)

                        # Display transactions in the list
                        lastTransactionsList.remove_items(all_transactions)
                        lastTransactionsList.add_items(transactions)

                        # Display total income and expenses
                        monthlyIncome.html_text = ""
                        monthlyIncome_text = str(total_income)
                        monthlyIncome.append_html_text(monthlyIncome_text)

                        monthlyExpense.html_text = ""
                        monthlyExpense_text = str(total_expenses)
                        monthlyExpense.append_html_text(monthlyExpense_text)

                elif event.user_type == pygame_gui.UI_SELECTION_LIST_DOUBLE_CLICKED_SELECTION:
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
            gui.MANAGER.process_events(event)
            
        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(uiRefreshRate)
        gui.createImage(window, 50, 50, 100, 100, "images/Logo.png")  
        gui.MANAGER.draw_ui(window)   
        pygame.display.update()

if __name__ == "__main__":
    monthlyTransactionList()