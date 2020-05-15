#!/usr/bin/python3.6
#coding:utf-8
from ast import literal_eval
import sqlite3
import sys

"""
Classe Database
- Sauvegarde les données du jeu
"""
class Database:
	__instance = None

	def __init__(self, filename : str = 'tomo.db'):
		self.filename = filename
		self.connection = None
		self.cursor = None

		if Database.__instance is None:
			Database.__instance = self
		else:
			raise Exception("Classe déjà instanciée")

	@staticmethod
	def GetInstance():
		if not Database.__instance:
			Database()
		return Database.__instance

	"""
	Connexion à la base de données SQLite
	"""
	def connect(self):
		try:
			self.connection = sqlite3.connect(self.filename, isolation_level = None)
			self.cursor = self.connection.cursor()
		except:
			print("Problème de connexion à la BASE !")

		self.create()

	"""
	Création des tables dans la base de données
	"""
	def create(self):
		self.cursor.execute("CREATE TABLE IF NOT EXISTS tomo(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(20) NOT NULL UNIQUE, age INTEGER NOT NULL, health INTEGER NOT NULL, items TEXT)")

	def save(self, dbname : str, columns : dict):
		names = ""
		values = ""

		for name, value in columns.items():
			names += "'" + str(name) + "', "

			if isinstance(value, list):
				values += "'" + " ".join(value) + "', "
			else:
				values += "'" + str(value) + "', "

		names = names[:-2]
		values = values[:-2]

		sql = f"INSERT INTO {dbname}({names}) VALUES({values})"
		print(sql)
		self.cursor.execute(sql)

	"""
	Clôture la connexion à la base de données SQLite
	"""
	def disconnect(self):
		self.cursor.close()
		self.connection.close()

if __name__ == '__main__':
	db = Database()
	db.connect()

	data = {
		"name": "Ralof", 
		"age": 12, 
		"health": 100, 
		"items": ["Cuvette", "Pain"]
	}

	db.save("tomo", data)
	db.disconnect()