import pygame
import pygame_gui
import sys
from GUI import GUI

def userPage():
    gui = GUI()
    window = gui.createWindow("User Page")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    logo = gui.createImage(window, 50, 50, 50, 50, "images/logo.png")
    logoutButton = gui.createButton(window, 325, 25, 50, 50, "Logout")
    currentAmount = gui.createTextBox(window, 100, 100, 200, 100, "100000000 €")
    addTransactionButton = gui.createButton(window, 50, 250, 50, 50, "Add")
    transactionListButton = gui.createButton(window, 175, 250, 50, 50, "List")
    filterButton = gui.createButton(window, 300, 250, 50, 50, "Filter")
    monthlyRecapButton = gui.createButton(window, 50, 500, 50, 50, "Month")
    alertsButton = gui.createButton(window, 175, 500, 50, 50, "Alerts")
    graphicsButton = gui.createButton(window, 300, 500, 50, 50, "Graphics")
    lastTransactionsList = gui.createSelectionList(window, 50, 350, 300, 100, ["Transaction 1", "Transaction 2", "Transaction 3", "Transaction 4", "Transaction 5"], True)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            gui.MANAGER.process_events(event)
        gui.MANAGER.update(uiRefreshRate)
        gui.MANAGER.draw_ui(window)
        pygame.display.update()

if __name__ == "__main__":
    userPage()
