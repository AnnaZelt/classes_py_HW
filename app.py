class Peon:
    color = ""
    position = [None, None]

class Queen:
    color = ""
    position = [None, None] 

def move(peon):
    peon = Peon()
    peon.position = [int(input()),int(input())]
    redraw()

def redraw():
    pass

def getKilled(peon):
    peon = Peon()
    peon.color = ""
    peon.position = [None, None]

def Crowned(qPeon):
    qPeon = Queen()