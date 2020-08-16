from Utils.Writer import Writer
import random
from database.DataBase import DataBase

class ServerBox(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        reward_list = [2 , 3 , 8]
        if self.player.boxID == 5:
            self.writeVint(203)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(10)
            self.writeVint(2)
            GoldValue = random.randrange(1, 1000)
            self.writeVint(GoldValue)

            newGold = self.player.gold + GoldValue
            DataBase.replaceValue(self, 'gold', newGold)

            self.writeVint(0)
            self.writeVint(7)
            self.writeVint(0)
            self.writeVint(0)
            value = random.randrange(1, 20)
            self.writeVint(value)
            self.writeVint(0)
            reward = random.choice(reward_list)
            self.writeVint(reward)

            if reward == 8:
                newGems = self.player.gems + value
                DataBase.replaceValue(self, 'gems', newGems)
            elif reward == 3:
                newTickets = self.player.tickets + value
                DataBase.replaceValue(self, 'tickets', newTickets)     

            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(-1)
            self.writeVint(-1)
            self.writeVint(0)
            self.writeVint(0)
        if self.player.boxID == 4:
            self.writeVint(203)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(12)
            self.writeVint(2)
            GoldValue = random.randrange(1, 2500)
            self.writeVint(GoldValue)

            newGold = self.player.gold + GoldValue
            DataBase.replaceValue(self, 'gold', newGold)

            self.writeVint(0)
            self.writeVint(7)
            self.writeVint(0)
            self.writeVint(0)
            value = random.randrange(1, 50)
            self.writeVint(value)
            self.writeVint(0)
            reward = random.choice(reward_list)
            self.writeVint(reward)

            if reward == 8:
                newGems = self.player.gems + value
                DataBase.replaceValue(self, 'gems', newGems)
            elif reward == 3:
                newTickets = self.player.tickets + value
                DataBase.replaceValue(self, 'tickets', newTickets)

            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(-1)
            self.writeVint(-1)
            self.writeVint(0)
            self.writeVint(0)
        if self.player.boxID == 3:
            self.writeVint(203)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(11)
            self.writeVint(2)

            GoldValue = random.randrange(1, 5000)
            self.writeVint(GoldValue)

            newGold = self.player.gold + GoldValue
            DataBase.replaceValue(self, 'gold', newGold)

            self.writeVint(0)
            self.writeVint(7)
            self.writeVint(0)
            self.writeVint(0)
            value = random.randrange(1, 100)
            self.writeVint(value)
            self.writeVint(0)
            reward = random.choice(reward_list)
            self.writeVint(reward)

            if reward == 8:
                newGems = self.player.gems + value
                DataBase.replaceValue(self, 'gems', newGems)
            elif reward == 3:
                newTickets = self.player.tickets + value
                DataBase.replaceValue(self, 'tickets', newTickets)

            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(-1)
            self.writeVint(-1)
            self.writeVint(0)
            self.writeVint(0)
        if self.player.boxID == 1:
            self.writeVint(203)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(12)
            self.writeVint(2)

            GoldValue = random.randrange(1, 2500)
            self.writeVint(GoldValue)

            newGold = self.player.gold + GoldValue
            DataBase.replaceValue(self, 'gold', newGold)

            self.writeVint(0)
            self.writeVint(7)
            self.writeVint(0)
            self.writeVint(0)
            value = random.randrange(1, 50)
            self.writeVint(value)
            self.writeVint(0)
            reward = random.choice(reward_list)
            self.writeVint(reward)

            if reward == 8:
                newGems = self.player.gems + value
                DataBase.replaceValue(self, 'gems', newGems)
            elif reward == 3:
                newTickets = self.player.tickets + value
                DataBase.replaceValue(self, 'tickets', newTickets)

            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(-1)
            self.writeVint(-1)
            self.writeVint(0)
            self.writeVint(0)