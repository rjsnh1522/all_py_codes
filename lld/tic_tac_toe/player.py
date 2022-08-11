

class Player:
    def __init__(self, name, email, symbol):
        self.name = name
        self.email = email
        self.ranking = None
        self.player_symbol = symbol
        self.games_played = 0
        self.games_won = 0

    def get_player_symbol(self):
        return self.player_symbol
