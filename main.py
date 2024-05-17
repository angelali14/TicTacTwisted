import pygame
from start import Start
import time

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("TicTacTwisted")

# set up variables for the display
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 600
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
title_screen = pygame.display.set_mode(size)

current_time = time.time()
start_time = current_time + 10


name = "Collect coins as fast as you can!"
message = "Collision not detected"
r = 50
g = 0
b = 100

# render the text for later
display_name = my_font.render(name, True, (255, 255, 255))
display_message = my_font.render(message, True, (255, 255, 255))


score = 0
s = Start(100, 100)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
intro = True
game_over = False
# -------- Main Program Loop -----------
while run:
    screen.fill((245, 195, 194))
    s =

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

screen.fill((r, g, b))
screen.blit(display_message, (0, 0))
screen.blit(s.image, s.rect)
pygame.display.update()