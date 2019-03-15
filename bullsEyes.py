from graphics import *

def circle(posX, posY, rad, color):
    trgt = Circle(Point(posX,posY), rad)
    trgt.setFill(color)
    trgt.setOutline(color)
    trgt.draw(bEWin)

def bEye(posX, posY, rad, col1, col2):
    circle(posX, posY, rad, col1)
    circle(posX, posY, rad-20, col2)
    circle(posX, posY, rad-40, col1)
    circle(posX, posY, rad-60, col2)
    circle(posX, posY, rad-80, col1)

bEWin = GraphWin("bullsEyes", 300, 300)
bEWin.setCoords(0, 0, 300, 300)

bEye(150, 150, 100, "red", "white")

bEWin.getMouse()
bEWin.close()
