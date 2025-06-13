import pygame
from core import settings
from core.scene_manager import SceneManager


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption(settings.TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.scene_manager = SceneManager(self.screen)

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("assets/sounds/background_music.mp3")
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)

    def run(self):
        while self.running:
            dt = self.clock.tick(settings.FPS) / 1000
            self.scene_manager.handle_events()
            self.scene_manager.update(dt)
            self.scene_manager.draw()
            pygame.display.flip()
