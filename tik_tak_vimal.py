# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
from termios import tcflush, TCIFLUSH
board = ['-','-','-','-','-','-','-','-','-']

currentPlayer = 'X'
gameRunning = True
winner = None

def checkHori(board):
    global winner
    if board[0]==board[1]==board[2] and board[0]!='-':
        winner = board[0]
        return True
    if board[3]==board[4]==board[5] and board[3]!='-':
        winner = board[3]
        return True
    if board[6]==board[7]==board[8] and board[8]!='-':
        winner = board[8]
        return True

def checkdia(board):
    global winner
    if board[0]==board[4]==board[8] and board[8]!='-':
        winner = board[0]
        return True
    if board[3]==board[4]==board[6] and board[6]!='-':
        winner = board[3]
        return True

def checkrow(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!='-':
        winner = board[0]
        return True
    if board[1]==board[4]==board[7] and board[1]!='-':
        winner = board[1]
        return True
    if board[2]==board[5]==board[8] and board[8]!='-':
        winner = board[8]
        return True


def checkWin():
    global gameRunning
    if checkrow(board) or checkdia(board) or checkHori(board):
        print(f"the winner is {winner}")
        gameRunning = False


def checkTie():
    global gameRunning
    if '-' not in board:
        gameRunning = False
        printBoard(board)


def switchplayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    elif currentPlayer == 'O':
        currentPlayer = 'X'

def printBoard(board):
    print(board[0]+ "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3]+ "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6]+ "|" + board[7] + "|" + board[8])

def playIt(board):
    #inp = " "

    inp = int(input("Enter no between 1 to 9").strip())
    #tcflush(sys.stdin, TCIFLUSH)
    print("888",inp)
    print("test")
    if inp >=1 and inp <=9 and board[inp-1] == '-':
        board[inp-1]=currentPlayer
        print(board)
    else:
        print("already a move exits or wrong selection")
        playIt(board)

while gameRunning:
    printBoard(board)
    playIt(board)
    checkWin()
    checkTie()
    switchplayer()

