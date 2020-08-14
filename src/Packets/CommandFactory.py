from Utils.reader import CoCMessageReader

class Commands(CoCMessageReader):
	def __init__(self, client, player, initial_bytes):
		super().__init__(initial_bytes)
		self.client = client
		self.player= player
		
	def decode(self):
		self.read_Vint()
		self.read_Vint()
		#print(Reader.read(50))
		self.read_Vint()
		self.read_Vint()
		commandID = self.read_Vint()

	def process(self):
		pass