from Utils.Writer import Writer


class BattleResult(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player

    def encode(self):
        self.writeVint(2)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeInt(8193)
        self.writeString(self.player.name)
        self.writeVint(1)
        self.writeVint(16)
        self.writeVint(self.player.brawlerID)
        self.writeVint(29)
        self.writeVint(self.player.skinID)
        self.writeVint(9999)
        self.writeVint(10)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(28)
        self.writeVint(0)
        self.writeVint(0)
        print("[INFO] Message BattleResult has been sent.")