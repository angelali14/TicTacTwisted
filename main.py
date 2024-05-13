import pygame

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Welcome to TicTacTwisted")

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

r = 255
g = 182
b = 193

run = True

start_img = pygame.image.load('start.png').convert_alpha()
exit_img = pygame.image.load('exit.png').convert_alpha()


# -------- Main Program Loop -----------
## ----- NO BLIT ZONE START ----- ##
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
    pygame.display.update()

pygame.quit()


##  ----- NO BLIT ZONE END  ----- ##
screen.fill((r, g, b))
