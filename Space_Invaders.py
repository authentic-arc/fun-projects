import pygame
import random

pygame.init()

win = pygame.display.set_mode((750, 750))
pygame.display.set_caption("Space Invaders")

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Define constants
BULLET_SPEED = 15
ENEMY_SPEED = 5
ENEMY_DIRECTION = 1

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50, 25])
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.live = 5

    def draw(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([25, 25])
        self.image.fill(white)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += ENEMY_SPEED * ENEMY_DIRECTION

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5, 10])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = x + 22.5  # Center the bullet
        self.rect.y = y

    def update(self):
        self.rect.y -= BULLET_SPEED  # Move bullet upwards


class Bunker(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([8, 8])
        self.image.fill(green)
        self.rect = self.image.get_rect()

ship = Ship()
ship.rect.x = 375
ship.rect.y = 650

enemy_list = pygame.sprite.Group()
bunker_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()  # Group for bullets

# Create enemies
for row in range(1, 6):
    for column in range(1, 11):
        enemy = Enemy()
        enemy.rect.x = 80 + (50 * column)
        enemy.rect.y = 25 + (50 * row)
        enemy_list.add(enemy)

# Create bunkers
for bunk in range(3):
    for row in range(5):
        for column in range(10):
            bunker = Bunker()
            bunker.rect.x = (50 + (275 * bunk)) + (10 * column)
            bunker.rect.y = 500 + (10 * row)
            bunker_list.add(bunker)

def redraw():
    win.fill(black)
    ship.draw()
    enemy_list.draw(win)
    bunker_list.draw(win)
    bullet_list.draw(win)  # Draw bullets
    pygame.display.update()

run = True
while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and ship.rect.x > 0:
        ship.rect.x -= 10
    if key[pygame.K_RIGHT] and ship.rect.x < 700:  # Keep the ship within the screen
        ship.rect.x += 10
    if key[pygame.K_SPACE]:  # Shoot bullet
        bullet = Bullet(ship.rect.x, ship.rect.y)
        bullet_list.add(bullet)

    # Update bullet positions
    bullet_list.update()

    # Update enemy positions
    enemy_list.update()
    
    # Check for bullet collisions with enemies
    for bullet in bullet_list:
        hit_enemies = pygame.sprite.spritecollide(bullet, enemy_list, True)  # Remove enemy on collision
        if hit_enemies:
            bullet_list.remove(bullet)  # Remove bullet on hit

    # Move enemies down when they hit the edge
    for enemy in enemy_list:
        if enemy.rect.x >= 725 or enemy.rect.x <= 0:
            ENEMY_DIRECTION *= -1  # Reverse direction
            for e in enemy_list:
                e.rect.y += 10  # Move all enemies down
            break 

    redraw()

pygame.quit()
