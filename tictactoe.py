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
    if userInput == "q":
        print("Thanks for playing!")
        return True
    else: return False

# printGameBoard(board)

while True:
    userInput = input("Please enter a slot 1-9 or \"q\" to quit: ")
    if quitGame(userInput):
        break