import pygame
import button

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("TicTacTwisted")

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 600
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
title_screen = pygame.display.set_mode(size)

start_img = pygame.image.load('start.png')
start_img = pygame.transform.scale(start_img, (250, 150))
exit_img = pygame.image.load('exit.png')
exit_img = pygame.transform.scale(exit_img, (300, 140))

start_button = button.Button(30, 200, start_img)
exit_button = button.Button(290, 205, exit_img)

r = 50
g = 0
b = 100

run = True
# -------- Main Program Loop -----------
while run:
    screen.fill((245, 195, 194))

    if start_button.draw(screen):
        print("START")

    if exit_button.draw(screen):
        print("EXIT")
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

screen.fill((r, g, b))
pygame.display.update()