##
## Name:
## Phillip Cork
##
##Program:
## bumper.py
##
## Purpose:
## To create a model of a new bumper cars activity in which
## the cars automatically change directions based on running into
## walls or other bumper cars.
##
##
## Input:
## A click from the user for ending the program.
##
## Output:
## The graphical elements including each bumper car and the window and the text instructions.

#import graphics for interfact and random for number generation
from graphics import *
from random import randint

# using the given amount of desire movement, create a random number
# between the negative and positive version of the integer
def getRandom(moveAmount):
    rand = randint(0-moveAmount,0+moveAmount)
    return rand


def didCollide(ball,ball2):
    # check to see if the two cars collide by getting the center X and Y coordinates of each point
    ballCenter = ball.getCenter()
    ball2Center = ball2.getCenter()
    ballX = ballCenter.getX()
    ballY = ballCenter.getY()
    ball2X = ball2Center.getX()
    ball2Y = ball2Center.getY()

    # if the distance from the center of one car to the next is less than or equal to the sum of the radius
    # return True, if not, return False
    if ((ball2X-ballX)**2+(ball2Y-ballY)**2)**.5 <= (ball.getRadius()+ball2.getRadius()):
        return True
    else:
        return False

def hitVertical(ball):
    # check the ball's x-coordinate of the center
    ballCenter = ball.getCenter()
    ballX = ballCenter.getX()
    # if the ball's center x-coordinate distance to a vertical wall is equal to the radius or less,
    # return True, if not, return False.
    if ballX <= 25 or ballX >= 475:
        return True
    else:
        return False


def hitHorizantal(ball):
    # check the ball's center y-coordinate of the center
    ballCenter = ball.getCenter()
    ballY = ballCenter.getY()
    # if the ball's center y-coorindate distance to a horizontal wall is equal to the radius or less,
    # return True, if not, return False.
    if ballY <= 25 or ballY >= 475:
        return True
    else:
        return False

def randomColor():
    # generate a random number between 0 and 255, the numberical values for rgb
    return randint(0,255)

def main():
    # create the graphical elements used in this demo
    # including the window, text instructions, and the two balls representing bumper cars
    # assign initial color and position to cars
    win = GraphWin("Bumper Cars",500,500)
    toQuit = Text(Point(250,400),"Click to Quit")
    ball = Circle(Point(100,100), 25)
    ball.setFill("blue")
    ball2 = ball.clone()
    ball2.setFill("red")
    ball2.move(350,350)
    toQuit.draw(win)
    ball.draw(win)
    ball2.draw(win)

    # set the range of movement
    moveAmount = 10
    # create the slope of each ball's trajectory given random integers
    b1X, b1Y = getRandom(moveAmount), getRandom(moveAmount)
    b2X, b2Y = getRandom(moveAmount), getRandom(moveAmount)

    # run this loop until the user clicks to quite
    while win.checkMouse() == None:

        # if the the center of each ball is within the sum of the radius distance from one another
        if didCollide(ball,ball2) == True:
        # set coordinate points so each ball will move in opposite directions
            b1X = b1X * -1
            b1Y = b1Y * -1
            b2X = b2X * -1
            b2Y = b2Y * -1

        # move the balls using new coordinates
            ball.move(b1X, b1Y)
            ball2.move(b2X, b2Y)

        # change colors
            ball.setFill(color_rgb(randomColor(), randomColor(), randomColor()))
            ball2.setFill(color_rgb(randomColor(), randomColor(), randomColor()))

        # if the ball's center is within the distance to the radius from a vertical wall,
        # flip the sign to change the trajectory and move the ball
        elif hitVertical(ball) == True:
            b1X = b1X * -1
            ball.move(b1X, b1Y)

        # if the ball's center is within the distance to the radius from a horizontal wall,
        # flip the sign to change the trajectory and move the ball
        elif hitHorizantal(ball) == True:
            b1Y = b1Y * -1
            ball.move(b1X, b1Y)
            # after moving the ball, flip the sign again to prevent
            # the ball from looping through reflections if stuck in a corner
            if hitHorizantal(ball) == True:
                b1Y = b1Y * -1
            else:
                pass

        # repeat above for ball 2
        elif hitVertical(ball2) == True:
            b2X = b2X * -1
            ball2.move(b2X, b2Y)

        elif hitHorizantal(ball2) == True:
            b2Y = b2Y * -1
            ball2.move(b2X, b2Y)
            if hitHorizantal(ball2) == True:
                b2Y = b2Y * -1
            else:
                pass

        # if no other conditions are met, continue moving cars according to slope
        else:
            ball.move(b1X, b1Y)
            ball2.move(b2X, b2Y)


main()
