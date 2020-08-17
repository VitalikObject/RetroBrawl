from Utils.Reader import BSMessageReader
from Packets.Messages.Server.ServerBox  import ServerBox
from Packets.Messages.Server.GameroomData  import GameroomData
from database.DataBase import DataBase

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
        if self.commandID == 505:
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.player.profileIcon = self.read_Vint()
            DataBase.replaceValue(self, 'profileIcon', self.player.profileIcon)
            print("Command ID", self.commandID, "has been handled")
        if self.commandID == 506:
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.player.skinID = self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.player.brawlerID = self.read_Vint()
            DataBase.replaceValue(self, 'skinID', self.player.skinID)
            DataBase.replaceValue(self, 'brawlerID', self.player.brawlerID)
            if(self.player.roomID != 0):
            	GameroomData(self.client, self.player).send()
            print("Command ID", self.commandID, "has been handled")
        if self.commandID == 521:
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.gold = self.read_Vint()
            if self.gold == 0:
                newGold = self.player.gold + 150
                newGems = self.player.gems - 20
                DataBase.replaceValue(self, 'gold', newGold)
                DataBase.replaceValue(self, 'gems', newGems)
            elif self.gold == 1:
                newGold = self.player.gold + 400
                newGems = self.player.gems - 50
                DataBase.replaceValue(self, 'gold', newGold)
                DataBase.replaceValue(self, 'gems', newGems)
            elif self.gold == 2:
                newGold = self.player.gold + 1200
                newGems = self.player.gems - 140
                DataBase.replaceValue(self, 'gold', newGold)
                DataBase.replaceValue(self, 'gems', newGems)
        elif self.commandID >= 0: 
            print("Command ID", self.commandID, "don\'t handled!")