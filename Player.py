class Player:
    
    def __init__(self,name, hand, startingPos):
        self.name = name
        self.deck = hand

    def setPlayerHand(self,hand):
        self.deck = hand
        
    def makeSuggestion(self,deck):

        suggestion_weapon = deck[0]
        suggestion_room = deck[1]
        suggestion_suspect = deck[2]
        suggestion = [suggestion_suspect, suggestion_room, suggestion_weapon]
        return self.suggestion
    
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
    
     
    