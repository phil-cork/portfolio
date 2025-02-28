##
## Name:
## Phillip Cork
##
##Program:
## TicTacToe.py
##
## Purpose:
## To provide two players a graphic interface in which to play Tic Tac Toe.
##
## Input:
## Clicks from the user playing the game in the GUI.
##
## Output:
## The graphical elements including instructions, the board, the player's markers, and updates.

#import graphics
from graphics import *

# create initial board of all empty spaces
# set up graphic window and make relative coordinates for board

def buildBoard():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    win = GraphWin("Tic Tac Toe", 450, 450)
    win.setCoords(0, 0, 11, 11)
    win.setBackground(color_rgb(254, 255, 156))
    return board, win

# display the vertical and horizontal lines of the board
def displayBoard(win):
    vLine1 = Line(Point(4, 1), Point(4, 10))
    vLine2 = Line(Point(7, 1), Point(7, 10))
    hLine1 = Line(Point(1, 4), Point(10, 4))
    hLine2 = Line(Point(1, 7), Point(10, 7))
    vLine1.draw(win)
    vLine2.draw(win)
    hLine1.draw(win)
    hLine2.draw(win)

# get user's click, use x and y coordinates to determine which square is chosen.
# if no valid square is chosen, return an error message
def getSpot(spot):

    spotX = spot.getX()
    spotY = spot.getY()
    error = ""
    square = 0
    center = Point(-1, -1)
    if 7 < spotY < 10:
        if 1 < spotX < 4:
            square = 1
            center = Point(2.5,8.5)
        elif 4 < spotX < 7:
            square = 2
            center = Point(5.5, 8.5)
        elif 7 < spotX < 10:
            square = 3
            center = Point(8.5, 8.5)
        else:
            error = "Please choose a valid point"
    elif 4 < spotY < 7:
        if 1 < spotX < 4:
            square = 4
            center = Point(2.5, 5.5)
        elif 4 < spotX < 7:
            square = 5
            center = Point(5.5, 5.5)
        elif 7 < spotX < 10:
            square = 6
            center = Point(8.5, 5.5)
        else:
            error = "Please choose a valid point"
    elif 1 < spotY < 4:
        if 1 < spotX < 4:
            square = 7
            center = Point(2.5, 2.5)
        elif 4 < spotX < 7:
            square = 8
            center = Point(5.5, 2.5)
        elif 7 < spotX < 10:
            square = 9
            center = Point(8.5, 2.5)
        else:
            error = "Please choose a valid point"
    else:
        error = "Please choose a valid point"

    return square, center, error

# check to see if that spot on the board is empty
# if empty, return True. if not, return False
def isLegal(board, square):
        if board[square-1] == "x":
            return False
        elif board[square-1] == "o":
            return False
        else:
            return True

# if spot is legal, fill spot with player's character
def fillSpot(board, square, char):
    if isLegal(board, square) is True:
        board[square-1] = char

def updateBoard(win,char, center):
    charPlace = Text(center, char)
    charPlace.setSize(32)
    if char == "x":
        charPlace.setTextColor("red")
    elif char == "o":
        charPlace.setTextColor("blue")
    else:
        pass
    charPlace.draw(win)

# check to see if game is won after each move.
def isGameWon(board):
    win = ""
    # diagonal win conditions in list, square = # + 1
    if board[6] == board[4] == board[2] or board[0] == board[4] == board[8]:
        win = "diagonal"
    # vertical win conditions in list, square = # + 1
    elif board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8]:
        win = "vertical"
    # horizontal win conditions in list, square = # + 1
    elif board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8]:
        win = "horizontal"
    else:
        # no win condition, return False
        win = ""

    if win != "":
        return True
    else:
        return False

# check to see if the game is over due to winning or no remaining turns.
def isGameOver(numPlays):
    if numPlays == 9:
        return True
    else:
        return False

def main():
    # build the board list and GUI board
    board, win = buildBoard()
    displayBoard(win)

    # initialize the player number, the turns, the character
    # and the messages to be used throughout game.
    player = 1
    numPlays = 0
    char = "x"
    turn = Text(Point(5.5, .5), "Player 1's Turn")
    turn.draw(win)
    rules = Text(Point(5.5, .25), "")

    while isGameOver(numPlays) is False and isGameWon(board) is False:

        spot = win.getMouse()
        square, center, error = getSpot(spot)

        while isLegal(board, square) is False or error != "":
            rules = Text(Point(5.5, .25), "Please choose a valid square")
            rules.draw(win)

            spot = win.getMouse()
            square, center, error = getSpot(spot)
            isLegal(board, square)
            rules.undraw()

        if player % 2 == 0:
            turn.undraw()
            turn = Text(Point(5.5,.5), "Player 1's turn")
            turn.draw(win)
            char = "o"

        if player % 2 != 0:
            turn.undraw()
            turn = Text(Point(5.5,.5), "Player 2's turn")
            turn.draw(win)
            char = "x"

        fillSpot(board, square, char)

        # update the GUI board for users using the respective player's character
        # and
        updateBoard(win,char,center)

        player = player + 1
        numPlays = numPlays + 1

        isGameOver(numPlays)
        isGameWon(board)

        if isGameWon(board) is True:
            rules.undraw()
            turn.undraw()
            if player % 2 == 0:
                result = Text(Point(5.5,.25), "Player 1 Wins. Click to Quit.")
            elif player % 2 != 0:
                result = Text(Point(5.5, .25), "Player 2 Wins. Click to Quit.")
            else:
                result = Text(Point(5.5,.25), "")
            result.draw(win)
            win.getMouse()

        elif isGameOver(numPlays) is True:
            result = Text(Point(5.5,.25), "No One Wins. Click to Quit.")
            rules.undraw()
            turn.undraw()
            result.draw(win)
            win.getMouse()

main()