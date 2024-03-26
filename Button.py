import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Button!")
main_font = pygame.font.SysFont("cambria", 50)

class Button():
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, (60, 74, 62))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.button = pygame.image.load("images/button.png")
        self.buttonHover = pygame.image.load("images/buttonHover.png")

    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if self.rect.collidepoint(position):
            print("Button Press!")

    def changeColor(self, position):
        if self.rect.collidepoint(position):
            self.text = main_font.render(self.text_input, True, (78, 178, 178))
            self.image = self.buttonHover
        else:
            self.text = main_font.render(self.text_input, True, (60, 74, 72))
            self.image = self.button

button = Button(pygame.image.load("images/button.png"), 400, 300, "Button")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            button.checkForInput(pygame.mouse.get_pos())

    screen.fill((255, 255, 255))

    button.update()
    button.changeColor(pygame.mouse.get_pos())

    pygame.display.update()
