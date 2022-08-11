from tic_tac_toe.gameboard import GameBoard
from tic_tac_toe.player import Player


class PlayGame:
    def __init__(self):
        p1 = Player(name="ramesh", email="ramesh@genpact.com", symbol="X")
        p2 = Player(name="suresh", email="suresh@genpact.com", symbol="O")

        gameboard = GameBoard(p1, p2, board_size=4)
        gameboard.start_game()


play_game = PlayGame()
# print(play_game)
