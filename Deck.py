'''
Deck
3/16/22 RO
This class will creat a deck of cards consisting of 6 names of people, 6 weapons, and 9 rooms. When initialized the object will set aside 3 random cards that are unique to each category, this will be the cards needed to be guessed to win the game. Finally the deck is shuffled.
The deal function will allow cards to be passed to another player removing them from the top of the deck.
The guess function will take in a users guess as a list of 3 strings to see if they won the game.
'''

from random import shuffle, randint
class Deck:
    def __init__(self):
        #initialize deck: 6 people, 6 weapons, 9 rooms
        self.cards = ["Colonel Mustard", "Professor Plum", "Reverend Green", "Mr. Peacock", " Miss Scarlet", "Mrs. White",
        "Knife", "Candle Stick", "Revolver", "Rope", "Lead Pipe", "Wrench",
        "Hall", "Lounge", "Dining Room", "Kitchen", "Ball Room", "Conservatory", "Billiard Room", "Library", "Study"]

        #create killer set: person, weapon, room
        self.killer = []
        self.killer.append(self.cards.pop(randint(0,5)))
        self.killer.append(self.cards.pop(randint(5,10)))
        self.killer.append(self.cards.pop(randint(10,18)))

        #shuffle deck
        shuffle(self.cards)

    def deal(self, count):
        #deals count number of cards from the top of the deck to a player
        hand = []
        for i in range(0,count):
            hand.append(self.cards.pop(0))
        return(hand)
    
    def guess(self, accusation):
        #takes in a list of accusations to determine if a winner can be crowned
        if len(accusation)== 3:
            winner = set(accusation).issubset(set(self.killer))
            return(winner)
        else:
            print("Incorrect number of items. Try again")
            return(-1)

    def remainder(self):
        if len(self.cards)>0:
            return(self.cards)
        else:
            return(None)
