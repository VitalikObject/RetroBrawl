from Utils.Writer import Writer


class PlayerProfile(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24113
        self.player = player

    def encode(self):
    	self.writeHexa('''bdb103edaef48005''')
    	self.writeString("Mr Vitalik")
    	self.writeHexa('''000108000082058c05060a019f9a0c029f9a0c039f9a0c049f9a0c059f9a0c079f9a0c089f9a0c099f9a0c0a9f9a0c0b9f9a0c01000000000000029a0000000d7777772e6c776172622e636f6d080b03018f9c010000000000025553001902''')
    	print("Message PlayerProfile has been sent.")