import pygame
from start import Start
from exit import Exit
import random

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("TicTacTwisted")

# set up variables for the display
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 530
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

r = 50
g = 0
b = 100
clicks = 0 

message = "Welcome to TicTacTwisted!"
display_message = my_font.render(message, True, (255, 255, 255))
display_clicks = my_font.render(str(clicks), True, (255, 255, 255))

s = Start(40, 40)
e = Exit(100, 40)

run = True

# -------- Main Program Loop -----------
## ----- NO BLIT ZONE START ----- ##
while run:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            if s.rect.collidepoint(event.pos):
                x = random.randint(0, 370)
                y = random.randint(0, 270)
                s.x = x
                s.y = y
                s.move(s.x, s.y)
                clicks = clicks + 1


pygame.quit()

##  ----- NO BLIT ZONE END  ----- ##
screen.fill((r, g, b))
screen.blit(display_message, (0, 0))
screen.blit(s.image, s.rect)
pygame.display.update()
screen.blit(display_clicks, (20, 40))
