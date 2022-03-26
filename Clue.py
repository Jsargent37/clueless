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

        self.names = [" Miss Scarlet", "Colonel Mustard", "Mrs. White", "Reverend Green" ,"Mr. Peacock", "Professor Plum"]

        for i in range(self.total_players):
            self.set_players[i].playing = True
            self.set_players[i].setPlayerHand(self.deck.deal(self.cards_to_deal))
            self.board.blockAndUnblockHallway(self.set_players[i].getCurrentPosition())
        
        self.leftoverCards = self.deck.remainder()

    #Move players on board
    def move(self, location, player):
        #accept a list of 2 coordinates and name of player being moved
        legal = self.board.whereCanIMoveTo(location)
        player = self.names.index(player)
        if legal:
            #unblock/block hallway if needed
            self.board.blockAndUnblockHallway(location)
            #update current position
            self.set_players[player].setCurrentPosition(location)
    
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

    def accuse(self, accusation, player):
        winner = False
        winner = self.deck.guess(accusation)
        player = self.names.index(player)

        if not winner:
            #knocked out for wrong guess
            self.set_players[player].playing = winner

        return(winner) 

    def testWinner(self):
        count = 0
        winner = False
        for i in range(self.total_players):
            if self.set_players[i].playing:
                count += 1
        if count > 1:
            winner = True
        return(winner)

def main():
    newGame = Clue(["Jack", "Michelle", "Rylee"])
    
    print()
    print("Winning Accusation:")
    print(newGame.deck.killer)
    print()
    for i in range(len(newGame.set_players)):
        if newGame.set_players[i].playing == True:
            print("Player:")
            print(newGame.set_players[i].getName())
            print("Player's hand:")
            print(newGame.set_players[i].playerHand)
            print("Player's Current Position as Coordinate:")
            print(newGame.set_players[i].getCurrentPosition())
            print("Player's Current Position as Room:")
            print(newGame.board.returnRoom(newGame.set_players[i].getCurrentPosition()))
            print("Player's Possible Moves as Coordinates:")
            playerMoves = newGame.board.whereCanIMoveTo(newGame.set_players[i].getCurrentPosition())
            print(playerMoves)
            print("Player's Possible Moves as Rooms: ")
            playerRooms = []
            for j in range(len(playerMoves)):
                playerRooms.append(newGame.board.returnRoom(playerMoves[j]))
            print(playerRooms)
            print()
    
    print("Excess Cards:")
    print(newGame.leftoverCards)
    print()

main()