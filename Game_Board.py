from Room import Rm

class Board:
    def __init__(self):
        self.study = Rm(False, "Study")
        self.hallwaySH = Rm(True, "Hallway to Study or Hall")
        self.hall = Rm(False, "Hall")
        self.hallwayHL = Rm(True, "Hallway to Hall or Lounge")
        self.lounge = Rm(False, "Lounge")
        self.hallwaySL = Rm(True, "Hallway to Study or Library")
        self.hallwayHB = Rm(True, "Hallway to Hall or Billiard Room")
        self.hallwayLD = Rm(True, "Hallway to Lounge or Dining Room")
        self.library = Rm(False, "Library")
        self.hallwayLB = Room(True, "Hallway to Library or Billiard Room")
        self.billiard_room = Room(False, "Billiard Room")
        self.hallwayBD = Room(True, "Hallway to Billiard Room or Dining Room")
        self.dining_room = Room(False, "Dining Room")
        self.hallwayLC = Room(True, "Hallway to Library or Conservatory")
        self.hallwayBB = Room(True, "Hallway to Billiard Room or Ballroom")
        self.hallwayDK = Room(True, "Hallway to Dining Room or Kitchen")
        self.conservatory = Room(False, "Conservatory")
        self.hallwayCB = Room(True, "Hallway to Conservatory or Ballroom")
        self.ballroom = Room(False, "Ballroom")
        self.hallwayBK = Room(True, "Hallway to Ballroom or Kitchen")
        self.kitchen = Room(False, "Kitchen")
    
        self.study.setRoomConnections([0, self.hallwaySL, self.hallwaySH, 0, self.kitchen])
        self.hallwaySH.setRoomConnections([0, 0, self.hall, self.study, 0])
        self.hall.setRoomConnections([0, self.hallwayHB, self.hallwayHL, self.hallwaySH, 0])
        self.hallwayHL.setRoomConnections([0, 0, self.lounge, self.hall, 0])
        self.lounge.setRoomConnections([ 0, self.hallwayLD, 0, self.hallwayHL, self.conservatory])
        self.hallwaySL.setRoomConnections([ self.study, self.library, 0, 0, 0])
        self.hallwayHB.setRoomConnections([ self.hall, self.billiard_room, 0, 0, 0])
        self.hallwayLD.setRoomConnections([ self.lounge, self.dining_room, 0, 0, 0])
        self.library.setRoomConnections([self.hallwaySL, self.hallwayLC, self.hallwayLB, 0, 0])
        self.hallwayLB.setRoomConnections([0, 0, self.billiard_room, self.library, 0])
        self.billiard_room.setRoomConnections([ self.hallwayHB, self.hallwayBB, self.hallwayBD, self.hallwayLB, 0])
        self.hallwayBD.setRoomConnections([ 0, 0, self.dining_room, self.billiard_room, 0])
        self.dining_room.setRoomConnections([self.hallwayLD, self.hallwayDK, 0, self.hallwayBD, 0])
        self.hallwayLC.setRoomConnections([self.library, self.conservatory, 0, 0, 0])
        self.hallwayBB.setRoomConnections([self.billiard_room, self.ballroom, 0, 0, 0])
        self.hallwayDK.setRoomConnections([ self.dining_room, self.kitchen, 0, 0, 0])
        self.conservatory.setRoomConnections([self.hallwayLC, 0, self.hallwayCB, 0, self.lounge])
        self.hallwayCB.setRoomConnections([0, 0, self.ballroom, self.conservatory, 0])
        self.ballroom.setRoomConnections([self.hallwayBB, 0, self.hallwayBK, self.hallwayCB, 0])
        self.hallwayBK.setRoomConnections([0, 0, self.kitchen, self.ballroom, 0])
        self.kitchen.setRoomConnections([ self.hallwayDK, 0, 0, self.hallwayBK, self.study])

    def movesForPlayer(self, playerPosition: Room):
        possibleMoves = []
        for i in range(len(playerPosition.moves)):
            if playerPosition.moves[i] != 0:
                if playerPosition.moves[i].canPlayerEnterRoom() == True:
                    possibleMoves.append(playerPosition.moves[i])
        
        return possibleMoves

def main():
    x = Board()
    playerMoves = x.movesForPlayer(x.billiard_room)

    for i in playerMoves:
        print(i.name)

main()