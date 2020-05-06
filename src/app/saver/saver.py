#!/usr/bin/python3.6
#coding:utf-8
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
		self.cursor.execute("CREATE TABLE IF NOT EXISTS tomo(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(20) NOT NULL UNIQUE, age INTEGER NOT NULL, items TEXT)")

	def store_data(self):
		# TODO Faire un tomo Delex dans la BDD
		self.cursor.execute(f"INSERT INTO tomo(name, age, items) VALUES('Delex', '24', '[Salade, Tomates, Oignons]')")
		self.cursor.execute(f"INSERT INTO tomo(name, age, items) VALUES('Ralouf', '0', '[Cuillère]')")
	
	def disconnect(self):
		self.cursor.close()
		self.connection.close()

if __name__ == '__main__':
	s = Saver()
	s.connect()
	s.create_table()
	s.store_data()
	s.disconnect()