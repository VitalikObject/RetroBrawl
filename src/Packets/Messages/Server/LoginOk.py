import time

from Utils.Writer import Writer


class LoginOk(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.id = 20104
        self.version = 1

    def encode(self):
        self.writeInt(self.player.HighID)
        self.writeInt(self.player.LowID)
        # HighID, lowID
        self.writeInt(self.player.HighID)
        self.writeInt(self.player.LowID)
        # HighID, lowID
        self.writeString(self.player.Token)  # Token
        self.writeString()
        self.writeString()
        self.writeInt(16)  # MajorVersion
        self.writeInt(167)  # Build
        self.writeInt(1)  # MinorVersion
        self.writeString("prod")  # Environment
        self.writeInt(1) 
        self.writeInt(1)  
        self.writeInt(62) 
        self.writeString()  
        self.writeString() 
        self.writeString()  
        self.writeInt(0)
        self.writeString() 
        self.writeString("IL")
        self.writeString()
        self.writeInt(1)
        self.writeString()  
        self.writeString() 
        self.writeString() 
        self.writeVint(0)
        self.writeString()
        self.writeVint(1)
        print("Message LoginOk has been sent.")