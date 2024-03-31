import pygame
import pygame_gui
import sys
from GUI import GUI
from page_manager import PageManager

def monthlyTransactionList():
    gui = GUI()
    window = gui.createWindow("Monthly Transaction List")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    gui.createImage(window, 50, 50, 100, 100, "images/logo.png")
    gui.createLabel(window, 20, 120, 150, 30, "Select a month :")
    monthList = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((200, 120), (100, 30)),
        options_list=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        starting_option="January",
        manager=gui.MANAGER,)
    gui.createLabel(window, 20, 160, 150, 30, "Select a year :")
    yearList = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((200, 160), (100, 30)),
        options_list=["2024","2023","2022","2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010"],
        starting_option="2024",
        manager=gui.MANAGER,)
    gui.createButton(window, 150, 200, 100, 30, "GET LIST")
    TransactionsList = pygame_gui.elements.UISelectionList(
        relative_rect=pygame.Rect((50, 300), (300, 150)),
        item_list=["Transaction 1", "Transaction 2", "Transaction 3", "Transaction 4", "Transaction 5"],
        manager=gui.MANAGER,)
    
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
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == closeButton:
                        PageManager.show_user_page()
            gui.MANAGER.process_events(event)
            
        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(uiRefreshRate)
        gui.createImage(window, 50, 50, 100, 100, "images/Logo.png")  
        gui.MANAGER.draw_ui(window)   
        pygame.display.update()

if __name__ == "__main__":
    monthlyTransactionList()