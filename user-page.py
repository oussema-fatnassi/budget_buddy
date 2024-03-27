import pygame
import pygame_gui
import sys
from GUI import GUI

def userPage():
    gui = GUI()
    window = gui.createWindow("User Page")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    gui.createImage(window, 200, 100, 100, 100, "images/logo.png")
    gui.createTextBox(window, 125, 200, 150, 50, "100000000 €")
    # gui.createLabel(window, 20, 250, 100, 30, "Email")
    # gui.createTextInput(window, 50, 300, 300, 30)
    # gui.createLabel(window, 30, 350, 100, 30, "Password")
    # gui.createPasswordInput(window, 50, 400, 300, 30)
    # gui.set_text_hidden(True)
    # gui.createButton(window, 150, 500, 100, 30, "LOGIN")
    # gui.createButton(window, 150, 550, 100, 30, "REGISTER")


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