from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.GameroomData import GameroomData

from Utils.reader import CoCMessageReader
from database.player import DataBase


class ChangeMap(CoCMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.db = DataBase()

    def decode(self):
        self.read_Vint()
        self.player.mapID = self.read_Vint()

    def process(self):
        GameroomData(self.client, self.player).send()