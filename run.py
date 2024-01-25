board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
player1 = "X"
winner = None
gameRunning = True

def boardGame(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print('------------')
    print(board[0] + "|" + board[1] + "|" + board[2])
    print('------------')
    print(board[0] + "|" + board[1] + "|" + board[2])

boardGame(board)

def playerInput(board):
    input = int(input("Enter a number between 1-9:"))
    

