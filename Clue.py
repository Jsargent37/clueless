from Deck import Deck
from Game_Board import Board
from Player import Player
class Clue:
    def __init__(self, player_names):
        self.total_players = len(player_names)

        self.deck = Deck()
        self.board = Board()

        self.cards_to_deal = 18//self.total_players

        #initialize players
        self.ms_scarlet = Player("Miss Scarlet", [0,3])
        self.col_mustart = Player("Col. Mustard", [1,4])
        self.ms_white = Player("Mrs. White", [4,3])
        self.mr_green = Player("Mr. Green", [4,1])
        self.ms_peacock = Player("Mrs. Peacock", [3,0])
        self.prof_plum = Player("Prof. Plum", [1,0])

        for i in range(self.total_players):
            ## players need to be set to true based on number of players
            ## players need cards

    #Move players on board
    #ryan lee 
    def move(self, location):
        pass
    
    #make suggestion , 3 cards they are suggesting. have to move player to where they are being suggested
    #Michelle
    def suggestion(self, suggest):
        Player.suggestion
        #loop here to disprove suggestion

    def accuse(self, accusation):
        winner = False
        winner = self.deck.guess(accusation)
        return(winner) 

    #rylee
    def testWinner(self):
        pass




    



        
        



#player1 = Playergame name)

#gem install rails --version 7.0.2.3s
#card format = [room, weapon, suspect]
#player will make accusation, and deck class will check
#player will pass other players a suggestion.
#more comment more comment more comment