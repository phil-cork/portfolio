##
## Name:
## Phillip Cork
##
##Program:
## fallGreeting.py
##
## Purpose:
## To use the graphics package provided by the author to design a Thanksgiving
## greeting card that incorporates 4 graphic objects, a message, and an animation.
##
##
## Input:
## Clicks from the user to start and stop the animation.
##
## Output:
## The graphical elements included in the function.
##

# import the sleep function to manage animation speeds
from time import *
# import graphics
from graphics import *
#create the window for graphics to display
win = GraphWin("greeting",1000,1000)
#set up relative gride for placing objects
win.setCoords(0,-2,20,20)
#set background color
win.setBackground(color_rgb(140,106,69))

#create greeting message and style with Face, Size, and Style options
message = Text(Point(10,19), "Happy Thanksgiving!")
message.setFace("helvetica")
message.setSize(36)
message.setStyle("italic")
message.draw(win)

#create and style the leaf and stem
triangle = Polygon(Point(10,2),Point(10.5,2),Point(10,4))
triangle.setFill(color_rgb(16, 159, 36))
stem = Line(Point(10,2),Point(10,12))

#create template for the white "nodes" on the leaf
zero = Point(0,0)
node = Circle(zero,.075)
node.setFill("white")

#create a series of lines as branches from the stem
leftBranch1 = Line(Point(10,7),Point(4,13))
leftBranch2 = Line(Point(10,9),Point(8,11))
leftBranch3 = Line(Point(10,12),Point(9,13))
leftBranch4 = Line(Point(6,11),Point(6,13))
leftBranch5 = Line(Point(8,9),Point(5,7))
leftBranch6 = Line(Point(8,9),Point(4,9))
leftBranch7 = Line(Point(9,10),Point(9,11.5))

rightBranch1 = Line(Point(10,7),Point(16,13))
rightBranch2 = Line(Point(11,8),Point(14,8))
rightBranch3 = Line(Point(14,8),Point(14.5,7.5))
rightBranch4 = Line(Point(14,11),Point(15,11))
rightBranch5 = Line(Point(15,12),Point(17,12))
rightBranch6 = Line(Point(10,10),Point(12,12))
rightBranch7 = Line(Point(10,12),Point(11,13))
rightBranch8 = Line(Point(13,10),Point(13,11))
rightBranch9 = Line(Point(11,11),Point(11,12))

#create the two sides of the leaf using polygon
leftLeaf = Polygon(
Point(9,7),
Point(7,7.5),
Point(5,6.5),
Point(4,6),
Point(4,7),
Point(5,8.5),
Point(4,8),
Point(2,9.5),
Point(5,10),
Point(4,10.5),
Point(5,11),
Point(2,12),
Point(3,12.5),
Point(2,15),
Point(5,14),
Point(5,16),
Point(6,15),
Point(7,14),
Point(7,13),
Point(8,12),
Point(7,15),
Point(9,14),
Point(9,15),
Point(10,18),
Point(10,6.5)
)
leftLeaf.setFill(color_rgb(16, 159, 36))

rightLeaf = Polygon(
Point(10,6.5),
Point(11,7),
Point(14.,7),
Point(16,7),
Point(14,9),
Point(17,10),
Point(16,10.5),
Point(17,11),
Point(18,12.5),
Point(17,13.5),
Point(17,15),
Point(15,13),
Point(15,14),
Point(12.5,12),
Point(13.5,14),
Point(12,13),
Point(12.5,14),
Point(12,15),
Point(11.5,14),
Point(11,15),
Point(10,18),
)
rightLeaf.setFill(color_rgb(16, 159, 36))

#clone template node and move into place
lb1Node = node.clone()
lb1Node.move(9,8)
lb2Node = node.clone()
lb2Node.move(8,9)
lb3Node = node.clone()
lb3Node.move(7,10)
lb4Node = node.clone()
lb4Node.move(6,11)
lb5Node = node.clone()
lb5Node.move(5,12)
lb6Node = node.clone()
lb6Node.move(4,13)
lb7Node = node.clone()
lb7Node.move(7,9)
lb8Node = node.clone()
lb8Node.move(6,9)
lb9Node = node.clone()
lb9Node.move(5,9)
lb10Node = node.clone()
lb10Node.move(4,9)
lb11Node = node.clone()
lb11Node.move(5,7)
lb12Node = node.clone()
lb12Node.move(6,13)
lb13Node = node.clone()
lb13Node.move(4,13)
lb14Node = node.clone()
lb14Node.move(8,11)
lb15Node = node.clone()
lb15Node.move(9,13)
lb16Node = node.clone()
lb16Node.move(9,11.5)
lb17Node = node.clone()
lb17Node.move(9,10)

