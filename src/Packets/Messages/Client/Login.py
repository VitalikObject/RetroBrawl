from random import choice
from string import ascii_uppercase
import json
import time

from Logic.Player import Players
from Packets.Messages.Server.LoginOk import LoginOk
from Packets.Messages.Server.OwnHomeData import OwnHomeData
from Utils.reader import CoCMessageReader
from database.player import DataBase
from Utils.Helpers import Helpers

class Login(CoCMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.db = DataBase()

    def decode(self):
        self.player.HighID = self.read_int()
        self.player.LowID = self.read_int()
        self.player.Token = self.read_string()
        self.major = self.read_int()
        self.minor = self.read_int()
        self.build = self.read_int()

    def process(self):
        if self.player.LowID != 0:
            LoginOk(self.client, self.player).send()
            time.sleep(0.2)
            OwnHomeData(self.client, self.player).send()
        else:
            self.player.LowID = 1
            self.player.HighID = 0
            self.player.Token = Helpers.randomStringDigits()
            LoginOk(self.client, self.player).send()
            time.sleep(0.2)
            OwnHomeData(self.client, self.player).send()