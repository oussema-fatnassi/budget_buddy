import pygame
import pygame_gui
import sys
from GUI import GUI

def accountCreation():
    gui = GUI()
    window = gui.createWindow()
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    gui.createImage(window, 350, 50, 100, 100, "images/logo.png")
    gui.createLabel(window, 10, 100, 100, 30, "First Name")
    gui.createTextInput(window, 20, 130, 300, 30)
    gui.createLabel(window, 10, 170, 90, 30, "Last Name")
    gui.createTextInput(window, 20, 200, 300, 30)
    gui.createLabel(window, 10, 240, 60, 30, "Email")
    gui.createTextInput(window, 20, 270, 300, 30)
    gui.createLabel(window, 10, 310, 85, 30, "Password")
    gui.createPasswordInput(window, 20, 340, 300, 30)
    gui.set_text_hidden(True)
    gui.createLabel(window, 10, 380, 150, 30, "Confirm Password")
    gui.createPasswordInput(window, 20, 410, 300, 30)
    gui.set_text_hidden(True)
    gui.createButton(window, 150, 500, 100, 30, "LOGIN")
    gui.createButton(window, 150, 550, 100, 30, "REGISTER")


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
    accountCreation()