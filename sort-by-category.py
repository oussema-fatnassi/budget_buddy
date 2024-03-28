import pygame
import pygame_gui
import sys
from pygame_gui.windows.ui_message_window import UIMessageWindow
from GUI import GUI
from pygame_gui.core import ObjectID

def transactionList():
    gui = GUI()
    window = gui.createWindow("Sort By Category Page")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    logo = gui.createImage(window, 50, 50, 50, 50, "images/logo.png")
    label = gui.createLabel(window, 50, 100, 300, 50, "Select the category to filter by")

    lastTransactionsList = pygame_gui.elements.UISelectionList(
        relative_rect=pygame.Rect((50, 200), (300, 300)),
        item_list=["Transaction 1", "Transaction 2", "Transaction 3", "Transaction 4", "Transaction 5"],
        manager=gui.MANAGER,
        object_id=ObjectID("selection_list")
    )
    categoryList = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((50, 150), (300, 30)),
        options_list=["GROCERIES", "RENT", "UTILITIES", "TRANSPORTATION", "HEALTHCARE", "ENTERTAINMENT", "SALARY", "HOBBIES", "TRAVEL", "RESTAURANTS", "OTHERS"],
        starting_option="GROCERIES",
        manager=gui.MANAGER,
        object_id=ObjectID("day_list1")
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
                        UIMessageWindow(
                            rect=pygame.Rect((50, 50), (300, 300)),
                            html_message=selected_item,  
                            manager=gui.MANAGER,
                            window_title='Message Box',
                            object_id="message_box"
                        )

                elif event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == confirmButton:
                        categoryList = categoryList.selected_option
                        print("Category selected:", categoryList)

        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(gui.uiRefreshRate)
        gui.createImage(window, 50, 50, 50, 50, "images/Logo.png")
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

if __name__ == "__main__":
    transactionList()
