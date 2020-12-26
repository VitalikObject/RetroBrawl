from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.BattleResult import BattleResult
from Packets.Messages.Server.Battle2Result import Battle2Result

from Utils.Reader import BSMessageReader


class BattleEnd(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.GameType = self.read_Vint()
        self.read_Vint()
        self.player.Rank = self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.player.Team = self.read_Vint() #red or blue
        self.read_Vint()

        self.read_string() #Your Name

        self.read_Vint()
        self.Bot1 = self.read_Vint() #bot brawer
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()

        self.Bot1N = self.read_string()

        self.read_Vint()
        self.Bot2 = self.read_Vint() #bot brawer
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()

        self.Bot2N = self.read_string()

        self.read_Vint()
        self.Bot3 = self.read_Vint() #bot brawer
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()

        self.Bot3N = self.read_string()

        self.read_Vint()
        self.Bot4 = self.read_Vint() #bot brawer
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()

        self.Bot4N = self.read_string()

        self.read_Vint()
        self.Bot5 = self.read_Vint() #bot brawer
        self.read_Vint()
        self.read_Vint() #red or blue
        self.read_Vint()

        self.Bot5N = self.read_string()

    def process(self):
        if self.player.Rank != 0:
            BattleResult(self.client, self.player).send()
        else:
            if self.player.Team == 0:
                self.player.Bot1Skin = self.getSkinId(self.Bot1)
                self.player.Bot2Skin = self.getSkinId(self.Bot2)
                self.player.Bot3Skin = self.getSkinId(self.Bot3)
                self.player.Bot4Skin = self.getSkinId(self.Bot4)
                self.player.Bot5Skin = self.getSkinId(self.Bot5)
                self.player.Bot1N = self.Bot1N
                self.player.Bot2N = self.Bot2N
                self.player.Bot3N = self.Bot3N
                self.player.Bot4N = self.Bot4N
                self.player.Bot5N = self.Bot5N
                self.player.Bot1 = self.Bot1
                self.player.Bot2 = self.Bot2
                self.player.Bot3 = self.Bot3
                self.player.Bot4 = self.Bot4
                self.player.Bot5 = self.Bot5
                Battle2Result(self.client, self.player).send()
            else:
                self.player.Bot1Skin = self.getSkinId(self.Bot4)
                self.player.Bot2Skin = self.getSkinId(self.Bot5)
                self.player.Bot3Skin = self.getSkinId(self.Bot3)
                self.player.Bot4Skin = self.getSkinId(self.Bot1)
                self.player.Bot5Skin = self.getSkinId(self.Bot2)
                self.player.Bot1N = self.Bot4N
                self.player.Bot2N = self.Bot5N
                self.player.Bot3N = self.Bot3N
                self.player.Bot4N = self.Bot1N
                self.player.Bot5N = self.Bot2N
                self.player.Bot1 = self.Bot4
                self.player.Bot2 = self.Bot5
                self.player.Bot3 = self.Bot3
                self.player.Bot4 = self.Bot1
                self.player.Bot5 = self.Bot2
                Battle2Result(self.client, self.player).send()

    def getSkinId(self, character):
        if character == 0:
            return 0
        elif character == 1:
            return 1
        elif character == 2:
            return 3
        elif character == 3:
            return 4
        elif character == 4:
            return 9
        elif character == 5:
            return 10
        elif character == 6:
            return 12
        elif character == 7:
            return 13
        elif character == 8:
            return 14
        elif character == 9:
            return 6
        elif character == 10:
            return 7
        elif character == 11:
            return 18
        elif character == 12:
            return 19
        elif character == 13:
            return 21
        elif character == 14:
            return 22
        elif character == 15:
            return 23
        elif character == 16:
            return 24
        elif character == 17:
            return 32
        elif character == 18:
            return 34
        elif character == 19:
            return 41
        elif character == 20:
            return 42
        elif character == 23:
            return 62
