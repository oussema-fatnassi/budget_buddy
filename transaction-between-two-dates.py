import pygame
import pygame_gui
import sys
from GUI import GUI
from pygame_gui.core import ObjectID

def transactionList():
    gui = GUI()
    window = gui.createWindow("Filter Transactions Between Two Dates")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    logo = gui.createImage(window, 50, 50, 50, 50, "images/logo.png")
    label = gui.createLabel(window, 50, 100, 300, 50, "Select two dates to filter by")
    labelFromDate = gui.createLabel(window, -65, 150, 300, 50, "From Date")
    labelToDate = gui.createLabel(window, -75, 225, 300, 50, "To Date")

    lastTransactionsList = pygame_gui.elements.UISelectionList(
        relative_rect=pygame.Rect((50, 350), (300, 150)),
        item_list=["Transaction 1", "Transaction 2", "Transaction 3", "Transaction 4", "Transaction 5"],
        manager=gui.MANAGER,
        object_id=ObjectID("selection_list")
    )
    dayList1 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((50, 200), (100, 30)),
        options_list=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"],
        starting_option="1",
        manager=gui.MANAGER,
        object_id=ObjectID("day_list1")
    )
    monthList1 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((150, 200), (100, 30)),
        options_list=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        starting_option="January",
        manager=gui.MANAGER,
        object_id=ObjectID("month_list1")
    )
    yearList1 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((250, 200), (100, 30)),
        options_list=["2024","2023","2022","2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010"],
        starting_option="2024",
        manager=gui.MANAGER,
        object_id=ObjectID("year_list1")
    )
    dayList2 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((50, 275), (100, 30)),
        options_list=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"],
        starting_option="1",
        manager=gui.MANAGER,
        object_id=ObjectID("day_list2")
    )
    monthList2 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((150, 275), (100, 30)),
        options_list=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        starting_option="January",
        manager=gui.MANAGER,
        object_id=ObjectID("month_list2")
    )
    yearList2 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((250, 275), (100, 30)),
        options_list=["2024","2023","2022","2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010"],
        starting_option="2024",
        manager=gui.MANAGER,
        object_id=ObjectID("year_list2")
    )
    confirmButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150, 525), (100, 30)),
        text='Confirm',
        manager=gui.MANAGER,
        object_id=ObjectID("confirm_button")
    )

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
                        pygame_gui.windows.UIMessageWindow(
                            rect=pygame.Rect((50, 50), (300, 300)),
                            html_message= selected_item,
                            manager=gui.MANAGER,
                            window_title='Message Box',
                            object_id="message_box"
                        )

                elif event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == confirmButton:
                            from_day = dayList1.selected_option
                            from_month = monthList1.selected_option
                            from_year = yearList1.selected_option
                            to_day = dayList2.selected_option
                            to_month = monthList2.selected_option
                            to_year = yearList2.selected_option

                            # Format selected dates as "DD/MM/YYYY"
                            from_date = f"{from_day}/{from_month}/{from_year}"
                            to_date = f"{to_day}/{to_month}/{to_year}"

                            # Print the selected dates
                            print("From Date:", from_date)
                            print("To Date:", to_date)
                            print("Button pressed event detected")  # Debugging print statement

        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(gui.uiRefreshRate)
        gui.createImage(window, 50, 50, 50, 50, "images/Logo.png")
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

if __name__ == "__main__":
    transactionList()

