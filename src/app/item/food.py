#!/usr/bin/python3.6
#coding:utf-8
from src.app.item.consumable import Consumable

"""
Nourriture du jeu
"""
class Food(Consumable):
	def __init__(self, id : int, name : str, expiration : int, heal : int):
		assert heal > 0, "Les points doivent être positifs"

		super().__init__(self, id, name, expiration)
		self.heal = heal