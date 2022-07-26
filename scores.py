import pygame.font


class Scores():
    """
    Game information output.
    """
    
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)
        self.image_scores()
        self.image_high_score()

    def image_scores(self):
        """
        Score string to image on screen.
        """
        self.scores_img = self.font.render(
                str(self.stats.scores), True, self.text_color, (0, 0, 0)
                )
        self.scores_rect = self.scores_img.get_rect()
        self.scores_rect.right = self.screen_rect.right - 40
        self.scores_rect.top = 20
    
    def draw_scores(self):
        self.screen.blit(self.scores_img, self.scores_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def image_high_score(self):
        """
        High score string to image on screen.
        """
        self.high_score_image = self.font.render(
                str(self.stats.high_score), True, self.text_color, (0, 0, 0)
                )
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

