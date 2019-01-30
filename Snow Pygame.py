import pygame, random, math

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

pygame.init()

size = (640,480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("snow")

class snow(pygame.sprite.Sprite):
    def __init__(self, color, width, height, speed):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(0, 400)
        self.speed = speed

    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y > 480:
            self.rect.y = 0
done = False

snow_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()

number_of_flakes = 50
for x in range (number_of_flakes):
    snow_size = 4
    snow_speed = 1
    my_snow = snow(WHITE, snow_size, snow_size, snow_speed)
    snow_group.add(my_snow)
    all_sprites_group.add(my_snow)
    
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    all_sprites_group.update()
    screen.fill(BLACK)
    all_sprites_group.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
