class Players:
	
	HighID = 0
	LowID = 0
	Token = None
	boxID = 0
	mapID = 7
	roomID = 0
	brawlerID = 0
	skinID = 0
	gems = 99999
	gold = 99999
	tickets = 99999
	name = None
	profileIcon = 0
	brawlBoxes = 99999
	bigBoxes = 99999

	def __init__(self, device):
		self.device = device