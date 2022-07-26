

class Stats():
    """
    Statistics tracking.
    """

    def __init__(self):
        self.reset_stats()
        self.run_game = True
        with open("highscore.txt", "r") as file:
            self.high_score = int(file.readline())
            print(self.high_score)

    def reset_stats(self):
        """
        Statistic changing.
        """
        self.guns_left = 3
        self.scores = 0

