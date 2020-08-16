from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.GameroomData import GameroomData

from Utils.Reader import BSMessageReader
from database.player import DataBase


class CreateGameroom(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.db = DataBase()

    def decode(self):
        self.read_Vint()
        self.mapID = self.read_Vint()

    def process(self):
        if self.mapID == 1:
            self.player.mapID = 7
        elif self.mapID == 2:
            self.player.mapID = 13
        elif self.mapID == 3:
            self.player.mapID = 1
        elif self.mapID == 4:
            self.player.mapID = 24
        elif self.mapID == 5:
            self.player.mapID = 34
        elif self.mapID == 6:
            self.player.mapID = 58
        elif self.mapID == 7:
        	self.player.mapID = 53
        GameroomData(self.client, self.player).send()