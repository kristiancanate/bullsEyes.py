from graphics import *

bEWin = GraphWin("bullsEyes", 300, 300)
bEWin.setCoords(0, 0, 300, 300)

trgt = Circle(Point(150,150), 100)
trgt.setFill("red")
trgt.setOutline("red")
trgt.draw(bEWin)

bEWin.getMouse()
bEWin.close()
