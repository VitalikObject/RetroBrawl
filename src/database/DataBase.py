import json
import string
import random
from Utils.Helpers import Helpers

class DataBase:

    def loadAccount(self):
        with open('data.txt', 'r') as read_data:
            for line in read_data.readlines():
                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))  # loading and dumping json data from file

                if self.player.Token in dict:
                    self.player.name = dict[str(self.player.Token)]['name']  # loading player name from existing account

    def createAccount(self):
        self.player.name = Helpers.randomName(self)
        data = {
            self.player.Token: {

                "name": self.player.name,
                "gems": 99999,
                "gold": 99999,
                "brawlerID": 0,
                "skinID":0
            }
        }

        with open('data.txt', 'a+') as data_file:
            json.dump(data, data_file)  # writing data for new account
            data_file.write('\n')  # writing a new line



    def replaceValue(self, value_name, new_value):
        with open('data.txt', 'r+') as file:

            for line in file.readlines():
                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))  # loading and dumping json data from file
                if self.player.Token in dict:
                    dict[str(self.player.Token)][value_name] = new_value

                with open('data.txt', 'w'):
                    file.write(str(dict))
                    file.write('\n')

        # example usage: replaceValue(self, gems, 7777)



