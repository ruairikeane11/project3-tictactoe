import random
from colorama import init, Fore, Style

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
player1 = "X"
winner = None
gameRunning = True
roundCounter = 0
score = {"X": 0, "O": 0}

init(autoreset=True)  # Autoresets colors


def boardGame(board):
    print(Fore.BLUE + f"YOU ARE {player1}")
    print(Fore.BLUE + "THE FIRST PLAYER TO GET 3 IN A ROW WINS.")
    print(board[0] + "|" + board[1] + "|" + board[2])
    print('-----')
    print(board[3] + "|" + board[4] + "|" + board[5])
    print('-----')
    print(board[6] + "|" + board[7] + "|" + board[8])


def playerInput(board):
    try:
        inp = int(input("Enter a number between 1-9: "))
        if inp >= 1 and inp <= 9 and board[inp - 1] == " ":
            board[inp - 1] = player1
        else:
            print(Fore.RED + 'Sorry, this place has been taken!')
            print(Style.RESET_ALL)  # Resets color to default
            playerInput(board)
    except ValueError:
        print(Fore.RED + 'Invalid input. Please enter a number between 1-9.')
        print(Style.RESET_ALL)  # Resets color to default
        playerInput(board)


def checkAcross(board):
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
    global winner
    if board[0] == board[4] == board[8] and board[0] != " ":
        winner = board[0]
        return True
    elif board[6] == board[4] == board[2] and board[6] != " ":
        winner = board[6]
        return True


def checkDraw(board):
    global gameRunning
    if " " not in board:
        print(boardGame(board))
        print(Fore.RED + "IT'S A DRAW, START AGAIN!")
        print(Style.RESET_ALL)
        restartGame()
        gameRunning = False


def checkWinner():
    global roundCounter, score
    if checkAcross(board) or checkDown(board) or checkDiag(board):
        print(Fore.RED + f'THE WINNER IS {winner}')
        roundCounter += 1
        score[player1] += 1
        print(f"SCORE - X: {score['X']} | O: {score['O']}")
        restartGame()
    
def restartGame():
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
    else:
        player1 = "X"


def computer(board):
    while player1 == 'O':
        position = random.randint(0, 8)
        if board[position] == " ":
            board[position] = "O"
            changePlayer()


def roundCount():
    global roundCounter
    print(Fore.BLUE + f"ROUNDS PLAYED: {roundCounter}")


# Create while loop to run the game
while gameRunning:
    roundCount()
    boardGame(board)
    playerInput(board)
    checkWinner()
    checkDraw(board)
    changePlayer()
    computer(board)
    checkWinner()
    checkDraw(board)

    
    



