import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Button!")

class Button():
    def __init__(self, image, x_pos, y_pos):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

        self.buttonLogin = pygame.image.load("images/button.png")
        self.buttonLogin = pygame.transform.scale(self.buttonLogin, (70, 30))

        self.buttonHover = pygame.image.load("images/buttonHover.png")
        self.buttonHover = pygame.transform.scale(self.buttonHover, (70, 30))

    def update(self):
        screen.blit(self.image, self.rect)

    def checkForInput(self, position):
        if self.rect.collidepoint(position):
            print("Button Press!")

    def changeColor(self, position):
        if self.rect.collidepoint(position):
            self.image = self.buttonHover
        else:
            self.image = self.buttonLogin

window_center_x = screen.get_width() // 2
window_center_y = screen.get_height() // 2
