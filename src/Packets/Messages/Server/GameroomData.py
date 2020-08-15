from Utils.Writer import Writer


class GameroomData(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player

    def encode(self):
        self.writeHexa('''01000a0000000000000001b8d9ccc50b0000000f''')
        self.writeVint(self.player.mapID)
        self.writeHexa('''010100006c7da80e8bad''')
        self.writeString("<cff3200>M<cff6500>r<cff9800> <cffcb00>V<cffff00>i<cccff00>t<c99ff00>a<c66ff00>l<c33ff00>i<c01ff00>k</c>")
        self.writeHexa('''03100000070702030000000000''')
        print("[INFO] Message GameroomData has been sent.")
