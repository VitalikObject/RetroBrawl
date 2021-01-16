from random import choice
from string import ascii_uppercase
import json

from database.DataBase import DataBase
from Logic.Player import Players
from Packets.Messages.Server.ClubProfileMessage import ClubProfileMessage

from Utils.Reader import BSMessageReader


class AskClubData(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.clubHighID = self.read_int()
        self.clubLowID = self.read_int()

    def process(self):
        ClubProfileMessage(self.client, self.player, self.clubLowID).send()