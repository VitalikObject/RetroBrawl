import sqlite3
import json

class DataBaseClub():
	def __init__(self):
		self.conn = sqlite3.connect("clubs.db")
		self.cursor = self.conn.cursor()
		try:
			self.cursor.execute("""CREATE TABLE main (LowID integer, Data json, Trophies integer)""")
		except:
			pass
	
	def get_top_players_db(self):
		try:
			self.cursor.execute("SELECT Trophies, Data FROM main ORDER BY Trophies DESC")
			return self.cursor.fetchall()
		except:
			pass
	
	def get_search_club_db(self):
		try:
			self.cursor.execute("SELECT Trophies, Data FROM main ORDER BY Trophies DESC")
			return self.cursor.fetchall()
		except:
			pass
			
	def create_club_db(self, lowID, data):
		try:
			self.cursor.execute("INSERT INTO main (LowID, Data, Trophies) VALUES (?, ?, ?)", (lowID, json.dumps(data, ensure_ascii=0), 5000))
			self.conn.commit()
		except:
			pass
			
	def get_club_db(self, low):
		try:
			self.cursor.execute("SELECT * from main where LowID=?", (low, ))
			return self.cursor.fetchall()
		except:
			pass
			
	def update_value_db(self, var, value, lowID):
		try:
			self.cursor.execute("UPDATE main SET %s=%s WHERE LowID=%s" % (var, value, lowID))
			self.conn.commit()
		except:
			pass
	
	def update_data_db(self, data, lowID):
		try:
			self.cursor.execute("UPDATE main SET Data=? WHERE LowID=?", (json.dumps(data, ensure_ascii=0), lowID))
			self.conn.commit()
		except:
			pass
			
	def low_id_desc_db(self):
		try:
			self.cursor.execute('SELECT LowID FROM main ORDER BY LowID DESC')
			return self.cursor.fetchall()[0][0] + 1
		except:
			return 1
			
		