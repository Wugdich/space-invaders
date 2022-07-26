import pygame
import time
import sys
from bullet import Bullet
from alien import Alien


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


def screen_update(bg_color: tuple, screen , gun, bullets, aliens) -> None:
    """
    Screen updating.
    """
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    aliens.draw(screen)
    pygame.display.flip()


def bullets_update(bullets, aliens):
    """
    Bullets update.
    """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)


def create_army(screen, aliens):
    """
    Aliens army creation.
    """
    alien = Alien(screen)
    alien_width = alien.rect.width
    army_size_x = int((700 - 2 * alien_width) / alien_width)

    alien_height = alien.rect.height
    army_size_y = int((800 - 84 - 2 * alien_width) / alien_width / 2)

    for row in range(army_size_y):
        for alien_number in range(army_size_x):
            alien = Alien(screen)
            alien.x = alien_width + alien_width * alien_number
            alien.y = alien_height + alien_height * row
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height +  1.5 * alien.rect.height * row
            aliens.add(alien)


def update_aliens(aliens, gun, stats, screen, bullets):
    """
    Aliens update.
    """
    aliens.update()
    if pygame.sprite.spritecollideany(gun, aliens):
        gun_destroy(stats, screen, gun, aliens, bullets)

def gun_destroy(stats, screen, gun, aliens, bullets):
    """
    Army and gun collision.
    """
    stats.guns_left -= 1
    aliens.empty()
    bullets.empty()
    create_army(screen, aliens)
    gun.create_gun()
    time.sleep(2)

