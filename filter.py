import pygame
import pygame_gui
import sys
from GUI import GUI

def transactionList():
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
        object_id="date_button"
    )
    categoryButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((50, 250), (300, 50)),
        text="Sort By Category",
        manager=gui.MANAGER,
        object_id="category_button"
    )
    typeButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((50, 300), (300, 50)),
        text="Sort By Type",
        manager=gui.MANAGER,
        object_id="type_button"
    )
    amountButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((50, 350), (300, 50)),
        text="Sort By Amount",
        manager=gui.MANAGER,
        object_id="amount_button"
    )
    betweenTwoDatesButton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((50, 400), (300, 50)),
        text="Sort Between Two Dates",
        manager=gui.MANAGER,
        object_id="between_two_dates_button"
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

        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(gui.uiRefreshRate)
        gui.createImage(window, 50, 50, 50, 50, "images/Logo.png")
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

if __name__ == "__main__":
    transactionList()