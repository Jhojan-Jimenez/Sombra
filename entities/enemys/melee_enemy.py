import pygame
from .enemy import Enemy


class MeleeEnemy(Enemy):
    def __init__(self, pos):
        super().__init__(pos)

        original_image = pygame.image.load(
            "assets/melee_enemy.png").convert_alpha()
        self.image_right = pygame.transform.scale(original_image, (28, 28))
        self.image_left = pygame.transform.flip(self.image_right, True, False)

        self.image = self.image_right
        self.rect = self.image.get_rect(center=pos)

        self.max_health = 80
        self.health = self.max_health
        self.speed = 100
        self.facing = "right"

    def update(self, player, dt):
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        dist = max((dx**2 + dy**2) ** 0.5, 1)

        move_x = (dx / dist) * self.speed * dt
        move_y = (dy / dist) * self.speed * dt

        if move_x < 0:
            self.image = self.image_left
            self.facing = "left"
        else:
            self.image = self.image_right
            self.facing = "right"

        self.rect.x += move_x
        self.rect.y += move_y
