import pygame
import math
from .enemy import Enemy


class RangedEnemy(Enemy):
    def __init__(self, pos):
        super().__init__(pos, color=(0, 0, 255), size=(28, 28))
        self.image = pygame.image.load(
            "assets/range_enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (48, 48))

        self.rect = self.image.get_rect(center=pos)
        self.max_health = 40
        self.health = self.max_health
        self.cooldown = 1.5
        self.timer = 0
        self.speed = 80

    def update(self, player, dt, projectiles):
        self.timer -= dt

        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        distance = math.hypot(dx, dy)

        if distance < 150:
            self.rect.x -= int(dx / distance * self.speed * dt)
            self.rect.y -= int(dy / distance * self.speed * dt)

        if self.timer <= 0 and distance < 300:
            self.timer = self.cooldown
            projectile = EnemyProjectile(self.rect.center, player.rect.center)
            projectiles.add(projectile)

        self.stay_in_bounds()


class EnemyProjectile(pygame.sprite.Sprite):
    def __init__(self, pos, target, damage=10, color=(255, 0, 0)):
        super().__init__()
        self.image = pygame.Surface((8, 8))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)

        dx = target[0] - pos[0]
        dy = target[1] - pos[1]
        dist = max(math.hypot(dx, dy), 1)

        speed = 300
        self.velocity = (dx / dist * speed, dy / dist * speed)
        self.damage = damage

        self.pos = list(pos)

    def update(self, dt):
        self.pos[0] += self.velocity[0] * dt
        self.pos[1] += self.velocity[1] * dt
        self.rect.center = (int(self.pos[0]), int(self.pos[1]))
