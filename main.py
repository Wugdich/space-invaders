import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from alien import Alien


def run() -> None:
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space Invaders")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    alien = Alien(screen)

    while True:
        controls.events(screen, gun, bullets) 
        gun.update_gun()
        controls.bullets_update(bullets)
        controls.screen_update(bg_color, screen, gun, bullets, alien)


if __name__ == '__main__':
    run()

