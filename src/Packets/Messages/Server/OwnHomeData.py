from Utils.Writer import Writer


class OwnHomeData(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        self.writeVint(2019053)
        self.writeVint(75980)
        self.writeVint(99999)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(99)
        self.writeVint(99999)
        self.writeVint(28)
        self.writeVint(0)
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
        self.writeVint(0)
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
        self.writeVint(0)
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
        self.writeVint(99999)
        self.writeHexa('''6b1000ffffffff00adbbf601a4010a1e0390010a32a80fb407329c877a06001e9001aa029e0500070102030405060707dad19401010098a3090a0f070300000000000000dad19401020098a3090a0f0d0300000000000000dad19401030098a3090a0f010300000000000000dad19401040098a3090a0f180300000000000000dad19401050098a3090a0f220300000000000000dad19401060098a3090a0f3a0300000000000000dad19401070098a3090a0f350300000000000000000814238b018c02a204a007a00ca2130801020304050a0f14030a1e90010306143c0314328c020396029006b012028803148087010a05063280ea4901000000006c7da80e8bad007f0000bdb103edaef4800500000000''')
        self.writeString("Mr Vitalik")
        self.writeVint(1)
        self.writeString()
        self.writeVint(8)
        self.writeVint(4)
        self.writeVint(23)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(5)
        self.writeVint(1)
        self.writeVint(99999)
        self.writeVint(5)
        self.writeVint(8)
        self.writeVint(99999)
        self.writeVint(5)
        self.writeVint(9)
        self.writeVint(99999)
        self.writeVint(1)
        self.writeVint(16)
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(1)
        self.writeVint(16)
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(16)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(16)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(99999)
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