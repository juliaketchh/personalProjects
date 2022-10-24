# tic tac toe
#following a YouTube tutorial by Garrett codes
#Julia Ketch
#October 22nd, 2022
#Seoul, South Korea

# prompt the user to enter a number 1-9 corrsponding to the slots of the board, left to right top to bottom
# check if the slot is already taken
# if not add it to the board
# check if there is a 3 in a row
# end game if so
# end game if all slots are filled
# toggle between users

import copy



def printGameBoard(board) :
    for row in board:
        for slot in row:
            print(slot, end=" ")
        print()        

def quitGame(userInput) :
    if userInput.lower() == "q":
        print("thanks for playing!")
        return True
    else: return False

def checkInput(userInput) :
    # check if input is a number
    if not isNum(userInput):
        return False
    # is 1 - 9
    userInputNum = int(userInput)

    if not bounds(userInputNum) :
        return False
    #check if the slot if not already taken 
    return True

def isNum(userInput) :
    if not userInput.isnumeric() :
        print("this is not a valid number")
        return False
    else: return True

def bounds(userInput) :
    if userInput > 9 or userInput < 1 :
        print("this number is out of bounds")
        return False
    else: return True

def isTaken(coords, board) :
    if board[coords[0]][coords[1]] != "-":
        print("this position is already taken")
        return True
    else: return False

def coordinates(userInput) :
    row = userInput // 3
    col = userInput % 3
    return(row, col)

def initalizeBoard() :
    board = [
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]
    ]
    return board

def addToBoard(coords, board, playerSymbol):
    newBoard = copy.deepcopy(board)
    newBoard[coords[0]][coords[1]] = playerSymbol
    return newBoard 

def currentUser(user):
    if user:
        return "x"
    else:
        return "o"

def checkRow(user, board):
    for row in board:
        completeRow = True
        for slot in row:
            if slot != user:
                completeRow = False
                break
        if completeRow:
            return True

    return False

def checkCol(user, board):
    for col in range(3):
        completeCol = True
        for row in range(3):
            if board[row][col] != user:
                completeCol = False
                break
        if completeCol:
            return True
    return False

def checkDiagonal(user, board):
    if board[0][0] == user and board[1][1] == user and board[2][2] == user:
        return True
    if board[0][2] == user and board[1][1] == user and board[2][0] == user:
        return True
    return False

def isWin(user, board):
    if checkRow(user, board):
        return True
    if checkCol(user, board):
        return True
    if checkDiagonal(user, board):
        return True

    return False


gameBoard = initalizeBoard()

user = True # when true, put x's on the board, otherwise put o's

while True :
    player = currentUser(user)
    printGameBoard(gameBoard)
    userInput = input("enter a slot 1-9 or \"q\" to quit: ")
    if quitGame(userInput):
        break
    if not checkInput(userInput):
        print("please try again")
        continue

    userInput =int(userInput)
    userInput = userInput - 1
    coords = coordinates(userInput)

    if isTaken(coords, gameBoard):
        print("please try again")
        continue

    gameBoard = addToBoard(coords, gameBoard, player)
    if isWin(player, gameBoard) :
        printGameBoard(gameBoard)
        print("congratulations,", player, "won!")
        break
    user = not user