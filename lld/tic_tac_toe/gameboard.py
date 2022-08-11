class GameBoard:
    def __init__(self, player_one, player_two, board_size=3):
        self.board_size = board_size
        self.game_board = [
            ["-" for i in range(self.board_size)] for j in range(self.board_size)
        ]
        self.input_value = ""
        self.player_one = player_one
        self.player_two = player_two
        self.next_turn = [player_one, player_two]
        self.occupied_places = []

    def __print_board(self):
        for row in self.game_board:
            print(row)
        print("-------------------------------")

    def __validate_input(self, value):
        if value < 0 or value > ((self.board_size * self.board_size) - 1):
            return False
        if value in self.occupied_places:
            return False
        return True

    def __get_user_input(self, current_player):
        self.__print_board()
        val = int(input(
            "{} Please enter a number between 0 to {} ".format(current_player.name,
                                                               (self.board_size * self.board_size) - 1
            )
        ))
        while not self.__validate_input(val):
            self.__print_board()
            print("Wrong input, Please try again")
            val = int(input(
                "{} Please enter a number between 0 to {}  ".format(current_player.name,
                                                                    (self.board_size * self.board_size) - 1
                )
            ))
        return val

    def __check_end_game(self, current_player):
        player_symbol = current_player.get_player_symbol()
        game_board = self.game_board
        board_size = self.board_size

        def row_win():
            won = False
            for row in range(len(game_board)):
                current_str = ""
                for col in range(len(game_board[row])):
                    if player_symbol == game_board[row][col]:
                        current_str += player_symbol
                        if len(current_str) == board_size:
                            won = True
                            print("Won from row match")
                            break
                    else:
                        current_str = ""
                        won = False
                        break
                if won:
                    break
            return won

        def col_win():
            won = False
            for col in range(len(game_board[0])):
                current_str = ""
                for row in range(len(game_board)):
                    if player_symbol == game_board[row][col]:
                        current_str += player_symbol
                        if len(current_str) == board_size:
                            won = True
                            print("Won from column match")
                            break
                    else:
                        current_str = ""
                        won = False
                        break
                if won:
                    break
            return won

        def diagonal_back_win():
            won = False
            current_str = ""
            for row in range(len(game_board)):
                for col in range(len(game_board[row])):
                    if row == col:
                        if player_symbol == game_board[row][col]:
                            current_str += player_symbol
                            if len(current_str) == board_size:
                                won = True
                                print("Won from backward diagonal match")
                                break
                        else:
                            current_str = ""
                            won = False
                            break
                if won:
                    break
            return won

        def diagonal_forward_win():
            won = False
            current_str = ""
            for row in range(len(game_board)):
                for col in range(len(game_board[row])):
                    if row + col == (board_size - 1):
                        if player_symbol == game_board[row][col]:
                            current_str += player_symbol
                            if len(current_str) == board_size:
                                won = True
                                print("Won from forward diagonal match")
                                break
                        else:
                            current_str = ""
                            won = False
                            break
                if won:
                    break
            return won

        if any([row_win(), col_win(), diagonal_back_win(), diagonal_forward_win()]):
            return True
        return False

    def start_game(self):
        self.__print_board()
        count = 0
        while True:
            count += 1
            if count == (self.board_size * self.board_size + 1):
                print("Match Draw")
                break
            current_player = self.next_turn.pop(0)
            position = int(self.__get_user_input(current_player))

            row = position // self.board_size
            col = position % self.board_size
            self.game_board[row][col] = current_player.get_player_symbol()
            self.__print_board()
            if count >= self.board_size:
                if self.__check_end_game(current_player):
                    print(f"Player {current_player.name} won, symbol {current_player.get_player_symbol()}")
                    break
            self.occupied_places.append(position)
            self.next_turn.append(current_player)
