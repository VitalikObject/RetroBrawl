from Utils.Helpers import Helpers
from database.DataBase import DataBase
from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.AllianceEvents.AllianceEditOkMessage import AllianceEditOkMessage
from Packets.Messages.Server.ClubInfoMessage import ClubInfoMessage

from Utils.Reader import BSMessageReader


class EditSettingsMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.clubDescription = self.read_string() # Club description

        self.inf2 = self.read_Vint() # ID Type
        self.badgeID = self.read_Vint() # Club BadgeID

        self.inf4 = self.read_Vint() # ID Type
        self.regionID = self.read_Vint() # Region ID

        self.clubType = self.read_Vint() # Club type || 1 = open, 2 = invite only, 3 = closed
        self.requiredTrophies = self.read_Vint() # Trophy required

    def process(self):
        # Replacing value   
        DataBase.replaceClubValue(self, self.player.ClubID, self.clubDescription, self.badgeID, self.clubType, self.requiredTrophies)
        
        # Sending confirmation and updated data
        AllianceEditOkMessage(self.client, self.player).send()
        ClubInfoMessage(self.client, self.player, self.player.ClubID).send()