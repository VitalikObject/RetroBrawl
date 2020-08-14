from Utils.Writer import Writer


class ServerBox(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        if self.player.boxID == 5:
            self.writeHexa('''8b036b010a01300007000000017f7f0000''')
        if self.player.boxID == 4:
            self.writeHexa('''8b036b010c02820100070000030003000000017f7f0000''')
        if self.player.boxID == 3:
            self.writeHexa('''8b036b010b02a00700070000010003000000017f7f0000''')
        if self.player.boxID == 1:
            self.writeHexa('''8b036b010c02820100070000030003000000017f7f0000''')