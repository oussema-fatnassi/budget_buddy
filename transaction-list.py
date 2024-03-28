import pygame
import pygame_gui
import sys
from GUI import GUI

def transactionList():
    gui = GUI()
    window = gui.createWindow("Transaction List Page")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    logo = gui.createImage(window, 50, 50, 50, 50, "images/logo.png")
    label = gui.createLabel(window, 50, 150, 300, 50, "Select a transaction to view details")
    lastTransactionsList = gui.createSelectionList(window, 50, 200, 300, 350, ["Transaction 1", "Transaction 2", "Transaction 3", "Transaction 4", "Transaction 5"], True)

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