import pygame
import random
from core.sound_manager import SoundManager
from entities.player import Player, Projectile
from entities.enemys.melee_enemy import MeleeEnemy
from entities.enemys.ranged_enemy import RangedEnemy
from core.settings import SCREEN_HEIGHT, SCREEN_WIDTH
from entities.enemys.boss_enemy import BossEnemy


class GameScene:
    def __init__(self, screen, scene_manager):
        self.screen = screen
        self.scene_manager = scene_manager
        self.sound_manager = SoundManager()

        self.background = pygame.image.load(
            "assets/scenes/game_background.png").convert()
        self.background = pygame.transform.scale(
            self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.player = Player((70, 70))
        self.all_sprites = pygame.sprite.Group(self.player)
        self.enemies = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.player_projectiles = pygame.sprite.Group()
        self.q_cooldown = 0
        self.e_cooldown = 0
        self.q_max_cooldown = 5
        self.e_max_cooldown = 60
        self.wave = 1
        self.score = 0
        self.show_wave_timer = 2
        self.wave_label_font = pygame.font.SysFont(None, 64)

        self.spawn_wave()

    def spawn_wave(self):
        self.enemies.empty()
        attempts = 0
        max_enemies = self.wave + 1

        if self.wave % 5 == 0:
            boss = BossEnemy((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.enemies.add(boss)
            self.all_sprites.add(boss)
            return

        while len(self.enemies) < max_enemies and attempts < 1000:
            attempts += 1
            x = random.randint(100, SCREEN_WIDTH - 100)
            y = random.randint(100, SCREEN_HEIGHT - 100)
            new_enemy = MeleeEnemy((x, y)) if random.choice(
                [True, False]) else RangedEnemy((x, y))

            if new_enemy.rect.colliderect(self.player.rect):
                continue

            if any(new_enemy.rect.colliderect(e.rect) for e in self.enemies):
                continue

            self.enemies.add(new_enemy)
            self.all_sprites.add(new_enemy)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                from scenes.pause_menu_scene import PauseMenuScene
                self.scene_manager.change_scene(PauseMenuScene(
                    self.screen, self.scene_manager, self))
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.sound_manager.play_shoot()
                mouse_pos = pygame.mouse.get_pos()
                projectile = Projectile(
                    pos=self.player.rect.center,
                    target=mouse_pos,
                    damage=10,
                    color=(0, 255, 255)
                )
                self.player_projectiles.add(projectile)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and self.q_cooldown <= 0:
                    mouse_pos = pygame.mouse.get_pos()
                    strong_projectile = Projectile(
                        pos=self.player.rect.center,
                        target=mouse_pos,
                        damage=20,
                        color=(255, 100, 100),
                        size=(16, 16)
                    )
                    self.player_projectiles.add(strong_projectile)
                    self.q_cooldown = self.q_max_cooldown

                elif event.key == pygame.K_e and self.e_cooldown <= 0:
                    self.player.health = min(
                        self.player.max_health, self.player.health + 10)
                    self.e_cooldown = self.e_max_cooldown

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.player.update(keys, dt, list(self.enemies))

        if self.q_cooldown > 0:
            self.q_cooldown -= dt

        if self.e_cooldown > 0:
            self.e_cooldown -= dt

        for enemy in self.enemies:
            if isinstance(enemy, MeleeEnemy):
                enemy.update(self.player, dt)
                if self.player.rect.colliderect(enemy.rect):
                    self.player.health -= 20 * dt
            elif isinstance(enemy, RangedEnemy):
                enemy.update(self.player, dt, self.projectiles)
            elif isinstance(enemy, BossEnemy):
                enemy.update(self.player, dt, self.projectiles)

        self.player_projectiles.update(dt)

        self.projectiles.update(dt)

        for projectile in self.player_projectiles:
            hit_enemies = pygame.sprite.spritecollide(
                projectile, self.enemies, dokill=False)
            for enemy in hit_enemies:
                enemy.health -= projectile.damage
                self.player_projectiles.remove(projectile)
                if enemy.health <= 0:
                    self.enemies.remove(enemy)
                    self.all_sprites.remove(enemy)
                    self.score += 10

        if pygame.sprite.spritecollide(self.player, self.projectiles, dokill=True):
            self.player.health -= 10

        self.player.health = max(0, self.player.health)

        if self.player.health <= 0:
            from scenes.game_over_scene import GameOverScene
            self.scene_manager.change_scene(
                GameOverScene(self.screen, self.scene_manager))

        if len(self.enemies) == 0:
            self.wave += 1
            self.show_wave_timer = 2
            self.spawn_wave()

    def draw(self):

        self.screen.blit(self.background, (0, 0))

        pygame.draw.rect(self.screen, (255, 255, 255),
                         self.screen.get_rect(), 4)

        self.all_sprites.draw(self.screen)
        self.projectiles.draw(self.screen)
        self.player_projectiles.draw(self.screen)
        self.player.draw_health_bar(self.screen)

        self.draw_ability_icon("Q", 20, SCREEN_HEIGHT - 70,
                               self.q_cooldown, self.q_max_cooldown)
        self.draw_ability_icon("E", 80, SCREEN_HEIGHT - 70,
                               self.e_cooldown, self.e_max_cooldown)

        for enemy in self.enemies:
            enemy.draw_health_bar(self.screen)

    def draw_ability_icon(self, key, x, y, cooldown, max_cooldown):

        rect = pygame.Rect(x, y, 50, 50)
        pygame.draw.rect(self.screen, (30, 30, 30), rect)
        pygame.draw.rect(self.screen, (255, 255, 255), rect, 2)

        font = pygame.font.SysFont(None, 36)
        text = font.render(key, True, (255, 255, 255))
        self.screen.blit(text, text.get_rect(center=rect.center))

        if cooldown > 0:
            cooldown_height = int(50 * (cooldown / max_cooldown))
            overlay = pygame.Surface((50, cooldown_height))
            overlay.set_alpha(150)
            overlay.fill((0, 0, 0))
            self.screen.blit(overlay, (x, y + 50 - cooldown_height))

            font_small = pygame.font.SysFont(None, 20)
            cd_text = font_small.render(
                f"{int(cooldown)+1}", True, (255, 100, 100))
            self.screen.blit(cd_text, cd_text.get_rect(
                center=(x + 25, y + 25)))

        if self.show_wave_timer > 0:
            wave_text = self.wave_label_font.render(
                f"Oleada {self.wave}", True, (255, 255, 255))
            self.screen.blit(wave_text, wave_text.get_rect(
                center=(SCREEN_WIDTH // 2, 50)))
            self.show_wave_timer -= 1 / 60

        score_font = pygame.font.SysFont(None, 36)
        score_text = score_font.render(
            f"Puntos: {self.score}", True, (255, 255, 0))
        self.screen.blit(score_text, (SCREEN_WIDTH - 150, 20))
