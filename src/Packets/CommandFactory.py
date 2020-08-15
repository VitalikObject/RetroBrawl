from Utils.Reader import BSMessageReader
from Packets.Messages.Server.ServerBox  import ServerBox

class EndClientTurn(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.player= player
        
    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.commandID = self.read_Vint()

    def process(self):
        if self.commandID == 500:
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.player.boxID = self.read_Vint()
            print("Command ID", self.commandID, "has been handled")
            ServerBox(self.client, self.player).send()
        elif self.commandID >= 0: 
            print("Command ID", self.commandID, "don\'t handled!")