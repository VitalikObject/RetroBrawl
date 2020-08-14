from Utils.Writer import Writer


class ClubProfileMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24301
        self.player = player

    def encode(self):
        self.writeHexa('''00000000000000029a''')
        self.writeString("Brawl Private Server")
        self.writeHexa('''080b03018f9c010000000000025553000000002c676f20746f207777772e6c776172622e636f6d20666f7220746865206c617465737420757064617465732021010000eecf2e9ff7070000000d7777772e6c776172622e636f6d02008f9c0100001c2100''')
        print("[INFO] Message ClubProfileMessage has been sent.")