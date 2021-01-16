from time import daylight
from random import choice
from string import ascii_uppercase
import json

from Packets.Messages.Server.ClubInfoMessage import ClubInfoMessage
from Packets.Messages.Server.ClubProfileMessage import ClubProfileMessage
#from Packets.Messages.Server.Alliance.AllianceStreamMessage import AllianceStreamMessage
from Packets.Messages.Server.AllianceEvents.AllianceJoinOkMessage import AllianceJoinOkMessage

from database.DataBase import DataBase
from Utils.Helpers import Helpers

from Utils.Reader import BSMessageReader


class CreateClubMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        # ClubID
        self.clubHighID = 0
        self.clubLowID = Helpers.randomClubID(self)

        # Info
        self.clubName           = self.read_string()    # Club name 
        self.clubdescription    = self.read_string()    # Club description

        # Badge
        self.BadgeIdentifier    = self.read_Vint()      # Badge Identifier
        self.clubbadgeID        = self.read_Vint()      # BadgeID

        # Region
        self.RegionIdentifier   = self.read_Vint()      # Region Identifier
        self.clubregionID       = self.read_Vint()      # RegionID 

        # Settings
        self.clubtype           = self.read_Vint()      # Type
        self.clubtrophiesneeded = self.read_Vint()      # Trophy required

    def process(self):
        DataBase.replaceValue(self, 'clubLowID', self.clubLowID)
        self.player.ClubID = self.clubLowID
        DataBase.replaceValue(self, 'clubRole', 2)
        self.player.ClubRole = 2

        # Club creation
        DataBase.createClub(self, self.clubLowID)

        # Club data
        AllianceJoinOkMessage(self.client, self.player).send()
        ClubInfoMessage(self.client, self.player, self.clubLowID).send()
        #AllianceStreamMessage(self.client, self.player, self.clubLowID, 0).send()