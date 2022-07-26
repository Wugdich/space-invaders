import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run() -> None:
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space Invaders")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    controls.create_army(screen, aliens)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets) 
        if stats.run_game:
            gun.update_gun()
            controls.bullets_update(bullets, aliens, screen, stats, sc)
            controls.screen_update(bg_color, screen, gun, bullets, aliens, sc)
            controls.update_aliens(aliens, gun, stats, screen, bullets)


if __name__ == '__main__':
    run()

