from Utils.reader import CoCMessageReader
from Packets.Messages.Server.ServerBox  import ServerBox

class Commands(CoCMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.player= player
        
    def decode(self):
        self.read_Vint()
        self.read_Vint()
        #print(Reader.read(50))
        self.read_Vint()
        self.read_Vint()
        self.player.commandID = self.read_Vint()

    def process(self):
        if self.player.commandID == 500:
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.player.boxID = self.read_Vint()
            print("Command ID", self.player.commandID, "has been handled")
            ServerBox(self.client, self.player).send()