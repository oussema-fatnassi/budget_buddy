import pygame
import pygame_gui
import sys

class GUI:
    def __init__(self):                                                                # Constructor to initialize the window object          
        self.windowWidth = 400
        self.windowHeight = 600
        self.BACKGROUND = (234, 234, 234)
        self.BUTTON = (0, 171, 179)
        self.TEXT = (60, 64, 72)
        clock = pygame.time.Clock()
        self.uiRefreshRate = clock.tick(60)/10000.0
        self.MANAGER = None  
        self.textInput = None  

    def createWindow(self):                                                          # createWindow method to create the window     
        pygame.init()
        pygame.display.set_caption("Window")
        window = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        window.fill(self.BACKGROUND)
        self.MANAGER = pygame_gui.UIManager((self.windowWidth, self.windowHeight))  

        return window

    def createTextInput(self, window, pos_x, pos_y, width, height):  
        self.textInput = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((pos_x, pos_y), (width, height)), manager=self.MANAGER, object_id="text_input")


    def main(self):                                                                  # run method to run the window
        window = self.createWindow()
        self.createTextInput(window, 50, 300, 300, 30)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.MANAGER.process_events(event)

            self.MANAGER.update(self.uiRefreshRate)
            self.MANAGER.draw_ui(window)
            pygame.display.update()

if __name__ == "__main__":
    window = GUI()
    window.main()
