import pygame
import pygame_gui
import sys
from GUI import GUI

def alerts():
    gui = GUI()
    window = gui.createWindow("Alerts Page")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    logo = gui.createImage(window, 50, 50, 50, 50, "images/logo.png")
    label = gui.createLabel(window, 50, 150, 300, 50, "Select alert to view details")
    lastTransactionsList = gui.createSelectionList(window, 50, 200, 300, 350, ["Alert 1", "Alert 2", "Alert 3", "Alert 4", "Alert 5"], True)

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
    alerts()