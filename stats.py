import pygame


class Stats():
    """
    Statistics tracking.
    """

    def __init__(self):
        self.reset_stats()

    def reset_stats(self):
        """
        Statistic changing.
        """
        self.guns_left = 3

