import pygame


class Gun():

    def __init__(self, screen: object):
        
        self.screen = screen
        self.image = pygame.image.load("images/gun.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 20
        self.mright = False
        self.mleft = False

    def output(self):
        """
        Gun drawing.
        """
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """
        Gun position update.
        """
        # Right movement.
        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        # Left movement.
        elif self.mleft and self.rect.left > 0:
            self.rect.centerx -= 1
