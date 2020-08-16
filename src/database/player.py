import sqlite3
import json

class DataBase():
	def __init__(self):
		self.conn = sqlite3.connect("players.db")
		self.cursor = self.conn.cursor()
		try:
			self.cursor.execute("""CREATE TABLE main (LowID integer, Token text, Data json, Trophies integer)""")
		except:
			pass
	
	def get_top_players_db(self):
		try:
			self.cursor.execute("SELECT Trophies, Data FROM main ORDER BY Trophies DESC")
			return self.cursor.fetchall()
		except:
			pass
			
	def create_player_db(self, lowID, token, data):
		try:
			self.cursor.execute("INSERT INTO main (LowID, Token, Data, Trophies) VALUES (?, ?, ?, ?)", (lowID, token, json.dumps(data, ensure_ascii=0), 5000))
			self.conn.commit()
		except:
			pass
			
	def get_player_db(self, token):
		try:
			self.cursor.execute("SELECT * from main where Token=?", (token, ))
			return self.cursor.fetchall()
		except:
			pass
	def get_player_lowID_db(self, low):
		try:
			self.cursor.execute("SELECT * from main where LowID=?", (low, ))
			return self.cursor.fetchall()
		except:
			pass
			
	def update_value_db(self, var, value, token):
		try:
			self.cursor.execute("UPDATE main SET %s=%s WHERE Token=%s" % (var, value, token))
			self.conn.commit()
		except:
			pass
	
	def update_data_db(self, data, token):
		try:
			self.cursor.execute("UPDATE main SET Data=? WHERE Token=?", (json.dumps(data, ensure_ascii=0), token))
			self.conn.commit()
		except:
			pass
			
	def low_id_desc_db(self):
		try:
			self.cursor.execute('SELECT LowID FROM main ORDER BY LowID DESC')
			return self.cursor.fetchall()[0][0] + 1
		except:
			return 1
			
		