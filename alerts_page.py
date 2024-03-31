import pygame
import pygame_gui
import sys
from GUI import GUI
from page_manager import PageManager

def alerts():
    gui = GUI()
    window = gui.createWindow("Alerts Page")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    logo = gui.createImage(window, 50, 50, 50, 50, "images/logo.png")
    label = gui.createLabel(window, 50, 150, 300, 50, "Select alert to view details")

    alertsList = pygame_gui.elements.UISelectionList(
        relative_rect=pygame.Rect((50, 200), (300, 350)),
        item_list=["Alert 1", "Alert 2", "Alert 3", "Alert 4", "Alert 5"],
        manager=gui.MANAGER,
        object_id="alerts_list"
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
                    if event.ui_element == alertsList:
                        selected_item = event.text
                        print("Double-click event detected")  # Debugging print statement
                        gui.createMessageBox(window, 50, 50, 300, 300, selected_item)
                if event.ui_element == closeButton:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        PageManager.show_user_page()

        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(gui.uiRefreshRate)
        gui.createImage(window, 50, 50, 50, 50, "images/Logo.png")
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

if __name__ == "__main__":
    alerts()