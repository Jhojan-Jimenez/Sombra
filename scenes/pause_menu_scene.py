import pygame
from scenes.game_scene import GameScene
from scenes.main_menu_scene import MainMenuScene


class PauseMenuScene:
    def __init__(self, screen, scene_manager, game_scene):
        self.screen = screen
        self.scene_manager = scene_manager
        self.game_scene = game_scene
        self.font = pygame.font.SysFont(None, 48)
        self.continue_button = pygame.Rect(300, 200, 200, 60)
        self.restart_button = pygame.Rect(300, 280, 200, 60)
        self.exit_button = pygame.Rect(300, 360, 200, 60)

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
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if self.continue_button.collidepoint(mouse_pos):
                    self.scene_manager.change_scene(self.game_scene)
                elif self.restart_button.collidepoint(mouse_pos):
                    self.scene_manager.change_scene(
                        GameScene(self.screen, self.scene_manager))
                elif self.exit_button.collidepoint(mouse_pos):
                    from scenes.main_menu_scene import MainMenuScene
                    self.scene_manager.change_scene(
                        MainMenuScene(self.screen, self.scene_manager))

    def update(self, dt):
        pass

    def draw(self):
        self.screen.fill((20, 20, 20))
        mouse_pos = pygame.mouse.get_pos()
        self.draw_button("Continuar", self.continue_button,
                         self.continue_button.collidepoint(mouse_pos))
        self.draw_button("Reiniciar", self.restart_button,
                         self.restart_button.collidepoint(mouse_pos))
        self.draw_button("Salir", self.exit_button,
                         self.exit_button.collidepoint(mouse_pos))
