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


def screen_update(bg_color: tuple, screen , gun, bullets, aliens, sc) -> None:
    """
    Screen updating.
    """
    screen.fill(bg_color)
    sc.draw_scores()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    aliens.draw(screen)
    pygame.display.flip()


def bullets_update(bullets, aliens, screen, stats, sc):
    """
    Bullets update.
    """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for dead_aliens in collisions.values():
            stats.scores += 10 * len(dead_aliens)
        sc.image_scores()
        check_highscore(stats, sc)
        sc.image_guns()
    if len(aliens) == 0:
        bullets.empty()
        create_army(screen, aliens)


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


def update_aliens(aliens, gun, stats, screen, bullets, sc):
    """
    Aliens update.
    """
    aliens.update()
    if pygame.sprite.spritecollideany(gun, aliens):
        gun_destroy(stats, screen, gun, aliens, bullets, sc)
    aliens_success(stats, screen, gun, aliens, bullets, sc)

def gun_destroy(stats, screen, gun, aliens, bullets, sc):
    """
    Army and gun collision.
    """
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        aliens.empty()
        bullets.empty()
        create_army(screen, aliens)
        gun.create_gun()
        time.sleep(2)
    else:
        stats.run_game = False
        sys.exit()

def aliens_success(stats, screen, gun, aliens, bullets, sc):
    """
    Check aliens are at the bottom of the screen.
    """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            gun_destroy(stats, screen, gun, aliens, bullets, sc)
            break

def check_highscore(stats, sc):
    """
    New highscore checking.
    """
    if stats.scores > stats.high_score:
        stats.high_score = stats.scores
        sc.image_high_score()
        with open("highscore.txt", "w") as file:
            file.write(str(stats.high_score))

