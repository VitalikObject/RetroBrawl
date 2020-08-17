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
                "bigBoxes": 99999
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



