

class Stats():
    """
    Statistics tracking.
    """

    def __init__(self):
        self.reset_stats()
        self.run_game = True

    def reset_stats(self):
        """
        Statistic changing.
        """
        self.guns_left = 3
        self.scores = 0

