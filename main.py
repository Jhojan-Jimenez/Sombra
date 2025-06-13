from core.game import Game
from core.settings import LIGHT_BLUE, DARK_BLUE, WHITE, BLACK

if __name__ == "__main__":
    game = Game()
    game.run()


import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Menú Principal")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)


def draw_button(text, rect, hovered):
    color = LIGHT_BLUE if hovered else DARK_BLUE
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, WHITE, rect, 3)
    txt_surface = font.render(text, True, WHITE)
    txt_rect = txt_surface.get_rect(center=rect.center)
    screen.blit(txt_surface, txt_rect)


def menu_loop():
    play_button = pygame.Rect(300, 200, 200, 60)
    exit_button = pygame.Rect(300, 300, 200, 60)

    while True:
        screen.fill(BLACK)
        mouse_pos = pygame.mouse.get_pos()

        draw_button("Jugar", play_button, play_button.collidepoint(mouse_pos))
        draw_button("Salir", exit_button, exit_button.collidepoint(mouse_pos))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_button.collidepoint(mouse_pos):
                    return
                elif exit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(60)


def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        pygame.display.flip()
        clock.tick(60)


menu_loop()
game_loop()
pygame.quit()
