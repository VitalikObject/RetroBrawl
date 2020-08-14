from Utils.Writer import Writer


class GameroomData(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player

    def encode(self):
        self.writeHexa('''01000a0000000000000001b8d9ccc50b0000000f07010100006c7da80e8bad''')
        self.writeString("Mr Vitalik")
        self.writeHexa('''03100000070702030000000000''')
        print("[INFO] Message GameroomData has been sent.")
