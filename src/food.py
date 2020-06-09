#!/usr/bin/python3.6
#coding:utf-8
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

	def create_food(self, db : Database):
		pass

	@staticmethod
	def get_food(db : Database, name : str):
		pass

if __name__ == '__main__':
	fo = Food(1, "Pain", 11, 25)