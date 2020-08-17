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
            if self.player.brawlerID == 0:
                DataBase.replaceValue(self, 'shellySkin', self.player.skinID)
            elif self.player.brawlerID == 1:
                DataBase.replaceValue(self, 'coltSkin', self.player.skinID)
            elif self.player.brawlerID == 2:
                DataBase.replaceValue(self, 'bullSkin', self.player.skinID)
            elif self.player.brawlerID == 3:
                DataBase.replaceValue(self, 'brockSkin', self.player.skinID)
            elif self.player.brawlerID == 4:
                DataBase.replaceValue(self, 'ricoSkin', self.player.skinID)
            elif self.player.brawlerID == 5:
                DataBase.replaceValue(self, 'spikeSkin', self.player.skinID)
            elif self.player.brawlerID == 6:
                DataBase.replaceValue(self, 'barleySkin', self.player.skinID)
            elif self.player.brawlerID == 7:
                DataBase.replaceValue(self, 'jessieSkin', self.player.skinID)
            elif self.player.brawlerID == 8:
                DataBase.replaceValue(self, 'nitaSkin', self.player.skinID)
            elif self.player.brawlerID == 9:
                DataBase.replaceValue(self, 'dynamikeSkin', self.player.skinID)
            elif self.player.brawlerID == 10:
                DataBase.replaceValue(self, 'elprimoSkin', self.player.skinID)
            elif self.player.brawlerID == 11:
                DataBase.replaceValue(self, 'mortisSkin', self.player.skinID)
            elif self.player.brawlerID == 12:
                DataBase.replaceValue(self, 'crowSkin', self.player.skinID)
            elif self.player.brawlerID == 13:
                DataBase.replaceValue(self, 'pocoSkin', self.player.skinID)
            elif self.player.brawlerID == 14:
                DataBase.replaceValue(self, 'boSkin', self.player.skinID)
            elif self.player.brawlerID == 15:
                DataBase.replaceValue(self, 'piperSkin', self.player.skinID)
            elif self.player.brawlerID == 16:
                DataBase.replaceValue(self, 'pamSkin', self.player.skinID)
            elif self.player.brawlerID == 17:
                DataBase.replaceValue(self, 'taraSkin', self.player.skinID)
            elif self.player.brawlerID == 18:
                DataBase.replaceValue(self, 'darrylSkin', self.player.skinID)
            elif self.player.brawlerID == 19:
                DataBase.replaceValue(self, 'pennySkin', self.player.skinID)
            elif self.player.brawlerID == 20:
                DataBase.replaceValue(self, 'frankSkin', self.player.skinID)
            elif self.player.brawlerID == 23:
                DataBase.replaceValue(self, 'leonSkin', self.player.skinID)
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