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
        self.writeString("<cff2400>V<cff4800>i<cff6d00>t<cfe9100>a<cffb600>l<cffda00>i<cfffe00>k<cffff00>O<cdaff00>b<cb6ff00>j<c91ff00>e<c6dfe00>c<c48ff00>t</c> <c4>and</c> <cff002a>P<cff0054>h<cff007f>o<cff00a9>e<cff00d4>n<cfe00fe>i<cff00ff>x<cd400ff>F<caa00ff>i<c7f00ff>r<c5500ff>e</c>")
        self.writeVint(8)
        self.writeVint(0)
        self.writeVint(3)
        self.writeVint(1)
        self.writeVint(9999)
        self.writeInt(0)
        self.writeInt(152915)
        self.writeVint(0)
        print("[INFO] Message ClubInfoMessage has been sent.")