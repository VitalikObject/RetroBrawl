from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.LoginFailed import LoginFailed

from Utils.Reader import BSMessageReader


class ClientAction(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.Type = self.read_Vint()

    def process(self):
        if self.Type == 4:
