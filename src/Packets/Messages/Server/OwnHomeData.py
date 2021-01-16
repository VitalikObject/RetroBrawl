from Utils.Writer import Writer
from database.DataBase import DataBase


class OwnHomeData(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        DataBase.loadAccount(self) # load account
        self.writeVint(2019053)
        self.writeVint(75980)
        self.writeVint(self.player.trophies)

        self.writeVint(self.player.trophies)
        self.writeVint(0)
        self.writeVint(99)

        self.writeVint(99999)
        self.writeVint(28)
        self.writeVint(self.player.profileIcon)

        self.writeVint(9)
        self.writeVint(0)
        self.writeVint(2)
        self.writeVint(3)
        self.writeVint(5)
        self.writeVint(6)
        self.writeVint(7)
        self.writeVint(8)
        self.writeVint(9)
        self.writeVint(10)

        self.writeVint(22)
        self.writeVint(29)
        self.writeVint(self.player.shellySkin)
        self.writeVint(29)
        self.writeVint(self.player.nitaSkin)
        self.writeVint(29)
        self.writeVint(self.player.coltSkin)
        self.writeVint(29)
        self.writeVint(self.player.bullSkin)
        self.writeVint(29)
        self.writeVint(self.player.jessieSkin)
        self.writeVint(29)
        self.writeVint(self.player.brockSkin)
        self.writeVint(29)
        self.writeVint(self.player.dynamikeSkin)
        self.writeVint(29)
        self.writeVint(self.player.boSkin)
        self.writeVint(29)
        self.writeVint(self.player.elprimoSkin)
        self.writeVint(29)
        self.writeVint(self.player.barleySkin)
        self.writeVint(29)
        self.writeVint(self.player.pocoSkin)
        self.writeVint(29)
        self.writeVint(self.player.ricoSkin)
        self.writeVint(29)
        self.writeVint(self.player.darrylSkin)
        self.writeVint(29)
        self.writeVint(self.player.pennySkin)
        self.writeVint(29)
        self.writeVint(self.player.piperSkin)
        self.writeVint(29)
        self.writeVint(self.player.pamSkin)
        self.writeVint(29)
        self.writeVint(self.player.frankSkin)
        self.writeVint(29)
        self.writeVint(self.player.mortisSkin)
        self.writeVint(29)
        self.writeVint(self.player.taraSkin)
        self.writeVint(29)
        self.writeVint(self.player.spikeSkin)
        self.writeVint(29)
        self.writeVint(self.player.crowSkin)
        self.writeVint(29)
        self.writeVint(self.player.leonSkin)

        self.writeVint(144)
        self.writeVint(29)
        self.writeVint(0)
        self.writeVint(29)
        self.writeVint(1)
        self.writeVint(29)
        self.writeVint(2)
        self.writeVint(29)
        self.writeVint(3)
        self.writeVint(29)
        self.writeVint(4)
        self.writeVint(29)
        self.writeVint(5)
        self.writeVint(29)
        self.writeVint(6)
        self.writeVint(29)
        self.writeVint(7)
        self.writeVint(29)
        self.writeVint(8)
        self.writeVint(29)
        self.writeVint(9)
        self.writeVint(29)
        self.writeVint(10)
        self.writeVint(29)
        self.writeVint(11)
        self.writeVint(29)
        self.writeVint(12)
        self.writeVint(29)
        self.writeVint(13)
        self.writeVint(29)
        self.writeVint(14)
        self.writeVint(29)
        self.writeVint(15)
        self.writeVint(29)
        self.writeVint(16)
        self.writeVint(29)
        self.writeVint(17)
        self.writeVint(29)
        self.writeVint(18)
        self.writeVint(29)
        self.writeVint(19)
        self.writeVint(29)
        self.writeVint(20)
        self.writeVint(29)
        self.writeVint(21)
        self.writeVint(29)
        self.writeVint(22)
        self.writeVint(29)
        self.writeVint(23)
        self.writeVint(29)
        self.writeVint(24)
        self.writeVint(29)
        self.writeVint(25)
        self.writeVint(29)
        self.writeVint(26)
        self.writeVint(29)
        self.writeVint(27)
        self.writeVint(29)
        self.writeVint(28)
        self.writeVint(29)
        self.writeVint(29)
        self.writeVint(29)
        self.writeVint(30)
        self.writeVint(29)
        self.writeVint(31)
        self.writeVint(29)
        self.writeVint(32)
        self.writeVint(29)
        self.writeVint(33)
        self.writeVint(29)
        self.writeVint(34)
        self.writeVint(29)
        self.writeVint(35)
        self.writeVint(29)
        self.writeVint(36)
        self.writeVint(29)
        self.writeVint(37)
        self.writeVint(29)
        self.writeVint(38)
        self.writeVint(29)
        self.writeVint(39)
        self.writeVint(29)
        self.writeVint(40)
        self.writeVint(29)
        self.writeVint(41)
        self.writeVint(29)
        self.writeVint(42)
        self.writeVint(29)
        self.writeVint(43)
        self.writeVint(29)
        self.writeVint(44)
        self.writeVint(29)
        self.writeVint(45)
        self.writeVint(29)
        self.writeVint(46)
        self.writeVint(29)
        self.writeVint(47)
        self.writeVint(29)
        self.writeVint(48)
        self.writeVint(29)
        self.writeVint(49)
        self.writeVint(29)
        self.writeVint(50)
        self.writeVint(29)
        self.writeVint(51)
        self.writeVint(29)
        self.writeVint(52)
        self.writeVint(29)
        self.writeVint(53)
        self.writeVint(29)
        self.writeVint(54)
        self.writeVint(29)
        self.writeVint(55)
        self.writeVint(29)
        self.writeVint(56)
        self.writeVint(29)
        self.writeVint(57)
        self.writeVint(29)
        self.writeVint(58)
        self.writeVint(29)
        self.writeVint(59)
        self.writeVint(29)
        self.writeVint(60)
        self.writeVint(29)
        self.writeVint(61)
        self.writeVint(29)
        self.writeVint(62)
        self.writeVint(29)
        self.writeVint(63)
        self.writeVint(29)
        self.writeVint(64)
        self.writeVint(29)
        self.writeVint(65)
        self.writeVint(29)
        self.writeVint(66)
        self.writeVint(29)
        self.writeVint(67)
        self.writeVint(29)
        self.writeVint(68)
        self.writeVint(29)
        self.writeVint(69)
        self.writeVint(29)
        self.writeVint(70)
        self.writeVint(29)
        self.writeVint(71)
        self.writeVint(29)
        self.writeVint(72)
        self.writeVint(29)
        self.writeVint(73)
        self.writeVint(29)
        self.writeVint(74)
        self.writeVint(29)
        self.writeVint(75)
        self.writeVint(29)
        self.writeVint(76)
        self.writeVint(29)
        self.writeVint(77)
        self.writeVint(29)
        self.writeVint(78)
        self.writeVint(29)
        self.writeVint(79)
        self.writeVint(29)
        self.writeVint(80)
        self.writeVint(29)
        self.writeVint(81)
        self.writeVint(29)
        self.writeVint(82)
        self.writeVint(29)
        self.writeVint(83)
        self.writeVint(29)
        self.writeVint(84)
        self.writeVint(29)
        self.writeVint(85)
        self.writeVint(29)
        self.writeVint(86)
        self.writeVint(29)
        self.writeVint(87)
        self.writeVint(29)
        self.writeVint(88)
        self.writeVint(29)
        self.writeVint(89)
        self.writeVint(29)
        self.writeVint(90)
        self.writeVint(29)
        self.writeVint(91)
        self.writeVint(29)
        self.writeVint(92)
        self.writeVint(29)
        self.writeVint(93)
        self.writeVint(29)
        self.writeVint(94)
        self.writeVint(29)
        self.writeVint(95)
        self.writeVint(29)
        self.writeVint(96)
        self.writeVint(29)
        self.writeVint(97)
        self.writeVint(29)
        self.writeVint(98)
        self.writeVint(29)
        self.writeVint(99)
        self.writeVint(29)
        self.writeVint(100)
        self.writeVint(29)
        self.writeVint(101)
        self.writeVint(29)
        self.writeVint(102)
        self.writeVint(29)
        self.writeVint(103)
        self.writeVint(29)
        self.writeVint(104)
        self.writeVint(29)
        self.writeVint(105)
        self.writeVint(29)
        self.writeVint(106)
        self.writeVint(29)
        self.writeVint(107)
        self.writeVint(29)
        self.writeVint(108)
        self.writeVint(29)
        self.writeVint(109)
        self.writeVint(29)
        self.writeVint(110)
        self.writeVint(29)
        self.writeVint(111)
        self.writeVint(29)
        self.writeVint(112)
        self.writeVint(29)
        self.writeVint(113)
        self.writeVint(29)
        self.writeVint(114)
        self.writeVint(29)
        self.writeVint(115)
        self.writeVint(29)
        self.writeVint(116)
        self.writeVint(29)
        self.writeVint(117)
        self.writeVint(29)
        self.writeVint(118)
        self.writeVint(29)
        self.writeVint(119)
        self.writeVint(29)
        self.writeVint(120)
        self.writeVint(29)
        self.writeVint(121)
        self.writeVint(29)
        self.writeVint(122)
        self.writeVint(29)
        self.writeVint(123)
        self.writeVint(29)
        self.writeVint(124)
        self.writeVint(29)
        self.writeVint(125)
        self.writeVint(29)
        self.writeVint(126)
        self.writeVint(29)
        self.writeVint(127)
        self.writeVint(29)
        self.writeVint(128)
        self.writeVint(29)
        self.writeVint(129)
        self.writeVint(29)
        self.writeVint(130)
        self.writeVint(29)
        self.writeVint(131)
        self.writeVint(29)
        self.writeVint(132)
        self.writeVint(29)
        self.writeVint(133)
        self.writeVint(29)
        self.writeVint(134)
        self.writeVint(29)
        self.writeVint(135)
        self.writeVint(29)
        self.writeVint(136)
        self.writeVint(29)
        self.writeVint(137)
        self.writeVint(29)
        self.writeVint(138)
        self.writeVint(29)
        self.writeVint(139)
        self.writeVint(29)
        self.writeVint(140)
        self.writeVint(29)
        self.writeVint(141)
        self.writeVint(29)
        self.writeVint(142)
        self.writeVint(29)
        self.writeVint(143)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0) #"token limit reached message" if value is 1
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(248791)
        self.writeVint(8)
        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(2)
        self.writeInt(140)
        self.writeVint(2)
        self.writeVint(1140)
        self.writeVint(0)
        self.writeVint(self.player.tickets) #Tickets
        self.writeVint(-21)

        self.writeVint(16)
        self.writeVint(self.player.brawlerID) #Selected Brawler

        self.writeString("IL")
        self.writeVint(0)
        self.writeVint(2019053)
        self.writeVint(100)
        self.writeVint(10)

        self.writeVint(30)
        self.writeVint(3)
        self.writeVint(80)
        self.writeVint(10)
        self.writeVint(50)
        self.writeVint(1000)

        self.writeVint(500)
        self.writeVint(50)
        self.writeVint(999900)
        self.writeVint(6)
        self.writeVint(0)
        self.writeVint(30)
        self.writeVint(80)
        self.writeVint(170)
        self.writeVint(350)
        self.writeVint(0)
        self.writeVint(7)
        self.writeVint(1)
        self.writeVint(2)
        self.writeVint(3)
        self.writeVint(4)
        self.writeVint(5)
        self.writeVint(6)
        self.writeVint(7)
        self.writeVint(7)
        self.writeVint(-133000102)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(75992)
        self.writeVint(10)
        self.writeVint(15)
        self.writeVint(7)
        self.writeVint(3)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(-133000102)
        self.writeVint(2)
        self.writeVint(0)
        self.writeVint(75992)
        self.writeVint(10)
        self.writeVint(15)
        self.writeVint(13)
        self.writeVint(3)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(-133000102)
        self.writeVint(3)
        self.writeVint(0)
        self.writeVint(75992)
        self.writeVint(10)
        self.writeVint(15)
        self.writeVint(1)
        self.writeVint(3)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(-133000102)
        self.writeVint(4)
        self.writeVint(0)
        self.writeVint(75992)
        self.writeVint(10)
        self.writeVint(15)
        self.writeVint(24)
        self.writeVint(3)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(-133000102)
        self.writeVint(5)
        self.writeVint(0)
        self.writeVint(75992)
        self.writeVint(10)
        self.writeVint(15)
        self.writeVint(34)
        self.writeVint(3)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(-133000102)
        self.writeVint(6)
        self.writeVint(0)
        self.writeVint(75992)
        self.writeVint(10)
        self.writeVint(15)
        self.writeVint(58)
        self.writeVint(3)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(-133000102)
        self.writeVint(7)
        self.writeVint(0)
        self.writeVint(75992)
        self.writeVint(10)
        self.writeVint(15)
        self.writeVint(53)
        self.writeVint(3)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(8)
        self.writeVint(20)
        self.writeVint(35)
        self.writeVint(75)

        self.writeVint(140)
        self.writeVint(290)
        self.writeVint(480)
        self.writeVint(800)
        self.writeVint(1250)

        self.writeVint(8)
        self.writeVint(1)
        self.writeVint(2)
        self.writeVint(3)
        self.writeVint(4)
        self.writeVint(5)
        self.writeVint(10)
        self.writeVint(15)
        self.writeVint(20)

        self.writeVint(3)
        self.writeVint(10)

        self.writeVint(30)
        self.writeVint(80)

        self.writeVint(3)
        self.writeVint(6)
        self.writeVint(20)
        self.writeVint(60)

        self.writeVint(3)

        self.writeVint(20)
        self.writeVint(50)
        self.writeVint(140)

        self.writeVint(3)

        self.writeVint(150)
        self.writeVint(400)
        self.writeVint(1200)

        self.writeVint(2)
        self.writeVint(200)
        self.writeVint(20)
        self.writeVint(8640)
        self.writeVint(10)
        self.writeVint(5)
        self.writeVint(6)
        self.writeVint(50)
        self.writeVint(604800)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)

        self.writeInt(0)
        self.writeInt(1)

        self.writeVint(0)
        self.writeVint(-1)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(self.player.LowID)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        if self.player.name is None:
            self.writeString("Guest") # player name
            self.writeVint(0)
            DataBase.createAccount(self) # create new account
        else:
            self.writeString(self.player.name) # player name
            self.writeVint(1)
        self.writeString()
        self.writeVint(8)

        self.writeVint(25)
        self.writeVint(23)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(4)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(8)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(12)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(16)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(20)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(24)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(28)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(32)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(36)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(40)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(44)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(48)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(52)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(56)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(60)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(64)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(68)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(72)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(95)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(100)
        self.writeVint(1)
        self.writeVint(23)
        self.writeVint(115)
        self.writeVint(1)

        self.writeVint(5)
        self.writeVint(1)
        self.writeVint(self.player.brawlBoxes) #Brawl Box tokens
        self.writeVint(5)
        self.writeVint(8)
        self.writeVint(self.player.gold) #Gold
        self.writeVint(5)
        self.writeVint(9)
        self.writeVint(self.player.bigBoxes) #Big Box tokens

        self.writeVint(23)
        self.writeVint(16)
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(1)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(2)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(3)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(4)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(5)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(6)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(7)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(8)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(9)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(10)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(11)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(12)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(13)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(14)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(15)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(16)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(17)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(18)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(19)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(20)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(22)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(23)
        self.writeVint(9999)

        self.writeVint(23)
        self.writeVint(16)
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(1)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(2)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(3)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(4)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(5)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(6)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(7)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(8)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(9)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(10)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(11)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(12)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(13)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(14)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(15)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(16)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(17)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(18)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(19)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(20)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(22)
        self.writeVint(9999)
        self.writeVint(16)
        self.writeVint(23)
        self.writeVint(9999)

        self.writeVint(0)

        self.writeVint(23)
        self.writeVint(16)
        self.writeVint(0)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(1)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(2)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(3)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(4)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(5)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(6)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(7)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(8)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(9)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(10)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(11)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(12)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(13)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(14)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(15)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(16)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(17)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(18)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(19)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(20)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(22)
        self.writeVint(1440)
        self.writeVint(16)
        self.writeVint(23)
        self.writeVint(1440)

        self.writeVint(23)
        self.writeVint(16)
        self.writeVint(0)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(1)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(2)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(3)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(4)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(5)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(6)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(7)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(8)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(9)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(10)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(11)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(12)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(13)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(14)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(15)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(16)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(17)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(18)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(19)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(20)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(22)
        self.writeVint(8)
        self.writeVint(16)
        self.writeVint(23)
        self.writeVint(8)

        self.writeVint(23)
        self.writeVint(16)
        self.writeVint(0)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(1)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(3)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(4)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(5)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(6)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(7)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(8)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(9)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(10)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(11)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(12)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(13)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(14)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(15)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(16)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(17)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(18)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(19)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(20)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(22)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(23)
        self.writeVint(2)

        self.writeVint(0)
        self.writeVint(self.player.gems) #gems
        self.writeVint(0)
        self.writeVint(99)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(2)
        self.writeVint(1550832808)
        print("[INFO] Message OwnHomeData has been sent.")