#!/usr/bin/python3.6
#coding:utf-8
from Consumable import Consumable

"""
Nourriture du jeu
"""
class Food(Consumable):
	def __init__(self, id : int, name : str, expiration : int, heal : int):
		Consumable.__init__(self, id, name, expiration)
		self.heal = heal