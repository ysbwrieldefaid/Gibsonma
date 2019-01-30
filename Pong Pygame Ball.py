import pygame

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
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

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, (x_val, y_val, width_of_ball, 20))
    x_val = x_val + x_direction
    y_val = y_val + y_direction
    if x_val == 630 or x_val == 0:
        x_direction = -x_direction
    if y_val == 470 or y_val == 0:
        y_direction = -y_direction

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
