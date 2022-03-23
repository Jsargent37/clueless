# clueless
gem install rails --version 7.0.2.3s
card format = [room, weapon, suspect]
player will make accusation, and deck class will check
player will pass other players a suggestion.

import Deck from Deck
import Game_Board from Game_Board
import Player from Player
class Clue:
    def __init__(self, player_names):
        self.deck = Deck()
        self.board = Game_Board()

        self.cards_to_deal = 18//len(player_names)

        #initialize players
        self.ms_scarlet = Player("Miss Scarlet", [3,0])
        self.col_mustart = Player("Col. Mustard", [4,1])
        self.ms_white = Player("Prof. Plum", [1,0])
        self.mr_green = Player("Mr. Green", [2,4])
        self.ms_peacock = Player("Mrs. Peacock", [3,0])
        self.prof_plum = Player("")
        self.cards_to_deal = 

    #Move players on board
    def move(self, location):
        pass
    
    #make suggestion
    def suggestion(self, inquiry):
        pass

    def accuse(self, accusation):
        pass

    def testWinner(self):
        pass




    



        
        



#player1 = Playergame name)

#gem install rails --version 7.0.2.3s
#card format = [room, weapon, suspect]
#player will make accusation, and deck class will check
#player will pass other players a suggestion.
#more comment more comment more comment
