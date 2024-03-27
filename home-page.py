import pygame
import pygame_gui
import sys
from GUI import GUI

def homePage():
    
    gui = GUI()
    window = gui.createWindow()
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    gui.createImage(window, 200, 175, 300, 300, "images/logo.png")
    gui.createButton(window, 100, 500, 200, 30, "LOGIN")
    gui.createButton(window, 100, 550, 200, 30, "CREATE NEW ACCOUNT")
    
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
    homePage()