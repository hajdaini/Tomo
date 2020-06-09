#!/usr/bin/python3.6
#coding:utf-8
from . database import Database
from . consumable import Consumable

"""
Nourriture du jeu
"""
class Food(Consumable):
	# id + name + expiration + heal
	def __init__(self, id : int, name : str, expiration : int, heal : int):
		assert heal > 0, "Les points doivent être positifs"

		super().__init__(id, name, expiration)
		self.heal = heal

	"""
	Enregistre un Food dans la base de données
	"""
	def create_food(self, db : Database):
		pass

	"""
	Récupère un Food depuis la base de données
	"""
	@staticmethod
	def get_food(db : Database, name : str):

	@staticmethod
	def get_food(db : Database, name : str):
		pass

if __name__ == '__main__':
	fo = Food(1, "Pain", 11, 25)