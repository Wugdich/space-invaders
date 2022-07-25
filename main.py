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
        screen.fill(bg_color)
        gun.update_gun()
        gun.output()
        pygame.display.flip()


if __name__ == '__main__':
    run()

