class NQueens:
    def __init__(self, num_queens):
        self.allowed_queens = num_queens
        self.queens = num_queens
        self.row_dict = {i: False for i in range(num_queens)}
        self.col_dict = {i: False for i in range(num_queens)}
        self.forward_dia_dict = {i: False for i in range(2*num_queens-1)}
        self.back_dia_dict = {i: False for i in range(2*num_queens-1)}
        self.row = num_queens

    def check_back_dia(self, row, col):
        for i in range((2*self.allowed_queens)-1):
            if (row - col) == ((self.allowed_queens) - i - 1):
                return i

    def is_allowed(self, row, col):
        if self.row_dict[row]:
            return False

        if self.col_dict[col]:
            return False

        # check forward dia
        if self.forward_dia_dict[row+col]:
            return False

        # check backward dia
        if self.back_dia_dict[self.check_back_dia(row, col)]:
            return False
        return True

    def mark_queen(self, row, col, val):
        self.row_dict[row] = val
        self.col_dict[col] = val
        self.forward_dia_dict[row + col] = val
        self.back_dia_dict[self.check_back_dia(row, col)] = val

    def solution(self, matrix, queens, row):

        if queens < 0:
            return
        if queens == 0:
            print(matrix)
            return True

        for i in range(row):
            for j in range(self.allowed_queens):
                if self.is_allowed(i, j):
                    self.mark_queen(i, j, True)
                    matrix[i][j] = 1
                    self.solution(matrix, queens-1, i+1)
                    matrix[i][j] = 0
                    self.mark_queen(i, j, False)


# matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

matrix = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

n = NQueens(4)
n.solution(matrix, 4, 4)
