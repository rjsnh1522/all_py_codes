#
# # player_symbol = 'x'
#
# game_board_diag = [['x', 'o', 'o', 'x'], ['x', 'x', 'x', 'o'], ['x', 'o', 'x', 'o'], ['x', 'x', 'x', 'x']]
# game_board_for_diag = [['x', 'x', 'o', 'x'], ['x', 'o', 'x', 'o'], ['x', 'o', 'x', 'o'], ['x', 'x', 'x', 'x']]
# game_board_row = [['x', 'x', 'o', 'x'], ['x', 'o', 'x', 'o'], ['x', 'o', 'x', 'o'], ['x', 'x', 'x', 'x']]
# game_board_col = [['x', 'x', 'x', 'x'], ['o', 'x', 'x', 'o'], ['x', 'o', 'x', 'o'], ['x', 'x', 'x', 'x']]
#
#
# def row_win(game_board, player_symbol, board_size=3):
#     won = False
#     for row in range(len(game_board)):
#         current_str = ""
#         for col in range(len(game_board[row])):
#             if player_symbol == game_board[row][col]:
#                 current_str += player_symbol
#                 if len(current_str) == board_size:
#                     won = True
#                     break
#             else:
#                 current_str = ""
#                 won = False
#                 break
#         if won:
#             break
#     return won
#
#
# def col_win(game_board, player_symbol, board_size=3):
#     for col in range(board_size):
#         current_str = ""
#         for row in range(board_size):
#             if player_symbol == game_board[row][col]:
#                 current_str += player_symbol
#                 if len(current_str) == board_size:
#                     won = True
#                     break
#             else:
#                 current_str = ""
#                 won = False
#                 break
#         if won:
#             break
#     return won
#
#
# def diagonal_back_win(game_board, player_symbol, board_size=3):
#     won = False
#     current_str = ""
#     for row in range(len(game_board)):
#         for col in range(len(game_board[row])):
#             if row == col:
#                 if player_symbol == game_board[row][col]:
#                     current_str += player_symbol
#                     if len(current_str) == board_size:
#                         won = True
#                         break
#                 else:
#                     current_str = ""
#                     won = False
#                     break
#         if won:
#             break
#     return won
#
#
# def diagonal_forward_win(game_board, player_symbol, board_size=3):
#     won = False
#     current_str = ""
#     for row in range(len(game_board)):
#         for col in range(len(game_board[row])):
#             if row + col == (board_size - 1):
#                 if player_symbol == game_board[row][col]:
#                     current_str += player_symbol
#                     if len(current_str) == board_size:
#                         won = True
#                         break
#                 else:
#                     current_str = ""
#                     won = False
#                     break
#         if won:
#             break
#     return won
#
#
# # print(row_win(game_board_row, 'x', board_size=4))
# print(col_win(game_board_col, 'x', board_size=3))
# # print(diagonal_back_win(game_board_diag, 'x'))
# # print(diagonal_forward_win(game_board_for_diag, 'x'))


class Student:
    # protected data members
    _name = None
    _roll = None
    _branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch
        self.goal = "goal"

    # protected member function
    def _displayRollAndBranch(self):
        # accessing protected data members
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)


# derived class
class Geek(Student):

    # constructor
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)

    # public member function
    def displayDetails(self):
        # accessing protected data members of super class
        print("Name: ", self._name)

        # accessing protected member functions of super class
        self._displayRollAndBranch()


# creating objects of the derived class
obj = Geek("R2J", 1706256, "Information Technology")

# calling public member functions of the class
obj.displayDetails()


