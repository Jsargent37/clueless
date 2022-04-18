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
        self.ms_scarlet = Player("Ms_Scarlet", "Miss Scarlet", [0,3])
        self.col_mustart = Player("Col_Mustard", "Col. Mustard", [1,4])
        self.ms_white = Player("Mrs_White", "Mrs. White", [4,3])
        self.mr_green = Player("Mr_Green", "Mr. Green", [4,1])
        self.ms_peacock = Player("Mrs_Peacock", "Ms. Peacock", [3,0])
        self.prof_plum = Player("Prof_Plum", "Professor Plum", [1,0])
        self.set_players = [self.ms_scarlet, self.col_mustart, self.ms_white, self.mr_green, self.ms_peacock, self.prof_plum]

        self.names = ["Ms_Scarlet", "Col_Mustard", "Mrs_White", "Mr_Green" ,"Mrs_Peacock", "Prof_Plum"]

        for i in range(self.total_players):
            self.set_players[i].playing = True
            self.set_players[i].setPlayerHand(self.deck.deal(self.cards_to_deal))
            self.board.blockAndUnblockHallway(self.set_players[i].getCurrentPosition())
        
        self.leftoverCards = self.deck.remainder()

    #Move players on board
    def move(self, location, player):
        player = self.names.index(player)
        #accept a tuple of 2 coordinates and name of player being moved
        legal = self.board.whereCanIMoveTo(self.set_players[player].getCurrentPosition())
        if location in legal:
            #unblock/block hallway if needed
            self.board.blockAndUnblockHallway(self.set_players[player].getCurrentPosition())
            self.board.blockAndUnblockHallway(location)
            #update current position
            self.set_players[player].setCurrentPosition(location)
            return(location)
        else:
            return(False)
    
    #make suggestion , 3 cards they are suggesting. have to move player to where they are being suggested
    def suggestion(self, suggest, playerSuggesting):
        suggestedKiller = suggest[0]
        suggestedWeapon = suggest[1]
        suggestedRoom = suggest[2]
        found = False

        #bring player into room
        for i in self.set_players:
            if i.getName() == suggestedKiller:
                newPosition = playerSuggesting.getCurrentPosition() 
                i.setCurrentPosition = newPosition



        #repeat until a player is able to be disprove suggestion 
        while not found:
            for i in self.set_players:
                if i.getStatus():
                    playerHand = i.getPlayerHand()
                    if  (suggestedKiller in playerHand or suggestedWeapon in playerHand or suggestedRoom in playerHand) and (i.getName() != playerSuggesting.getName()):
                        found = True
                        card = i.disprove(suggest,i.getName(), self.cards_to_deal,playerHand)
                        return card

    def testWinner(self):
        count = 0
        winner = False
        for i in range(self.total_players):
            if self.set_players[i].playing:
                count += 1
        if count == 1:
            winner = True
        return(winner)
                        
    def accuse(self, accusation, player):
        #Accuse will test to see if a players accusation matches the killer scenario for this game. 
        #A boolean will be returned indicating wether they were successful.
        winner = False
        winner = self.deck.guess(accusation)
        player = self.names.index(player)
        if not winner:
            #knocked out for wrong guess
            self.set_players[player].playing = winner
            print("Player Status")
            print(self.set_players[player].playing)
        return(winner) 

'''
def main():
    newGame = Clue(["Jack", "Michelle", "Rylee"])
    
    print()
    print("Winning Accusation:")
    print(newGame.deck.killer)
    print('---------------------------------')
    for i in range(newGame.total_players):
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

    #card = newGame.suggestion(["Mr. Green", "Rope", "Lounge"], newGame.set_players[0])

    #print(card)

#-----------------------------Test Movement---------------------------------------------------------------------
    #Move Miss Scarlet
    print(newGame.board.whereCanIMoveTo(newGame.set_players[0].getCurrentPosition()))
    pos = input('Input positions separate by commas. -1 to end')
    pos = pos.split(',')
    while (int(pos[0])!=-1):
        newLoc=newGame.move((int(pos[0]),int(pos[1])), "Miss Scarlet")
        print("You moved:")
        print(newLoc)
        pos = input('Input positions separate by commas. -1 to end')
        pos = pos.split(',')
    
    #Move Colonel Mustard
    print(newGame.board.whereCanIMoveTo(newGame.set_players[1].getCurrentPosition()))
    pos = input('Input positions separate by commas. -1 to end')
    pos = pos.split(',')
    while int(pos[0])!=-1:
        newLoc=newGame.move((int(pos[0]),int(pos[1])), "Colonel Mustard")
        print("You moved:")
        print(newLoc)
        pos = input('Input positions separate by commas. -1 to end')
        pos = pos.split(',')

#------------------------------Test Accusation--------------------------------------------------------------------
    winner = newGame.accuse(["Mr. Green", "Rope", "Lounge"], "Miss Scarlet")
    print("Winner: ")
    print(winner)
    print('------------------------')
    
    winner = newGame.accuse(["Mr. Green", "Rope", "Lounge"], "Colonel Mustard")
    print("Winner: ")
    print(winner)
    print('------------------------')
#------------------------------Test Knockout Win--------------------------------------------------------------------
    endOfGame = newGame.testWinner()
    print("Game Over?")
    print(endOfGame)

main()
'''