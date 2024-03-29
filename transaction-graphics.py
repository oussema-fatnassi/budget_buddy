import pygame
import pygame_gui
import sys
from GUI import GUI

def transactionGraphics():
    gui = GUI()
    window = gui.createWindow("transaction Graphics")
    clock = pygame.time.Clock()
    uiRefreshRate = clock.tick(60) / 10000.0
    gui.createImage(window, 50, 50, 100, 100, "images/logo.png")
    gui.createButton(window, 150, 550, 100, 30, "QUIT")
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            gui.MANAGER.process_events(event)
            
        window.fill(gui.BACKGROUND)
        gui.MANAGER.update(uiRefreshRate)
        gui.createImage(window, 50, 50, 100, 100, "images/Logo.png")  
        gui.MANAGER.draw_ui(window)   
        pygame.display.update()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == gui.button:
                    print("QUIT")

if __name__ == "__main__":
    transactionGraphics()