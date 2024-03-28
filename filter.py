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
    dateButton = gui.createButton(window, 50, 200, 300, 50, "Sort By Date")
    categoryButton = gui.createButton(window, 50, 250, 300, 50, "Sort By Category")
    typeButton = gui.createButton(window, 50, 300, 300, 50, "Sort By Type")
    amountButton = gui.createButton(window, 50, 350, 300, 50, "Sort By Amount")
    betweenTwoDatesButton = gui.createButton(window, 50, 400, 300, 50, "Sort Between Two Dates")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            gui.MANAGER.process_events(event)

            if event.type == pygame.USEREVENT:
                pass

        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(gui.uiRefreshRate)
        gui.createImage(window, 50, 50, 50, 50, "images/Logo.png")
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

if __name__ == "__main__":
    transactionList()