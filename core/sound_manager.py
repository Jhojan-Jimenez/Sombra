import pygame


class SoundManager:
    def __init__(self):
        self.shoot = pygame.mixer.Sound("assets/sounds/shoot.mp3")

        self.shoot.set_volume(0.5)

    def play_shoot(self):
        self.shoot.play()
