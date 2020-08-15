from Utils.Writer import Writer


class ClubProfileMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24301
        self.player = player

    def encode(self):
        self.writeVint(0)
        self.writeInt(0)
        self.writeInt(521)
        self.writeString("Brawl Private Server")
        self.writeVint(8)
        self.writeVint(11)
        self.writeVint(3)
        self.writeVint(1)
        self.writeVint(9999)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString("IL")
        self.writeVint(0)
        self.writeString("Welcome!")
        self.writeVint(1)
        self.writeInt(3182494701)
        self.writeInt(2935259141)
        self.writeVint(7)
        self.writeString("<cff3200>M<cff6500>r<cff9800> <cffcb00>V<cffff00>i<cccff00>t<c99ff00>a<c66ff00>l<c33ff00>i<c01ff00>k</c>")
        self.writeVint(7)
        self.writeVint(2)
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(28)
        self.writeVint(33)
        self.writeVint(0)
        print("[INFO] Message ClubProfileMessage has been sent.")