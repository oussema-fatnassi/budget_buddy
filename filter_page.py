import pygame
import pygame_gui
import sys
from GUI import GUI
from page_manager import PageManager

def filterPage():
    gui = GUI()
    window = gui.createWindow("Filter Page")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    logo = gui.createImage(window, 50, 50, 50, 50, "images/logo.png")
    label = gui.createLabel(window, 50, 150, 300, 50, "Select how to filter transactions:")
    dateButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((50, 200), (300, 50)),
        text="Sort By Date",
        manager=gui.MANAGER,
        object_id="filters_button"
    )
    categoryButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((50, 260), (300, 50)),
        text="Sort By Category",
        manager=gui.MANAGER,
        object_id="filters_button"
    )
    typeButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((50, 320), (300, 50)),
        text="Sort By Type",
        manager=gui.MANAGER,
        object_id="filters_button"
    )
    amountButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((50, 380), (300, 50)),
        text="Sort By Amount",
        manager=gui.MANAGER,
        object_id="filters_button"
    )
    betweenTwoDatesButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((50, 440), (300, 50)),
        text="Sort Between Two Dates",
        manager=gui.MANAGER,
        object_id="filters_button"
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
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == dateButton:
                        print("Sort By Date")
                    elif event.ui_element == categoryButton:
                        print("Sort By Category")
                    elif event.ui_element == typeButton:
                        print("Sort By Type")
                    elif event.ui_element == amountButton:
                        print("Sort By Amount")
                    elif event.ui_element == betweenTwoDatesButton:
                        print("Sort Between Two Dates")
                    elif event.ui_element == closeButton:
                        PageManager.show_user_page()

        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(gui.uiRefreshRate)
        gui.createImage(window, 50, 50, 50, 50, "images/Logo.png")
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

if __name__ == "__main__":
    filterPage()