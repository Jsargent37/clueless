'''
3/21/2022
This class represents the player. It initalizes the player with a name, their hand, and the starting position. 
setPlayerHand function takes player's new hand in and set it to players hand
checkSuggestion function takes a deck object and calls guess to to see if suggestion is accurate
setCurrentPosition function takes the new position of where player is and set it to position
getCurrentPosition function returns the player's position
'''

#from Deck import Deck

class Player:
    
    #initalize player with name, hand and their starting position
    def __init__(self, name, startingPos, hand, playing, hand):
        self.name = name
        self.playerHand = hand
        self.hand = []
        self.playing = False
        self.position = startingPos
        self.inplay = False

    #set player new hand
    def setPlayerHand(self,hand):
        self.playerHand = hand
        
    #call deck class to check if accusation is true
    def checkSuggestion(self, suggestedCards):
        return suggestedCards.guess(suggestedCards)
    
    #return player name
    def getName(self):
        return self.name
    
    #set current position
    def setCurrentPosition(self,pos):
        self.position = pos
    
    #return current position
    def getCurrentPosition(self):
        return self.position

    