import json
import string
import random
from tinydb import TinyDB, Query
from Utils.Helpers import Helpers

class DataBase:



    def loadAccount(self):
        db = TinyDB('data.db')
        query = Query()
        user_data = db.search(query.token == str(self.player.Token))
        if user_data:
            self.player.name = user_data[0]["info"]["name"]
            self.player.gems = user_data[0]["info"]["gems"]
            self.player.gold = user_data[0]["info"]["gold"]
            self.player.tickets = user_data[0]["info"]["tickets"]
            self.player.brawlerID = user_data[0]["info"]["brawlerID"]
            self.player.skinID = user_data[0]["info"]["skinID"]
            self.player.trophies = user_data[0]["info"]["trophies"]
            self.player.profileIcon = user_data[0]["info"]["profileIcon"]
            self.player.brawlBoxes = user_data[0]["info"]["brawlBoxes"]
            self.player.bigBoxes = user_data[0]["info"]["bigBoxes"]
            self.player.shellySkin = user_data[0]["info"]["shellySkin"]
            self.player.nitaSkin = user_data[0]["info"]["nitaSkin"]
            self.player.coltSkin = user_data[0]["info"]["coltSkin"]
            self.player.bullSkin = user_data[0]["info"]["bullSkin"]
            self.player.jessieSkin = user_data[0]["info"]["jessieSkin"]
            self.player.brockSkin = user_data[0]["info"]["brockSkin"]
            self.player.dynamikeSkin = user_data[0]["info"]["dynamikeSkin"]
            self.player.boSkin = user_data[0]["info"]["boSkin"]
            self.player.elprimoSkin = user_data[0]["info"]["elprimoSkin"]
            self.player.barleySkin = user_data[0]["info"]["barleySkin"]
            self.player.pocoSkin = user_data[0]["info"]["pocoSkin"]
            self.player.ricoSkin = user_data[0]["info"]["ricoSkin"]
            self.player.darrylSkin = user_data[0]["info"]["darrylSkin"]
            self.player.pennySkin = user_data[0]["info"]["pennySkin"]
            self.player.piperSkin = user_data[0]["info"]["piperSkin"]
            self.player.pamSkin = user_data[0]["info"]["pamSkin"]
            self.player.frankSkin = user_data[0]["info"]["frankSkin"]
            self.player.mortisSkin = user_data[0]["info"]["mortisSkin"]
            self.player.taraSkin = user_data[0]["info"]["taraSkin"]
            self.player.spikeSkin = user_data[0]["info"]["spikeSkin"]
            self.player.crowSkin = user_data[0]["info"]["crowSkin"]
            self.player.leonSkin = user_data[0]["info"]["leonSkin"]




    def createAccount(self):

        db = TinyDB('data.db')

        data = {
            "token": str(self.player.Token),

            "info":
                {
                "name": self.player.name,
                "gems": 99999,
                "gold": 99999,
                "tickets": 99999,
                "brawlerID": 0,
                "skinID": 0,
                "trophies": 99999,
                "profileIcon": 0,
                "brawlBoxes": 99999,
                "bigBoxes": 99999,
                "shellySkin": 0,
                "nitaSkin": 0,
                "coltSkin": 0,
                "bullSkin": 0,
                "jessieSkin": 0,
                "brockSkin": 0,
                "dynamikeSkin": 0,
                "boSkin": 0,
                "elprimoSkin": 0,
                "barleySkin": 0,
                "pocoSkin": 0,
                "ricoSkin": 0,
                "darrylSkin": 0,
                "pennySkin": 0,
                "piperSkin": 0,
                "pamSkin": 0,
                "frankSkin": 0,
                "mortisSkin": 0,
                "taraSkin": 0,
                "spikeSkin": 0,
                "crowSkin": 0,
                "leonSkin": 0

                }

        }

        db.insert(data)





    def replaceValue(self, value_name, new_value):
        db = TinyDB('data.db')
        query = Query()
        data = db.search(query.token == str(self.player.Token))
        user_data = data[0]
        user_data["info"][str(value_name)] = new_value
        db.update(user_data, query.token == str(self.player.Token))