from Utils.Writer import Writer


class ClubInfoMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24399
        self.player = player

    def encode(self):    
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(25)
        self.writeVint(2)
        self.writeInt(0)
        self.writeInt(521)
        self.writeString("Brawl Private Server")
        self.writeVint(8)
        self.writeVint(0)
        self.writeVint(3)
        self.writeVint(1)
        self.writeVint(9999)
        self.writeInt(0)
        self.writeInt(152915)
        self.writeVint(0)
        print("[INFO] Message ClubInfoMessage has been sent.")