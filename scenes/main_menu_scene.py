import pygame
import sys
from core import settings
from scenes.game_scene import GameScene


class MainMenuScene:
    def __init__(self, screen, scene_manager):
        self.screen = screen
        self.scene_manager = scene_manager
        self.font = pygame.font.SysFont(None, 48)
        self.play_button = pygame.Rect(300, 220, 200, 60)
        self.exit_button = pygame.Rect(300, 320, 200, 60)

    def draw_button(self, text, rect, hovered):
        color = (100, 100, 255) if hovered else (50, 50, 200)
        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, (255, 255, 255), rect, 3)
        txt_surface = self.font.render(text, True, (255, 255, 255))
        txt_rect = txt_surface.get_rect(center=rect.center)
        self.screen.blit(txt_surface, txt_rect)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if self.play_button.collidepoint(mouse_pos):
                    self.scene_manager.change_scene(
                        GameScene(self.screen, self.scene_manager))
                elif self.exit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

    def update(self, dt):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        mouse_pos = pygame.mouse.get_pos()
        self.draw_button("Jugar", self.play_button,
                         self.play_button.collidepoint(mouse_pos))
        self.draw_button("Salir", self.exit_button,
                         self.exit_button.collidepoint(mouse_pos))
