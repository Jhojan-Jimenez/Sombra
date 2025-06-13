import pygame
import sys
from core import settings
from scenes.game_scene import GameScene
from scenes.main_menu_scene import MainMenuScene


class GameOverScene:
    def __init__(self, screen, scene_manager):
        self.screen = screen
        self.scene_manager = scene_manager
        self.font = pygame.font.SysFont(None, 64)
        self.button_font = pygame.font.SysFont(None, 40)

        self.restart_button = pygame.Rect(300, 300, 200, 60)
        self.exit_button = pygame.Rect(300, 380, 200, 60)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if self.restart_button.collidepoint(mouse_pos):
                    self.scene_manager.change_scene(
                        GameScene(self.screen, self.scene_manager))
                elif self.exit_button.collidepoint(mouse_pos):
                    self.scene_manager.change_scene(
                        MainMenuScene(self.screen, self.scene_manager))

    def update(self, dt):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))

        title = self.font.render("¡Has muerto!", True, (255, 0, 0))
        self.screen.blit(title, title.get_rect(
            center=(settings.SCREEN_WIDTH // 2, 180)))

        self.draw_button("Reiniciar", self.restart_button)
        self.draw_button("Salir", self.exit_button)

    def draw_button(self, text, rect):
        pygame.draw.rect(self.screen, (50, 50, 200), rect)
        pygame.draw.rect(self.screen, (255, 255, 255), rect, 2)
        txt_surface = self.button_font.render(text, True, (255, 255, 255))
        self.screen.blit(txt_surface, txt_surface.get_rect(center=rect.center))
