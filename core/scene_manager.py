import pygame


class SceneManager:
    def __init__(self, screen):
        from scenes.main_menu_scene import MainMenuScene
        self.current_scene = MainMenuScene(screen, self)

    def change_scene(self, new_scene):
        self.current_scene = new_scene

    def handle_events(self):
        events = pygame.event.get()
        self.current_scene.handle_events(events)

    def update(self, dt):
        self.current_scene.update(dt)

    def draw(self):
        self.current_scene.draw()
