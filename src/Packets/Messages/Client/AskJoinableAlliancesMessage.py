from Packets.Messages.Server.JoinableAllianceListMessage import JoinableAllianceListMessage

from Utils.Reader import BSMessageReader

class AskJoinableAlliancesMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        pass
        #JoinableAllianceListMessage(self.client, self.player).send()