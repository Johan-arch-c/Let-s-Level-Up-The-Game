import pygame
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom Event - Change Sprite Colours")

clock = pygame.time.Clock()

# --- Custom Event ---
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 1000)  # every 1 second

# --- Sprite Class ---
class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((80, 80))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(x, y))

    def change_color(self):
        # pick a random new RGB color
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        self.image.fill(self.color)

# Create two sprites
sprite1 = ColorSprite(200, 200, (255, 0, 0))
sprite2 = ColorSprite(400, 200, (0, 0, 255))

all_sprites = pygame.sprite.Group(sprite1, sprite2)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Custom event triggers colour change
        if event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    screen.fill((30, 30, 30))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