rb1Node = node.clone()
rb1Node.move(11,8)
rb2Node = node.clone()
rb2Node.move(12,8)
rb3Node = node.clone()
rb3Node.move(13,8)
rb4Node = node.clone()
rb4Node.move(14,8)
rb5Node = node.clone()
rb5Node.move(14.5,7.5)
rb6Node = node.clone()
rb6Node.move(12,9)
rb7Node = node.clone()
rb7Node.move(14,11)
rb8Node = node.clone()
rb8Node.move(15,12)
rb9Node = node.clone()
rb9Node.move(16,13)
rb10Node = node.clone()
rb10Node.move(15,11)
rb11Node = node.clone()
rb11Node.move(17,12)
rb12Node = node.clone()
rb12Node.move(11,13)
rb13Node = node.clone()
rb13Node.move(11,11)
rb14Node = node.clone()
rb14Node.move(11,13)
rb15Node = node.clone()
rb15Node.move(13,10)
rb16Node = node.clone()
rb16Node.move(11,12)
rb17Node = node.clone()
rb17Node.move(13,11)
rb18Node = node.clone()
rb18Node.move(12,12)

#draw main objects
triangle.draw(win)
stem.draw(win)
leftLeaf.draw(win)
rightLeaf.draw(win)

#draw all of the branches, using sleep to space the objects out slightly
sleep(.1)
leftBranch1.draw(win)
sleep(.1)
leftBranch2.draw(win)
sleep(.1)
leftBranch3.draw(win)
sleep(.1)
leftBranch4.draw(win)
sleep(.1)
leftBranch5.draw(win)
sleep(.1)
leftBranch6.draw(win)
sleep(.1)
leftBranch7.draw(win)
sleep(.1)
rightBranch1.draw(win)
sleep(.1)
rightBranch2.draw(win)
sleep(.1)
rightBranch3.draw(win)
sleep(.1)
rightBranch4.draw(win)
sleep(.1)
rightBranch5.draw(win)
sleep(.1)
rightBranch6.draw(win)
sleep(.01)
rightBranch7.draw(win)
sleep(.1)
rightBranch8.draw(win)
sleep(.1)
rightBranch9.draw(win)

#draw the nodes in the window
lb1Node.draw(win)
lb2Node.draw(win)
lb3Node.draw(win)
lb4Node.draw(win)
lb5Node.draw(win)
lb6Node.draw(win)
lb7Node.draw(win)
lb8Node.draw(win)
lb9Node.draw(win)
lb10Node.draw(win)
lb11Node.draw(win)
lb12Node.draw(win)
lb13Node.draw(win)
lb14Node.draw(win)
lb15Node.draw(win)
lb16Node.draw(win)
lb17Node.draw(win)

rb1Node.draw(win)
rb2Node.draw(win)
rb3Node.draw(win)
rb4Node.draw(win)
rb5Node.draw(win)
rb6Node.draw(win)
rb7Node.draw(win)
rb8Node.draw(win)
rb9Node.draw(win)
rb10Node.draw(win)
rb11Node.draw(win)
rb12Node.draw(win)
rb13Node.draw(win)
rb14Node.draw(win)
rb15Node.draw(win)
rb16Node.draw(win)
rb17Node.draw(win)
rb18Node.draw(win)

sleep(.5)
#list of colors for gradient effect
bk_color=[
    color_rgb(16, 159, 36),
    color_rgb(18, 182, 41),
    color_rgb(20, 205, 46),
    color_rgb(23, 228, 51),
    color_rgb(43, 234, 69),
    color_rgb(255, 182, 93), #bright green
    color_rgb(255, 171, 70), #bright orange
    color_rgb(255, 159, 45),
    color_rgb(255, 148, 19),
    color_rgb(249, 136, 0),
    color_rgb(224, 122, 0),
    color_rgb(255, 148, 16),
    color_rgb(246, 136, 0),
    color_rgb(221, 122, 0),
    color_rgb(195, 108, 0),
    color_rgb(173,94,0),
    color_rgb(148,80,0),
    color_rgb(122,66,0),
    color_rgb(97,52,0),
    color_rgb(72,38,0),
    color_rgb(46,25,0),
    color_rgb(43, 2, 0), #dark brown
    color_rgb(69,3,0), #dark red
    color_rgb(94,4,0),
    color_rgb(95,5,0),
    color_rgb(120,6,0),
    color_rgb(146,7,0),
    color_rgb(171,9,0),
    color_rgb(197,10,0), #bright red
]

#loop through colors with a slight delay between each side of the Leaf to create gradient effect
for c in bk_color:
    leftLeaf.setFill(c)
    sleep(.205)
    rightLeaf.setFill(c)
    triangle.setFill(c)

#create closing message to appear after all animations are complete
closeMessage = Text(Point(10,1.5), "Click anywhere to close")
closeMessage.setFace("helvetica")
closeMessage.setSize(18)
closeMessage.setStyle("italic")
closeMessage.draw(win)
win.getMouse()
