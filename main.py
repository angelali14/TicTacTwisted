import pygame
import button

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 70)
pygame.display.set_caption("TicTacTwisted")

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

main_menu_message = "- Main Menu - "
main_menu = my_font.render(main_menu_message, True, (251, 172, 193))
start_img = pygame.image.load('start.png')
start_img = pygame.transform.scale(start_img, (200, 100))
exit_img = pygame.image.load('exit.png')
exit_img = pygame.transform.scale(exit_img, (200, 100))

start_button = button.Button(50, 210, start_img)
exit_button = button.Button(350, 210, exit_img)

board = pygame.image.load('board.JPG')
board_img = pygame.transform.scale(board, (600, 600))
x = pygame.image.load('my melody.png')
o = pygame.image.load('cinnamonroll.png')
x_img = pygame.transform.scale(x, (200, 200))
o_img = pygame.transform.scale(o, (200, 200))

run = True
cell_size = 200 # how big each box is
rows, cols = 3, 3

board_state = [[' ' for _ in range(cols)] for _ in range(rows)]

# calculating clickable areas
clickable_areas = []
for row in range(rows):
    for col in range(cols):
        clickable_areas.append(pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size))

def tic_tac_toe_screen():
    running = True
    player = 'X'  # start with X

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for index, area in enumerate(clickable_areas):   # identify which cell is clickable

                    if area.collidepoint(event.pos):  # whether a cell is clicked
                        row, col = index // cols, index % cols  # if mouse click is within area

                        if board_state[row][col] == ' ':  # used to check if this cell is empty
                            board_state[row][col] = player
                            player = 'O' if player == 'X' else 'X'  # change symbols

        screen.blit(board_img, (0, 0))

        for row in range(rows):
            for col in range(cols):
                if board_state[row][col] == 'X': # used to draw position
                    screen.blit(x_img, (col * cell_size, row * cell_size))
                elif board_state[row][col] == 'O':  # used to draw position
                    screen.blit(o_img, (col * cell_size, row * cell_size))

        pygame.display.update()

    pygame.quit()

while run:
    screen.fill((255, 220, 228))
    screen.blit(main_menu, (70, 70))

    if start_button.draw(screen):  # if start is clicked
        tic_tac_toe_screen()

    if exit_button.draw(screen):  # if exit is clicked
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

