from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.SetNameResponse import SetNameResponse
from database.DataBase import DataBase

from Utils.Reader import BSMessageReader


class SetName(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.db = DataBase()

    def decode(self):
        self.player.name = self.read_string()

    def process(self):
        DataBase.createAccount(self) # create new account
        SetNameResponse(self.client, self.player).send()