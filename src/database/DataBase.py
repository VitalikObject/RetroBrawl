import json
import string
import random
from Utils.Helpers import Helpers

class DataBase:

    def loadAccount(self):
        with open('data.db', 'r') as read_data:
            for line in read_data.readlines():

                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))  # loading and dumping json data from file

                if self.player.Token in dict:
                    self.player.name = dict[str(self.player.Token)]["name"]
                    self.player.gems = dict[str(self.player.Token)]["gems"]
                    self.player.gold = dict[str(self.player.Token)]["gold"]
                    self.player.tickets = dict[str(self.player.Token)]["tickets"]
                    self.player.brawlerID = dict[str(self.player.Token)]["brawlerID"]
                    self.player.skinID = dict[str(self.player.Token)]["skinID"]
                    self.player.profileIcon = dict[str(self.player.Token)]["profileIcon"]
                    self.player.brawlBoxes = dict[str(self.player.Token)]["brawlBoxes"]
                    self.player.bigBoxes = dict[str(self.player.Token)]["bigBoxes"]
                    self.player.shellySkin = dict[str(self.player.Token)]["shellySkin"]
                    self.player.nitaSkin = dict[str(self.player.Token)]["nitaSkin"]
                    self.player.coltSkin = dict[str(self.player.Token)]["coltSkin"]
                    self.player.bullSkin = dict[str(self.player.Token)]["bullSkin"]
                    self.player.jessieSkin = dict[str(self.player.Token)]["jessieSkin"]
                    self.player.brockSkin = dict[str(self.player.Token)]["brockSkin"]
                    self.player.dynamikeSkin = dict[str(self.player.Token)]["dynamikeSkin"]
                    self.player.boSkin = dict[str(self.player.Token)]["boSkin"]
                    self.player.elprimoSkin = dict[str(self.player.Token)]["elprimoSkin"]
                    self.player.barleySkin = dict[str(self.player.Token)]["barleySkin"]
                    self.player.pocoSkin = dict[str(self.player.Token)]["pocoSkin"]
                    self.player.ricoSkin = dict[str(self.player.Token)]["ricoSkin"]
                    self.player.darrylSkin = dict[str(self.player.Token)]["darrylSkin"]
                    self.player.pennySkin = dict[str(self.player.Token)]["pennySkin"]
                    self.player.piperSkin = dict[str(self.player.Token)]["piperSkin"]
                    self.player.pamSkin = dict[str(self.player.Token)]["pamSkin"]
                    self.player.frankSkin = dict[str(self.player.Token)]["frankSkin"]
                    self.player.mortisSkin = dict[str(self.player.Token)]["mortisSkin"]
                    self.player.taraSkin = dict[str(self.player.Token)]["taraSkin"]
                    self.player.spikeSkin = dict[str(self.player.Token)]["spikeSkin"]
                    self.player.crowSkin = dict[str(self.player.Token)]["crowSkin"]
                    self.player.leonSkin = dict[str(self.player.Token)]["leonSkin"]

    def createAccount(self):
        data = {
            self.player.Token: {

                "name": self.player.name,
                "gems": 99999,
                "gold": 99999,
                "tickets": 99999,
                "brawlerID": 0,
                "skinID": 0,
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

        with open('data.db', 'a+') as data_file:
            json.dump(data, data_file)  # writing data for new account
            data_file.write('\n')  # writing a new line



    def replaceValue(self, value_name, new_value):
        with open('data.db', 'r+') as file:
            list = []

            for line in file.readlines():
                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))  # loading and dumping json data from file
                if self.player.Token in dict:
                    dict[str(self.player.Token)][str(value_name)] = new_value
                list.append(dict)
                file.close()

        with open('data.db', 'w') as o:
            for i in list:
                o.write(str(i).replace("'", '"') + '\n')
            o.close()




        # example usage: replaceValue(self, 'gems', 7777)



