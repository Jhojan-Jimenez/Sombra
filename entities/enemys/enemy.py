import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, color=(255, 0, 0), size=(30, 30)):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)
        self.max_health = 100
        self.health = self.max_health
        self.speed = 100
        self.pos = pygame.math.Vector2(self.rect.topleft)

    def move_towards_player(self, player, dt, others):
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        dist = max((dx**2 + dy**2) ** 0.5, 1)

        move_x = (dx / dist) * self.speed * dt
        move_y = (dy / dist) * self.speed * dt

        self.rect.x += move_x

        if self.rect.colliderect(player.rect) or any(self.rect.colliderect(o.rect) for o in others if o != self):
            self.rect.x -= move_x

        self.rect.y += move_y

        if self.rect.colliderect(player.rect) or any(self.rect.colliderect(o.rect) for o in others if o != self):
            self.rect.y -= move_y

    def draw_health_bar(self, surface):
        unit_health = 10
        min_unit_width = 6
        bar_height = 6

        total_units = self.max_health // unit_health
        filled_units = int(self.health // unit_health)

        bar_width = total_units * min_unit_width
        x = self.rect.centerx - bar_width // 2
        y = self.rect.top - 10

        for i in range(total_units):
            unit_x = x + i * min_unit_width
            unit_color = (0, 255, 0) if i < filled_units else (60, 60, 60)
            pygame.draw.rect(surface, unit_color,
                             (unit_x, y, min_unit_width, bar_height))
            pygame.draw.rect(surface, (255, 255, 255), (unit_x, y,
                                                        min_unit_width, bar_height), 1)

    def stay_in_bounds(self):
        screen_width = 800
        screen_height = 600
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, screen_width)
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, screen_height)
