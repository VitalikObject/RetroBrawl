from database.DataBase import DataBase
from Utils.Writer import Writer


class ClubProfileMessage(Writer):

    def __init__(self, client, player, clubLowID):
        super().__init__(client)
        self.id = 24301
        self.player = player
        self.clubLowID = clubLowID

    def encode(self):
        DataBase.loadClub(self, self.clubLowID)

        self.writeVint(1)

        self.writeInt(0)
        self.writeInt(self.clubLowID)
        self.writeString(self.clubName)
        #self.writeString("<cff2400>V<cff4800>i<cff6d00>t<cfe9100>a<cffb600>l<cffda00>i<cfffe00>k<cffff00>O<cdaff00>b<cb6ff00>j<c91ff00>e<c6dfe00>c<c48ff00>t</c> <c4>and</c> <cff002a>P<cff0054>h<cff007f>o<cff00a9>e<cff00d4>n<cfe00fe>i<cff00ff>x<cd400ff>F<caa00ff>i<c7f00ff>r<c5500ff>e</c>")

        self.writeVint(8) # csvID
        self.writeVint(self.clubbadgeID)# BadgeID

        self.writeVint(self.clubtype) # Club type
        self.writeVint(self.clubmembercount) # Member count

        self.writeVint(self.clubtrophies) # Club trophies
        self.writeVint(self.clubtrophiesneeded) # Club trophies required

        self.writeVint(0)
        self.writeString("IL")
        self.writeVint(0)
        self.writeString(self.clubdescription)

        self.writeVint(self.clubmembercount)  # Members list count

        for member in DataBase.GetMemberData(self, self.clubLowID):

            self.writeInt(0)  # High Id
            self.writeInt(member['lowID'])  # Low Id
            self.writeString(member['name'])
            self.writeVint(member['clubRole'])  # player club role | 0 = Nothing, 1 = Member, 2 = President, 3 = Senior, 4 = Vice President
            self.writeVint(0)
            self.writeVint(member['trophies'])  # trophies
            self.writeVint(2) # Player state
            self.writeVint(0)
            self.writeVint(28)
            self.writeVint(member['profileIcon'])

        if False:
            self.writeInt(1)
            self.writeInt(1)
            self.writeString("<cff3200>M<cff6500>r<cff9800> <cffcb00>V<cffff00>i<cccff00>t<c99ff00>a<c66ff00>l<c33ff00>i<c01ff00>k</c>")
            self.writeVint(2)
            self.writeVint(0)
            self.writeVint(9999)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(28)
            self.writeVint(33)

            self.writeInt(1)
            self.writeInt(2)
            self.writeString(
                "<cff002a>P<cff0054>h<cff007f>o<cff00a9>e<cff00d4>n<cfe00fe>i<cff00ff>x<cd400ff>F<caa00ff>i<c7f00ff>r<c5500ff>e</c>")
            self.writeVint(2)
            self.writeVint(0)
            self.writeVint(9999)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(28)
            self.writeVint(33)

            self.writeInt(1)
            self.writeInt(3)
            self.writeString("<c0054ff>C<c00a9ff>r<c00feff>a<c00ffaa>z<c00ff55>o<c00ff02>r</c>")
            self.writeVint(2)
            self.writeVint(0)
            self.writeVint(9999)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(28)
            self.writeVint(33)
        print("[INFO] Message ClubProfileMessage has been sent.")