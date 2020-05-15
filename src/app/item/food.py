#!/usr/bin/python3.6
#coding:utf-8
from src.app.item.consumable import Consumable

"""
Nourriture du jeu
"""
class Food(Consumable):
	# id + name + expiration + heal
	def __init__(self, id : int, name : str, expiration : int, heal : int):
		assert heal > 0, "Les points doivent être positifs"

		Consumable.__init__(self, id, name, expiration)
		self.heal = heal

if __name__ == '__main__':
	fo = Food(1, "Pain", 11, 25)