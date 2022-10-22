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

board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

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

def isTaken(userInput) :
    if 


while True :
    userInput = input("enter a slot 1-9 or \"q\" to quit: ")
    if quitGame(userInput):
        break
    if not checkInput(userInput):
        print("please try again")
        continue
    userInput = int(userInput) - 1