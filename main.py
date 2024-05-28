import pygame
import time

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("TicTacTwisted")

start_img = pygame.image.load('start.png')
start_img = pygame.transform.scale(start_img, (250, 150))
exit_img = pygame.image.load('exit.png')
exit_img = pygame.transform.scale(exit_img, (300, 140))
class Button():
    def __init__(self, x, y, image):
        self.image =image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print("CLICKED")

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))


# set up variables for the display
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 600
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
title_screen = pygame.display.set_mode(size)

start_button = Button(50, 200, start_img)
exit_button = Button(300, 205, exit_img)

# current_time = time.time()
# start_time = current_time + 10


name = "Collect coins as fast as you can!"
message = "Collision not detected"
r = 50
g = 0
b = 100

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
intro = True
game_over = False
# -------- Main Program Loop -----------
while run:
    screen.fill((245, 195, 194))

    start_button.draw()
    exit_button.draw()

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

screen.fill((r, g, b))
pygame.display.update()