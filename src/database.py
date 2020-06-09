#!/usr/bin/python3.6
#coding:utf-8
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

		self.connect()
		self.create()

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

	"""
	Création des tables dans la base de données
	"""
	def create(self):
		self.cursor.execute("CREATE TABLE IF NOT EXISTS tomo(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(20) NOT NULL UNIQUE, age INTEGER NOT NULL, health INTEGER NOT NULL, items TEXT)")
		self.cursor.execute("CREATE TABLE IF NOT EXISTS foods(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(20) NOT NULL UNIQUE, expiration INTEGER NOT NULL, heal INTEGER NOT NULL)")

	"""
	Récupérer des données depuis la base
	"""
	def select(self, table_name : str, selector : dict):
		names = ""
		values = ""

		for name, value in selector.items():
			names = str(name)
			values = "'" + str(value) + "'"
			
		sql = f"SELECT * FROM {table_name} WHERE {names} = {values}"
		return self.cursor.execute(sql).fetchone()

	def save(self, table_name : str, columns : dict):
		names = ""
		values = ""

		for name, value in columns.items():
			names += "'" + str(name) + "', "
			if isinstance(value, list):
				values += "'" + " ".join(value) + "', "
			else:
				values += "'" + str(value) + "', "

			values = values.strip()

		names = names[:-2]
		values = values[:-2]
		sql = f"INSERT INTO {table_name}({names}) VALUES({values})"

		try:
			self.cursor.execute(sql)
		except:
			pass
			# 1. Aliment déjà présent, mais à mettre à jour
			# 2. Aliment déjà présent, ET identique (pas à mettre à jour)

	"""
	Clôture la connexion à la base de données SQLite
	"""
	def disconnect(self):
		self.cursor.close()
		self.connection.close()

if __name__ == '__main__':
	pass