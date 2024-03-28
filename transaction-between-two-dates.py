import pygame
import pygame_gui
import sys
from GUI import GUI

def transactionList():
    gui = GUI()
    window = gui.createWindow("Filter Transactions Between Two Dates")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    logo = gui.createImage(window, 50, 50, 50, 50, "images/logo.png")
    label = gui.createLabel(window, 50, 100, 300, 50, "Select two dates to filter by")
    labelFromDate = gui.createLabel(window, -65, 150, 300, 50, "From Date")
    lastTransactionsList = gui.createSelectionList(window, 50, 350, 300, 150, ["Transaction 1", "Transaction 2", "Transaction 3", "Transaction 4", "Transaction 5"], True)
    dayList1 = gui.createDropDown(window, 50, 200, 100, 30, ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"])
    monthList1 = gui.createDropDown(window, 150, 200, 100, 30, ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    yearList1 = gui.createDropDown(window, 250, 200, 100, 30, ["2024","2023","2022","2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010"])
    labelToDate = gui.createLabel(window, -75, 225, 300, 50, "To Date")
    dayList2 = gui.createDropDown(window, 50, 275, 100, 30, ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"])
    monthList2 = gui.createDropDown(window, 150, 275, 100, 30, ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    yearList2 = gui.createDropDown(window, 250, 275, 100, 30, ["2024","2023","2022","2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010"])



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            gui.MANAGER.process_events(event)

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_SELECTION_LIST_DOUBLE_CLICKED_SELECTION:
                    if event.ui_element == gui.selectionList:
                        selected_item = event.text
                        message = gui.item_messages[selected_item]
                        print("Double-click event detected")  # Debugging print statement
                        gui.createMessageBox(window, 50, 50, 300, 300, message)

        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(gui.uiRefreshRate)
        gui.createImage(window, 50, 50, 50, 50, "images/Logo.png")
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

if __name__ == "__main__":
    transactionList()