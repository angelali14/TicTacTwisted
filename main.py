import pygame
import button

pygame.mixer.init()
pygame.mixer.music.load('themesong.wav')
pygame.mixer.music.play(loops=-1, start=0)

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 70)
font = pygame.font.SysFont('Comic Sans MS', 30)
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
replay_button = button.Button(150, 250, replay_img)

cell_size = 200
rows, cols = 3, 3
player1 = 0
player2 = 0


def reset_game():
    global board_state, winner, tie, score_updated
    board_state = [[' ' for _ in range(cols)] for _ in range(rows)]  # creating board
    winner = None
    tie = False
    score_updated = False


reset_game()
clickable_areas = [pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size) for row in range(rows) for col in
                   range(cols)]
clickable_area = True


def tic_tac_toe_screen():
    global clickable_area, winner, tie, player1, player2, score_updated
    running = True
    player = 'X'

    while running:
        screen.blit(board_img, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # game end
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:  # starting the game
                if clickable_area:   # identify which cell is clickable
                    for index, area in enumerate(clickable_areas):  # whether a cell is clicked
                        if area.collidepoint(event.pos):  # if mouse click is within area
                            row, col = index // cols, index % cols  # used to check if this cell is empty
                            if board_state[row][col] == ' ':  # if the cell is empty, it will add the players symbol
                                board_state[row][col] = player
                                player = 'O' if player == 'X' else 'X'   # changes turns
                                check_win()
                                if winner or tie:
                                    clickable_area = False

        for row in range(rows):  # placing the x and o images
            for col in range(cols):
                if board_state[row][col] == 'X':   # used to draw position
                    screen.blit(x_img, (col * cell_size, row * cell_size))
                elif board_state[row][col] == 'O':  # used to draw position
                    screen.blit(o_img, (col * cell_size, row * cell_size))

        if winner or tie:
            if not score_updated:
                if winner == 'X':
                    player1 = player1 + 1
                elif winner == 'O':
                    player2 = player2 + 1

                score_updated = True
            status()
            if replay_button.draw(screen):
                reset_game()
                clickable_area = True
                tic_tac_toe_screen()
                running = True

        display_scores()
        pygame.display.update()


def display_scores():
    player1_score_text = font.render("Player 1 Score: " + str(player1), True, (114, 181, 180))
    player2_score_text = font.render("Player 2 Score: " + str(player2), True, (114, 181, 180))
    screen.blit(player1_score_text, (10, 10))
    screen.blit(player2_score_text, (10, 50))


def status():
    global tie
    if winner == 'X':
        screen.fill((255, 220, 228))
        winner_msg = my_font.render("Player 1 WON!", True, (156, 220, 219))
        screen.blit(winner_msg, (100, 100))

    if winner == 'O':
        screen.fill((255, 220, 228))
        winner_msg = my_font.render("Player 2 WON!", True, (156, 220, 219))
        screen.blit(winner_msg, (100, 100))

    if tie:
        screen.fill((255, 220, 228))
        draw_msg = my_font.render("Game Draw!", True, (156, 220, 219))
        screen.blit(draw_msg, (100, 100))


def check_win():
    global winner, tie

    for row in range(3):
        if board_state[row][0] == board_state[row][1] == board_state[row][2] and board_state[row][0] != ' ':
            winner = board_state[row][0]
            break

    for col in range(3):
        if board_state[0][col] == board_state[1][col] == board_state[2][col] and board_state[0][col] != ' ':
            winner = board_state[0][col]
            break

    if board_state[0][0] == board_state[1][1] == board_state[2][2] and board_state[0][0] != ' ':
        winner = board_state[0][0]

    if board_state[0][2] == board_state[1][1] == board_state[2][0] and board_state[0][2] != ' ':
        winner = board_state[0][2]

    if all(all(cell != ' ' for cell in row) for row in board_state) and winner is None:
        tie = True


def main_screen():
    screen.fill((255, 220, 228))
    screen.blit(main_menu, (70, 70))
    screen.blit(players, (100, 430))

    if start_button.draw(screen):
        tic_tac_toe_screen()

    if exit_button.draw(screen):
        pygame.quit()
        exit()

    pygame.display.update()


run = True
while run:
    main_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
