#!/usr/bin/python3.6
#coding:utf-8
from . database import Database
from . consumable import Consumable

"""
Nourriture du jeu
"""
class Food(Consumable):
	def __init__(self, identifier : int, name : str, expiration : int, heal : int):
		# assert heal > 0, "Les points doivent être positifs"
		super().__init__(identifier, name, expiration)
		self.heal = heal

	"""
	Enregistre un Food dans la base de données
	"""
	def create_food(self, db : Database):
		sql = "INSERT INTO foods(name, expiration, heal) VALUES(?, ?, ?)"
		data = (self.name, self.expiration, self.heal)
		db.cursor.execute(sql, data)

	"""
	Récupère un Food depuis la base de données
	"""
	@staticmethod
	def get_food(db : Database, name : str):
		request = db.select("foods", {'name' : name})
		if request is None:
			print("Cet aliment n'existe pas :(")
			return None

		return Food(request[1], request[2], request[3])

if __name__ == '__main__':
	pass