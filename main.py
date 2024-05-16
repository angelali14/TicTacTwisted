import pygame
from start import Start
import time

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("TicTacTwisted")

# set up variables for the display
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 530
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


s = Start(200, 85)
score = 0

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
intro = True
game_over = False
# -------- Main Program Loop -----------
while run:

    if intro == True:
       message1 = my_font.render("Use ASDW to move.", True, (255, 255, 255))
       message2 = my_font.render("You have 10 seconds to reach 100 points!", True, (255, 255, 255))
       message3 = my_font.render("Click anywhere on the screen to begin", True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
           intro = False

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    current_time = time.time()
    current_time = current_time - start_time
    current_time = round(current_time, 2)
    time_left = my_font.render("Time Remaining: " + str(abs(current_time)), True,  (255, 255, 255))

    screen.fill((r, g, b))
    if intro == True:
        screen.blit(message1, (100, 120))
        screen.blit(message2, (100, 150))
        screen.blit(message3, (100, 180))

    if intro == False:
       score_message = my_font.render("Score: " + str(score), True, (255, 255, 255))
       screen.blit(score_message, (0, 15))
       screen.blit(display_name, (0, 0))
       screen.blit(time_left, (0, 30))

    if game_over == True:
        screen.fill((r, g, b))
        if score == 100:
           screen.blit(game_over_message, (200, 200))
        else:
            screen.blit(lose_game_over, (200, 200))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
