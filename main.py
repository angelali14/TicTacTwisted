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
is_player1_turn = True
is_player2_turn = False

message = "Click an Option to Start!"

display_message = my_font.render(message, True, (255, 255, 255))


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
screen.blit(display_message, (0, 0))
