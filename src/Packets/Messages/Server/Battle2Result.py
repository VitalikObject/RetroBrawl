from Utils.Writer import Writer


class Battle2Result(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player

    def encode(self):
        self.writeVint(1)
        self.writeVint(self.player.Rank)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(32)
        self.writeVint(6)
        
        self.writeString(self.player.name)
        self.writeVint(1)
        self.writeVint(16)
        self.writeVint(self.player.brawlerID)
        self.writeVint(29)
        self.writeVint(self.player.skinID)
        self.writeVint(9999)
        self.writeVint(10)
        self.writeVint(0)
        
        self.writeString(self.player.Bot1N)
        self.writeVint(0)
        self.writeVint(16)
        self.writeVint(self.player.Bot1)
        self.writeVint(29)
        self.writeVint(self.player.Bot1Skin)
        self.writeVint(9999)
        self.writeVint(10)
        self.writeVint(0)
        
        self.writeString(self.player.Bot2N)
        self.writeVint(0)
        self.writeVint(16)
        self.writeVint(self.player.Bot2)
        self.writeVint(29)
        self.writeVint(self.player.Bot2Skin)
        self.writeVint(9999)
        self.writeVint(10)
        self.writeVint(0)
        
        self.writeString(self.player.Bot3N)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(self.player.Bot3)
        self.writeVint(29)
        self.writeVint(self.player.Bot3Skin)
        self.writeVint(9999)
        self.writeVint(10)
        self.writeVint(0)
        
        self.writeString(self.player.Bot4N)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(self.player.Bot4)
        self.writeVint(29)
        self.writeVint(self.player.Bot4Skin)
        self.writeVint(9999)
        self.writeVint(10)
        self.writeVint(0)

        self.writeString(self.player.Bot5N)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(self.player.Bot5)
        self.writeVint(29)
        self.writeVint(self.player.Bot5Skin)
        self.writeVint(9999)
        self.writeVint(10)
        self.writeVint(0)
        
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(28)
        self.writeVint(0)    
        
        #self.writeVint(0)
        
        print("[INFO] Message BattleResult has been sent.")