import pygame


class Start:

    def __init__(self, x, y):
        self.image = pygame.image.load("start.png")
        self.rect = self.image.get_rect()
        self.rect.top_left = (x,y)


    def draw(self):


