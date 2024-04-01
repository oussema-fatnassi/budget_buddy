import pygame
import pygame_gui
import sys
from GUI import GUI
from pygame_gui.core import ObjectID
from page_manager import PageManager

def sortBetweenTwoDates(retrieved_user):
    gui = GUI()
    window = gui.createWindow("Filter Transactions Between Two Dates")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    logo = gui.createImage(window, 50, 50, 50, 50, "images/logo.png")
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
        item_list=["Transaction 1", "Transaction 2", "Transaction 3", "Transaction 4", "Transaction 5"],
        manager=gui.MANAGER,
        object_id=ObjectID("selection_list")
    )
    dayList1 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((50, 175), (70, 30)),
        options_list=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"],
        starting_option="1",
        manager=gui.MANAGER,
        object_id=ObjectID("day_list1")
    )
    monthList1 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((125, 175), (120, 30)),
        options_list=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        starting_option="January",
        manager=gui.MANAGER,
        object_id=ObjectID("month_list1")
    )
    yearList1 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((250, 175), (90, 30)),
        options_list=["2024","2023","2022","2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010"],
        starting_option="2024",
        manager=gui.MANAGER,
        object_id=ObjectID("year_list1")
    )
    dayList2 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((50, 250), (70, 30)),
        options_list=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"],
        starting_option="1",
        manager=gui.MANAGER,
        object_id=ObjectID("day_list2")
    )
    monthList2 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((125, 250), (120, 30)),
        options_list=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        starting_option="January",
        manager=gui.MANAGER,
        object_id=ObjectID("month_list2")
    )
    yearList2 = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((250, 250), (90, 30)),
        options_list=["2024","2023","2022","2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010"],
        starting_option="2024",
        manager=gui.MANAGER,
        object_id=ObjectID("year_list2")
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
                        pass
                    if event.ui_element == closeButton:
                        PageManager.show_filter_page(retrieved_user)

        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(gui.uiRefreshRate)
        gui.createImage(window, 50, 50, 50, 50, "images/Logo.png")
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

if __name__ == "__main__":
    sortBetweenTwoDates()
