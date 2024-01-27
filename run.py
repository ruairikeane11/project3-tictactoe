import random

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
player1 = "X"
winner = None
gameRunning = True

def boardGame(board):
    print(board[0] +     "|"     + board[1] +     "|"     + board[2])
    print('-----')
    print(board[3] +     "|"     + board[4] +     "|"     + board[5])
    print('-----')
    print(board[6] +     "|"     + board[7] +     "|"     + board[8])


def playerInput(board):
    inp = int(input("Enter a number between 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == " ":
        board[inp-1] = player1
    else:
        print('Sorry, this place has been taken!')

def checkAcross(board):
    """
    Checks for horizonral rows of X and makes a winner
    """
    global winner 
    if board[0] == board[1] == board[2] and board[1] != " ":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != " ":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7] != " ":
        winner = board[6]
        return True

def checkDown(board):
    """
    Checks for downward rows of X and makes a winner
    """
    global winner 
    if board[0] == board[3] == board[6] and board[0] != " ":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        winner = board[2]
        return True

def checkDiag(board):
    """
    Checks for diagonal rows of X and makes a winner
    """
    global winner 
    if board[0] == board[4] == board[8] and board[0] != " ":
        winner = board[0]
        return True
    elif board[6] == board[4] == board[2] and board[6] != " ":
        winner = board[6]
        return True

def checkDraw(board):
    """
    Checks to see if the board is full while there is no winner, and then restarts the game
    """
    global gameRunning
    if " " not in board:
        print(boardGame)
        print("It's a draw, start again!")
        gameRunning = False

def checkWinner():
    if checkAcross(board) or checkDown(board) or checkDiag(board):
        print(f'The winner is {winner}')
        restartGame()

def restartGame():
    """
    restarts the game when there is a winner
    """
    global board, player1, winner, gameRunning

    board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]
    player1 = "X"
    winner = None
    gameRunning = True
    print("Restarting game .....\n")

def changePlayer():
    global player1   
    if player1 == "X":
        player1 = "O"
    else :
        player1 = "X"

def computer(board):
    """
    Generates random integer between 0-8 when its O
    """
    while player1 == 'O':
        position = random.randint(0,8)
        if board[position] == " ":
            board[position] = "O"
            changePlayer()




#Create while loop to run game
while gameRunning:
    boardGame(board)
    playerInput(board)
    checkWinner()
    checkDraw(board)
    changePlayer()
    computer(board)
    checkWinner()
    checkDraw(board)