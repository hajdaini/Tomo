#!/usr/bin/python3.6
#coding:utf-8
from src.app.tomo.tomo import Tomo
from ast import literal_eval
import sqlite3

"""
Classe Saver
- Sauvegarde les données du jeu
"""
class Saver:
	__instance = None

	def __init__(self, filename : str = 'tomo.db'):
		self.filename = filename
		self.connection = None
		self.cursor = None

		if Saver.__instance is None:
			Saver.__instance = self
		else:
			raise Exception("Classe déjà instanciée")

	@staticmethod
	def GetInstance():
		if not Saver.__instance:
			Saver()
		return Saver.__instance
		

	def __str__(self):
		pass 

	"""
	Connexion à la base de données SQLite
	"""
	def connect(self):
		try:
			self.connection = sqlite3.connect(self.filename, isolation_level = None)
			self.cursor = self.connection.cursor()
		except:
			print("Problème de connexion à la BASE !")

	"""
	Création de la table des tomos
	"""
	def create_table(self):
		self.cursor.execute("CREATE TABLE IF NOT EXISTS tomo(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(20) NOT NULL UNIQUE, age INTEGER NOT NULL, health INTEGER NOT NULL, items TEXT)")

	def store_data(self, tomo : Tomo):
		sql = "INSERT INTO tomo(name, age, health, items) VALUES(?, ?, ?, ?)"
		data = (tomo.name, tomo.age, tomo.health, str(tomo.inventory))

		self.cursor.execute(sql, data)

	def load_tomo(self):
		sql = "SELECT * FROM tomo"
		data = self.cursor.execute(sql).fetchone()
		parsed = [elt for elt in data]
		parsed[4] = literal_eval(parsed[4])
		return parsed
	
	def disconnect(self):
		self.cursor.close()
		self.connection.close()

if __name__ == '__main__':
	s = Saver()
	s.connect()
	s.create_table()
	s.store_data()
	s.disconnect()