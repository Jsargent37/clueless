class Board:
    def __init__(self):
        self.gameBoard = [[2, 1, 2, 1, 2],
        [1, 0, 1, 0, 1],
        [2, 1, 2, 1, 2],
        [1, 0, 1, 0, 1],
        [2, 1, 2, 1, 2]]

        self.roomsCor = {(0,0):"Study", (0,1):"Hallway", (0,2):"Hall", (0,3):"Hallway", (0,4):"Lounge",
        (1,0):"Hallway", (1,2):"Hallway", (1,4):"Hallway", (2,0):"Library", (2,1):"Hallway", (2,2):"Billiard Room",
        (2,3):"Hallway", (2,4):"Dining Room", (3,0): "Hallway", (3,2): "Hallway", (3,4):"Hallway",
        (4,0):"Conservatory", (4,1):"Hallway", (4,2):"Ballroom", (4,3):"Hallway", (4,4):"Kitchen"}

    def whereToMoveTo(self, cord):
        i, j = cord[0], cord[1]
        movesCords = []
        if i == 0 and j == 0:
            movesCords.append((4,4))
        elif i == 4 and j == 0:
            movesCords.append((0,4))
        elif i == 0 and j == 4:
            movesCords.append((4,0))
        elif i == 4 and j == 4:
            movesCords.append((0,0))
        if self.gameBoard[i-1][j] == 1 or self.gameBoard[i-1][j] == 2:
            movesCords.append((i-1,j))
        if self.gameBoard[i][j-1] == 1 or self.gameBoard[i][j-1] == 2:
            movesCords.append((i,j-1))
        if self.gameBoard[i+1][j] == 1 or self.gameBoard[i+1][j] == 2:
            movesCords.append((i+1,j))
        if self.gameBoard[i][j+1] == 1 or self.gameBoard[i][j+1] == 2:
            movesCords.append((i,j+1))
        return movesCords

    def blockAndUnblockHallway(self, cord):
        i, j = cord[0], cord[1]
        if self.gameBoard[i][j] == 1:
            self.gameBoard = -1
        elif self.gameBoard[i][j] == -1:
            self.gameBoard = 1

    def returnRoom(self, cord):
        cord1 = (cord[0], cord[1])
        return self.roomsCor.get(cord1)