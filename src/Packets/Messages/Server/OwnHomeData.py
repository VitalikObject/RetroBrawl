from Utils.Writer import Writer


class OwnHomeData(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):

        self.writeHexa('''adbbf6018ca3099f9a0c9f9a0c00a3019f9a0c1c000900020305060708090a0090021d001d011d021d031d041d051d061d071d081d091d0a1d0b1d0c1d0d1d0e1d0f1d101d111d121d131d141d151d161d171d181d191d1a1d1b1d1c1d1d1d1e1d1f1d201d211d221d231d241d251d261d271d281d291d2a1d2b1d2c1d2d1d2e1d2f1d301d311d321d331d341d351d361d371d381d391d3a1d3b1d3c1d3d1d3e1d3f1d80011d81011d82011d83011d84011d85011d86011d87011d88011d89011d8a011d8b011d8c011d8d011d8e011d8f011d90011d91011d92011d93011d94011d95011d96011d97011d98011d99011d9a011d9b011d9c011d9d011d9e011d9f011da0011da1011da2011da3011da4011da5011da6011da7011da8011da9011daa011dab011dac011dad011dae011daf011db0011db1011db2011db3011db4011db5011db6011db7011db8011db9011dba011dbb011dbc011dbd011dbe011dbf011d80021d81021d82021d83021d84021d85021d86021d87021d88021d89021d8a021d8b021d8c021d8d021d8e021d8f020000000001010097af1e080202020000008c02b411009f9a0c6b1000ffffffff00adbbf601a4010a1e0390010a32a80fb407329c877a06001e9001aa029e0500070102030405060707dad19401010098a3090a0f070300000000000000dad19401020098a3090a0f0d0300000000000000dad19401030098a3090a0f010300000000000000dad19401040098a3090a0f180300000000000000dad19401050098a3090a0f220300000000000000dad19401060098a3090a0f3a0300000000000000dad19401070098a3090a0f350300000000000000000814238b018c02a204a007a00ca2130801020304050a0f14030a1e90010306143c0314328c020396029006b012028803148087010a05063280ea4901000000006c7da80e8bad007f0000bdb103edaef4800500000000''')
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