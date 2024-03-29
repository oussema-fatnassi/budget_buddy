import pygame
import pygame_gui
import sys
from GUI import GUI
from pygame_gui.core import ObjectID

def sortByType():
    gui = GUI()
    window = gui.createWindow("Sort By Type")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    logo = gui.createImage(window, 50, 50, 50, 50, "images/logo.png")
    label = gui.createLabel(window, -50, 100, 300, 50, "Sort by type")
    labelTransactionList = gui.createLabel(window, -40, 200, 300, 50, "Transaction List")

    lastTransactionsList = pygame_gui.elements.UISelectionList(
        relative_rect=pygame.Rect((50, 250), (300, 150)),
        item_list=["Transaction 1", "Transaction 2", "Transaction 3", "Transaction 4", "Transaction 5"],
        manager=gui.MANAGER,
        object_id=ObjectID("selection_list")
    )
    selectionDropDown = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((50, 150), (300, 50)),
        options_list=["Resources", "Expenses"],
        starting_option="Resources",
        manager=gui.MANAGER,
        object_id=ObjectID("drop_down")
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
                        selectionDropDown = selectionDropDown.selected_option
                        print("Selected option:", selectionDropDown)

        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(gui.uiRefreshRate)
        gui.createImage(window, 50, 50, 50, 50, "images/Logo.png")
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

if __name__ == "__main__":
    sortByType()