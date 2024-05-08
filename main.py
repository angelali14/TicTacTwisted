import pygame

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Welcome to TicTacTwisted")

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
title_screen = pygame.display.set_mode(size)

r = 50
g = 0
b = 100

run = True
is_player1_turn = True
is_player2_turn = False

message = "Click an Option to Start!"
option1 = "| play with bot |"
option2 = "| play with friends |"
display_message = my_font.render(message, True, (255, 255, 255))
display_option1 = my_font.render(option1, True, (255, 255, 255))
display_option2 = my_font.render(option2, True, (255, 255, 255))

# -------- Main Program Loop -----------
## ----- NO BLIT ZONE START ----- ##
while run:


##  ----- NO BLIT ZONE END  ----- ##

screen.fill((r, g, b))
screen.blit(display_message, (0, 0))
