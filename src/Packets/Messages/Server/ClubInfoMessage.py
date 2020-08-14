from Utils.Writer import Writer


class ClubInfoMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24399
        self.player = player

    def encode(self):    
        self.writeHexa('''01011902000000000000029a''')
        self.writeString("Brawl Private Server")
        self.writeHexa('''080003018f9c01000000000002555300''')
        print("[INFO] Message ClubInfoMessage has been sent.")