from Utils.Writer import Writer
import random

class GameroomData(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player

    def encode(self):
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        if(self.player.roomID == 0):
            self.player.roomID = random.randrange(1, 2147483647)
            self.writeInt(self.player.roomID)
        else:
            self.writeInt(self.player.roomID)
        self.writeVint(1549375096)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(15)
        self.writeVint(self.player.mapID)
        self.writeVint(1)
        self.writeVint(1)
        self.writeInt(27773)
        self.writeInt(2819525549)
        self.writeString(self.player.name)
        self.writeVint(3)
        self.writeVint(16)
        self.writeVint(self.player.brawlerID)
        self.writeVint(0)
        self.writeVint(7)
        self.writeVint(7)
        self.writeVint(2)
        self.writeVint(3)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        print("[INFO] Message GameroomData has been sent.")
