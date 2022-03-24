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
        self.set_players = [self.ms_scarlet, self.col_mustart, self.ms_white, self.mr_green, self.ms_peacock, self.prof_plum]

        for i in range(self.total_players):
            self.players[i].playing = True
            self.players[i].playerHand = self.deck.deal(self.cards_to_deal)
            self.board.blockAndUnblockHallway(self.players[i].position)
        
        self.leftoverCards = self.deck.remainder()

        
    #Move players on board
    #ryan lee 
    def move(self, location):
        pass
    
    #make suggestion , 3 cards they are suggesting. have to move player to where they are being suggested
    #Michelle
    def suggestion(self, suggest, playerSuggesting):
        self.suggestedKiller = suggest[0]
        self.suggestedWeapon = suggest[1]
        self.suggestedRoom = suggest[2]

        #bring player into room
        for i in self.set_players:
            if i.getName() == self.suggestedKiller:
                self.newPosition = playerSuggesting.getCurrentPosition() 
                i.setCurrentPosition = self.newPosition


        #repeat until a player is able to be disprove suggestion
        while True:
            for i in range(self.set_player):
                if self.set_player.getStatus :
                    self.playerHand = i.getPlayerHand()
                    if self.playerHand[0] == self.suggestedKiller:  
                         #show card to player
                        self.found = True
                        break
                    elif self.playerHand[1] == self.suggestedWeapon:
                         #show card to player
                         self.found = True
                         break                           
                    elif self.playerHand[2] == self.suggestedRoom:
                        self.found = True 
                        break 
            if self.found:
                break

        return self.found

            

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