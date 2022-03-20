class Rm:
    def __init__(self, hallway: bool, name: str):
        self.hallway = hallway
        self.name = name
        self.north = 0
        self.south = 0
        self.east = 0
        self.west = 0
        self.secretPassage = 0
        self.moves = [self.north, self.south, self.east, self.west, self.secretPassage]
        self.players = []
    
    def setRoomConnections(self, connections: list):
        for i in range(len(connections)):
            if type(connections[i]) == Room:
                self.moves[i] = connections[i]


    def canPlayerEnterRoom(self):
        if self.hallway == True and len(self.players) == 0:
            return True
        elif self.hallway == True and len(self.players) > 0:
            return False
        elif self.hallway == False:
            return True

    def playerEnterRoom(self, player):
        if self.canPlayerEnterRoom == True:
            self.players.append(player)
    
    def playerExitsRoom(self, player):
        self.players.remove(player)