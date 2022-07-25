import pygame
import controls
from gun import Gun
from pygame.sprite import Group


def run() -> None:
    pygame.init()
    screen = pygame.display.set_mode((800, 900))
    pygame.display.set_caption("Space Invaders")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()

    while True:
        controls.events(screen, gun, bullets) 
        gun.update_gun()
        bullets.update()
        controls.screen_update(bg_color, screen, gun, bullets)


if __name__ == '__main__':
    run()

