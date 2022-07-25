import pygame
import sys


def events(gun) -> None:
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
        elif event.type == pygame.KEYUP:
            # Right movement.
            if event.key == pygame.K_d:
                gun.mright = False
            # Left movement.
            elif event.key == pygame.K_a:
                gun.mleft = False


def screen_update(bg_color: tuple, screen , gun) -> None:
    """
    Screen updating.
    """
    screen.fill(bg_color)
    gun.output()
    pygame.display.flip()

