'''
3/21/2022
This class represents the player. It initalizes the player with a name, their hand, and the starting position. 
setPlayerHand function takes player's new hand in and set it to players hand
checkSuggestion function takes a deck object and calls guess to to see if suggestion is accurate
setCurrentPosition function takes the new position of where player is and set it to position
getCurrentPosition function returns the player's position
'''

#from Deck import Deck

from operator import truediv


class Player:
    
    #initalize player with name, hand and their starting position
    def __init__(self, name, startingPos):
        self.name = name
        self.playerHand = list
        self.playing = False
        self.position = startingPos

    #set player new hand
    def setPlayerHand(self,hand):
        self.playerHand = hand
    
    def getPlayerHand(self):
        return self.playerHand
        
    #return player name
    def getName(self):
        return self.name
    
    #set current position
    def setCurrentPosition(self,pos):
        self.position = pos
    
    #return current position
    def getCurrentPosition(self):
        return self.position

    def disprove(self, suggest):
        wrongCard = True
        while wrongCard:
            while True:
                try:
                    cardChosen = int(input("Choose a card to show to player to disprove. 0 for Suspect, 1 for Weaspon, 2 for Killer"))  
                    if cardChosen not in range(3):
                        raise Exception("Error: not in range")
                    break
                except:
                    print("Please enter valid number. 0 for Susepct, 1 for Weapon, 2 for Killer")

            print(self.playerHand[cardChosen])
            if (self.playerHand[cardChosen]) == suggest[0] or self.playerHand[cardChosen] == suggest[1] or self.playerHand[cardChosen] == suggest[1]:
                wrongCard = False
                break
            print("Card not in suggested deck")  
        return cardChosen