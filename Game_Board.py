'''
3/21/2022
This class represents the game board. It intializes a 5x5 array to represent the board and a dictionary that holds the coordinates
that tie each spot on the array to a specific room on the board. The whereCanIMoveTo function returns possible moves to the player
class based on an inputted coordinate. The blockAndUnblockHallway blocks and unblocks hallways when players enter and exit them to
prevent more than one player from entering at a time. Lastly, the returnRoomFunction returns the name of a room based on a provided
coordinate.
'''

class Board:
    def __init__(self):
        ## represents the game board
        self.gameBoard = [[2, 1, 2, 1, 2],
        [1, 0, 1, 0, 1],
        [2, 1, 2, 1, 2],
        [1, 0, 1, 0, 1],
        [2, 1, 2, 1, 2]]

        ##holds the name of rooms on the board using their coordinates as keys
        self.roomsCor = {(0,0):"Study", (0,1):"Hallway", (0,2):"Hall", (0,3):"Hallway", (0,4):"Lounge",
        (1,0):"Hallway", (1,2):"Hallway", (1,4):"Hallway", (2,0):"Library", (2,1):"Hallway", (2,2):"Billiard Room",
        (2,3):"Hallway", (2,4):"Dining Room", (3,0): "Hallway", (3,2): "Hallway", (3,4):"Hallway",
        (4,0):"Conservatory", (4,1):"Hallway", (4,2):"Ballroom", (4,3):"Hallway", (4,4):"Kitchen"}

    ## This function returns possible moves from a provided coordinate
    def whereCanIMoveTo(self, cord):
        i, j = cord[0], cord[1]
        movesCords = []

        ## this section checks to see if a secret passage exists in the room
        if i == 0 and j == 0:
            movesCords.append((4,4))
        elif i == 4 and j == 0:
            movesCords.append((0,4))
        elif i == 0 and j == 4:
            movesCords.append((4,0))
        elif i == 4 and j == 4:
            movesCords.append((0,0))
        
        ##This section checks all directions for adjacent rooms
        if self.gameBoard[i-1][j] == 1 or self.gameBoard[i-1][j] == 2:
            movesCords.append((i-1,j))
        if self.gameBoard[i][j-1] == 1 or self.gameBoard[i][j-1] == 2:
            movesCords.append((i,j-1))
        if self.gameBoard[i+1][j] == 1 or self.gameBoard[i+1][j] == 2:
            movesCords.append((i+1,j))
        if self.gameBoard[i][j+1] == 1 or self.gameBoard[i][j+1] == 2:
            movesCords.append((i,j+1))
        
        ##Then the coordinates for all potential moves is returned
        return movesCords

    ##This function blocks and unblocks hallways
    def blockAndUnblockHallway(self, cord):
        i, j = cord[0], cord[1]
        if self.gameBoard[i][j] == 1:
            self.gameBoard = -1
        elif self.gameBoard[i][j] == -1:
            self.gameBoard = 1

    ##This function returns the name of the room
    def returnRoom(self, cord):
        cord1 = (cord[0], cord[1])
        return self.roomsCor.get(cord1)