import pygame
import math
import random
from .ranged_enemy import EnemyProjectile
from .enemy import Enemy


class BossEnemy(Enemy):
    def __init__(self, pos):
        super().__init__(pos)

        self.image = pygame.image.load(
            "assets/boss.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))

        self.rect = self.image.get_rect(center=pos)
        self.max_health = 500
        self.health = self.max_health
        self.speed = 60

        self.attack_timer = 0
        self.rush_cooldown = 5
        self.radial_cooldown = 3
        self.targeted_cooldown = 1.5

        self.time_since_last_rush = 0
        self.time_since_last_radial = 0
        self.time_since_last_targeted = 0

    def update(self, player, dt, projectiles_group):
        self.attack_timer += dt
        self.time_since_last_rush += dt
        self.time_since_last_radial += dt
        self.time_since_last_targeted += dt

        distance_to_player = pygame.math.Vector2(
            player.rect.center).distance_to(self.rect.center)

        if distance_to_player > 100:
            self.move_towards_player(player, dt, [])

        if self.time_since_last_radial >= self.radial_cooldown:
            self.radial_attack(projectiles_group)
            self.time_since_last_radial = 0

        if self.time_since_last_targeted >= self.targeted_cooldown:
            self.shoot_targeted(player, projectiles_group)
            self.time_since_last_targeted = 0

        if distance_to_player < 100 and self.time_since_last_rush >= self.rush_cooldown:
            self.rush_attack(player, dt)
            self.time_since_last_rush = 0

        self.stay_in_bounds()

    def radial_attack(self, group):
        """Dispara en todas direcciones"""
        num_projectiles = 12
        angle_step = 2 * math.pi / num_projectiles
        for i in range(num_projectiles):
            angle = i * angle_step
            dx = math.cos(angle)
            dy = math.sin(angle)
            target = (self.rect.centerx + dx * 100,
                      self.rect.centery + dy * 100)
            p = EnemyProjectile(self.rect.center, target)
            group.add(p)

    def shoot_targeted(self, player, group):
        """Dispara una bala al jugador"""
        p = EnemyProjectile(self.rect.center, player.rect.center,
                            damage=15, color=(255, 100, 0))
        group.add(p)

    def rush_attack(self, player, dt):
        """Empuja rápidamente al jugador si está cerca"""
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        dist = max(math.hypot(dx, dy), 1)
        strength = 300
        self.rect.x += int((dx / dist) * strength * dt)
        self.rect.y += int((dy / dist) * strength * dt)
