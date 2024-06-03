import pygame
import button

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 70)
pygame.display.set_caption("TicTacTwisted")

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 600
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
title_screen = pygame.display.set_mode(size)

# screen 1
main_menu_message = "- Main Menu - "
main_menu = my_font.render(main_menu_message, True, (251, 172, 193))
start_img = pygame.image.load('start.png')
start_img = pygame.transform.scale(start_img, (200, 100))
exit_img = pygame.image.load('exit.png')
exit_img = pygame.transform.scale(exit_img, (200, 100))

start_button = button.Button(50, 210, start_img)
exit_button = button.Button(350, 210, exit_img)

# screen 2
directions_message = ("You will need two players for this game. In this game of TicTacToe, players are able to put "
                      "down and take away. The goal is to get 3 in a row no matter the character.")
directions = my_font.render(directions_message, True, (251, 172, 193))

# screen 3
board = pygame.image.load('board.JPG')
board_img = pygame.transform.scale(board, (600, 500))

run = True
markers = []
clicked = False
pos = []
player = 1
x_pos = 0
y_pos = 0

# -------- Main Program Loop -----------

def tic_tac_toe_screen():
    running = True
    while running:
        screen.fill((255, 220, 228))
        screen.blit(board_img, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

while run:
    screen.fill((255, 220, 228))
    screen.blit(main_menu, (70, 70))

    if start_button.draw(screen):
        print("START")
        tic_tac_toe_screen()

    if exit_button.draw(screen):
        print("EXIT")
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            cell_x = pos[0]
            cell_y = pos[1]
            if markers[cell_x // 100][cell_y // 100] == 0:
                markers[cell_x// 100][cell_y // 100] = player
                player *= -1



    pygame.display.update()

for x in range(3):
    row = [0] * 3
    markers.append(row)
print(markers)


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

screen.fill((r, g, b))
screen.blit(board, (100, 100))
pygame.display.update()
