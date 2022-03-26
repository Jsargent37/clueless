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

    def getStatus(self):
        return self.playing

    #return player name
    def getName(self):
        return self.name
    
    #set current position
    def setCurrentPosition(self,pos):
        self.position = pos
    
    #return current position
    def getCurrentPosition(self):
        return self.position

    #return a card to disprove if another player has made a suggestion
    def disprove(self, suggest,name,numberOfCards,playerHand):
        wrongCard = True
        print("This player is disproving the suggestion: ", name)
        while wrongCard:
            print("disprove while loop")
            while True:
                try:
                    cardChosen = int(input("Choose a card to show to player to disprove"))  
                    if cardChosen not in range(numberOfCards+1):
                        raise Exception("Error: not in range")
                    break
                except:
                    print(" " )

            if (self.playerHand[cardChosen]) == suggest[0] or self.playerHand[cardChosen] == suggest[1] or self.playerHand[cardChosen] == suggest[2]:
                wrongCard = False
                break
        return self.playerHand[cardChosen]