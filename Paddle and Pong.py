# SRC - Try to make the ball hit the walls and paddle cleanly,
# ie, so it does not go off the screen or overlap the paddle.

import pygame

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
BLUE = (50,50,255)

size = (640,480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pong game")
width_of_ball = 20
x_val = 150
y_val = 200
x_direction = 1
y_direction = 1
paddle_length = 15
paddle_width = 60
x_padd = 0
y_padd = 20

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y_padd >= 0:
        y_padd = y_padd - 5
    elif keys[pygame.K_s] and y_padd <= 420:
        y_padd = y_padd + 5


    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, (x_val, y_val, 20, width_of_ball))
    x_val = x_val + x_direction
    y_val = y_val + y_direction
    if x_val == 630 or x_val == 0:
        x_direction = -x_direction
    if y_val == 470 or y_val == 0:
        y_direction = -y_direction

    pygame.draw.rect(screen, WHITE, (x_padd, y_padd, paddle_length, paddle_width))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
