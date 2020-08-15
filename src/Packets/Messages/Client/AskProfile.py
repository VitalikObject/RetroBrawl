from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.PlayerProfile import PlayerProfile

from Utils.Reader import BSMessageReader
from database.player import DataBase


class AskProfile(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.db = DataBase()

    def decode(self):
        pass

    def process(self):
        PlayerProfile(self.client, self.player).send()