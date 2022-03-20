class Player:
    
    def __init__(self,name, hand, startingPos):
        self.name = name
        self.deck = hand

    def setPlayerHand(self,hand):
        self.deck = hand
        
    
    
    def getName(self):
        return self.name
    
    def setCurrentPosition(self,pos):
        self.position = pos
    
    def getCurrentPosition(self):
        return self.position
    
    def setStartingPosition(self,startingPos):
        self.startingPosition = startingPos
    
    def getStartingPosition(self):
        return self.startingPosition
    
     
    