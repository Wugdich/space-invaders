import pygame
import sys
from bullet import Bullet


def events(screen, gun, bullets) -> None:
    """
    Events proccessing.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Right movement.
            if event.key == pygame.K_d:
                gun.mright = True
            # Left movement.
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                # Fire.
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # Right movement.
            if event.key == pygame.K_d:
                gun.mright = False
            # Left movement.
            elif event.key == pygame.K_a:
                gun.mleft = False


def screen_update(bg_color: tuple, screen , gun, bullets) -> None:
    """
    Screen updating.
    """
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    pygame.display.flip()

def bullets_update(bullets):
    """
    Bullets update.
    """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

