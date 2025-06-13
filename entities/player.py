import math
import pygame
from core.settings import SCREEN_HEIGHT, SCREEN_WIDTH


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        original_image = pygame.image.load("assets/player.png").convert_alpha()
        self.image_right = pygame.transform.scale(original_image, (64, 64))
        self.image_left = pygame.transform.flip(self.image_right, True, False)

        self.image = self.image_right

        self.rect = self.image.get_rect(center=pos)
        self.speed = 150
        self.health = 100
        self.max_health = 100

    def update(self, keys, dt, enemies=None):
        if enemies is None:
            enemies = []

        dx, dy = 0, 0
        speed = 150

        if keys[pygame.K_w]:
            dy -= speed * dt
        if keys[pygame.K_s]:
            dy += speed * dt
        if keys[pygame.K_a]:
            self.image = self.image_left
            self.rect.x -= self.speed * dt
            dx -= speed * dt
        if keys[pygame.K_d]:
            self.image = self.image_right
            self.rect.x += self.speed * dt
            dx += speed * dt

        self.rect.x += int(dx)

        self.rect.y += int(dy)
        self.rect.clamp_ip(pygame.Rect(
            30, 20, SCREEN_WIDTH-60, SCREEN_HEIGHT-40))

        keys = pygame.key.get_pressed()

    def draw_health_bar(self, surface):
        bar_width = 120
        bar_height = 18
        x = 10
        y = 10
        fill = int((self.health / self.max_health) * bar_width)

        pygame.draw.rect(surface, (255, 0, 0), (x, y, bar_width, bar_height))
        pygame.draw.rect(surface, (0, 255, 0), (x, y, fill, bar_height))
        pygame.draw.rect(surface, (255, 255, 255),
                         (x, y, bar_width, bar_height), 1)


class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos, target, damage=10, color=(255, 0, 0), size=(8, 8)):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)

        dx = target[0] - pos[0]
        dy = target[1] - pos[1]
        dist = max(math.hypot(dx, dy), 1)

        speed = 300
        self.velocity = (dx / dist * speed, dy / dist * speed)
        self.damage = damage

    def update(self, dt):
        self.rect.x += int(self.velocity[0] * dt)
        self.rect.y += int(self.velocity[1] * dt)
