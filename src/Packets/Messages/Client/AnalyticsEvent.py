from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.KeepAliveOK import KeepAliveOk

from Utils.Reader import BSMessageReader
from database.player import DataBase


class AnalyticsEvent(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.db = DataBase()

    def decode(self):
        self.Type = self.read_string()
        self.Event = self.read_string()

    def process(self):
        print("[INFO] " + self.Type + " " + self.Event)