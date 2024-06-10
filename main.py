import pygame
import button

pygame.mixer.init()
pygame.mixer.music.load('themesong.wav')
pygame.mixer.music.play(loops=-1, start=0)

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 70)
font = pygame.font.SysFont('Comic Sans MS', 20)
pygame.display.set_caption("TicTacTwisted")

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

main_menu_message = "- Main Menu - "
main_menu = my_font.render(main_menu_message, True, (251, 172, 193))

start_img = pygame.image.load('start.png')
start_img = pygame.transform.scale(start_img, (350, 150))
exit_img = pygame.image.load('exit.png')
exit_img = pygame.transform.scale(exit_img, (320, 143))
start_button = button.Button(-30, 190, start_img)
exit_button = button.Button(270, 201, exit_img)

players_img = pygame.image.load('players.png')
players = pygame.transform.scale(players_img, (350, 140))

board = pygame.image.load('board.JPG')
board_img = pygame.transform.scale(board, (600, 600))
x = pygame.image.load('my melody.png')
o = pygame.image.load('cinnamonroll.png')
x_img = pygame.transform.scale(x, (200, 200))
o_img = pygame.transform.scale(o, (200, 200))

replay_img = pygame.image.load('replay.png')
replay_img = pygame.transform.scale(replay_img, (300, 100))
replay = button.Button(150, 250, replay_img)

cell_size = 200  # how big each box is
rows, cols = 3, 3
board_state = [[' ' for _ in range(cols)] for _ in range(rows)]  # creating board
clickable_areas = [pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size) for row in range(rows) for col in range(cols)]

def tic_tac_toe_screen():
    global clickable_area
    clickable_area = True
    running = True
    player = 'X'  # x starts
    player1 = 0
    player2 = 0
    while running:  # beginning of while loop
        screen.blit(board_img, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # game end

            if event.type == pygame.MOUSEBUTTONDOWN:  # starting the game
                for index, area in enumerate(clickable_areas):  # identify which cell is clickable
                    if area.collidepoint(event.pos):  # whether a cell is clicked
                        row, col = index // cols, index % cols  # if mouse click is within area         # 65-67 issue
                        if board_state[row][col] == ' ':  # used to check if this cell is empty
                            board_state[row][col] = player  # if te cell is empty, it will add the players symbol
                            clickable_area = True
                            player = 'O' if player == 'X' else 'X'  # changes turns

        for row in range(rows):  # placing the x and o images (graphic)
            for col in range(cols):
                if board_state[row][col] == 'X':  # used to draw position
                    screen.blit(x_img, (col * cell_size, row * cell_size))
                elif board_state[row][col] == 'O':  # used to draw position
                    screen.blit(o_img, (col * cell_size, row * cell_size))

        for col in board_state:  # for col player 2 win
            if all(index == 'O' for index in col):
                win_msg = my_font.render("Player 2 Wins!", True, (156, 220, 219))
                screen.fill((255, 220, 228))
                replay.draw(screen)
                screen.blit(win_msg, (70, 150))
            # player2 += 1

        for row in board_state:  # for row player 2 win
            if all(index == 'O' for index in row):
                win_msg = my_font.render("Player 2 Wins!", True, (156, 220, 219))
                screen.fill((255, 220, 228))
                replay.draw(screen)
                screen.blit(win_msg, (70, 150))
                # player2 += 1

        for row in board_state:
            if all(index == 'X' for index in row):
                win_msg = my_font.render("Player 1 Wins!", True, (156, 220, 219))
                screen.fill((255, 220, 228))
                replay.draw(screen)
                screen.blit(win_msg, (70, 150))
                # player1 += 1

        for col in board_state:  # for col player 1 win
            if all(index == 'X' for index in col):
                win_msg = my_font.render("Player 1 Wins!", True, (156, 220, 219))
                screen.fill((255, 220, 228))
                replay.draw(screen)
                screen.blit(win_msg, (70, 150))

        if all(all(index != ' ' for index in row) for row in board_state):  # checks if all the rows are full
            for col in board_state:  # for col player 2 win
                if all(index == 'O' for index in col):
                    win_msg = my_font.render("Player 2 Wins!", True, (156, 220, 219))
                    screen.fill((255, 220, 228))
                    replay.draw(screen)
                    screen.blit(win_msg, (70, 150))
                # player2 += 1

            for row in board_state:  # for row player 2 win
                if all(index == 'O' for index in row):
                    win_msg = my_font.render("Player 2 Wins!", True, (156, 220, 219))
                    screen.fill((255, 220, 228))
                    replay.draw(screen)
                    screen.blit(win_msg, (70, 150))
                    # player2 += 1

            for row in board_state:
                if all(index == 'X' for index in row):
                    win_msg = my_font.render("Player 1 Wins!", True, (156, 220, 219))
                    screen.fill((255, 220, 228))
                    replay.draw(screen)
                    screen.blit(win_msg, (70, 150))
                    # player1 += 1

            for col in board_state:  # for col player 1 win
                if all(index == 'X' for index in col):
                    win_msg = my_font.render("Player 1 Wins!", True, (156, 220, 219))
                    screen.fill((255, 220, 228))
                    replay.draw(screen)
                    screen.blit(win_msg, (70, 150))
            tie_msg = my_font.render("Tie!!", True, (156, 220, 219))
            screen.fill((255, 220, 228))                      # tie does not work displays tie when cells are full
            screen.blit(tie_msg, (210, 150))
            replay.draw(screen)
        pygame.display.update()

        if all(all(index != ' ' for index in col) for col in board_state):  # checks if all the cols are full
            tie_msg = my_font.render("Tie!!", True, (156, 220, 219))
            screen.fill((255, 220, 228))
            screen.blit(tie_msg, (210, 150))
            replay.draw(screen)
        pygame.display.update()
def main_screen():
    screen.fill((255, 220, 228))
    screen.blit(main_menu, (70, 70))
    screen.blit(players, (100, 430))

    if start_button.draw(screen):
        tic_tac_toe_screen()

    if exit_button.draw(screen):
        pygame.quit()
    pygame.display.update()

run = True
while run:
    main_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if replay.draw(screen):
                screen.blit(board_img, (0, 0))
            pygame.display.update()

pygame.quit()
