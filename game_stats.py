class GameStats:
    """Track statistics for Alien Invasion."""
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state.
        self.game_active = False     
        
        # High score should never be reset.
        self.high_score = self.read_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        with open("high_score.txt", "r") as f:
            curr_hs = f.read()
        curr_high_score_read = int(curr_hs)
        return curr_high_score_read

    def write_high_score(self):
        curr_hs_read = self.read_high_score()
        if curr_hs_read < self.high_score:
            curr_hs_write = open("high_score.txt", "w")
            curr_hs_write.write(str(self.high_score))