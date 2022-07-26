import pygame


class Alien(pygame.sprite.Sprite):
    """
    One alien class.
    """

    def __init__(self, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/alien2.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """
        Alien drawing.
        """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        Alien movement.
        """
        self.y += 0.05
        self.rect.y = self.y

