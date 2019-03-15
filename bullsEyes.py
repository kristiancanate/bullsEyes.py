from graphics import *

def circle(posX, posY, rad, color):
    trgt = Circle(Point(posX,posY), rad)
    trgt.setFill(color)
    trgt.setOutline(color)
    trgt.draw(bEWin)

bEWin = GraphWin("bullsEyes", 300, 300)
bEWin.setCoords(0, 0, 300, 300)

circle(150, 150, 100, "red")

bEWin.getMouse()
bEWin.close()
