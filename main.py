import pygame
import controls
from gun import Gun


def run() -> None:
    pygame.init()
    screen = pygame.display.set_mode((800, 900))
    pygame.display.set_caption("Space Invaders")
    bg_color = (0, 0, 0)
    gun = Gun(screen)

    while True:
        controls.events(gun=gun) 
        gun.update_gun()
        controls.screen_update(bg_color, screen, gun)


if __name__ == '__main__':
    run()

