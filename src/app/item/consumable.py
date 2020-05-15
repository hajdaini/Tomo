#!/usr/bin/python3.6
#coding:utf-8
from src.app.item.item import Item

"""
Objet consommable du jeu
"""
class Consumable(Item):
	def __init__(self, id : int, name : str, expiration : int):
		assert expiration > 0, "La valeur d'expiration doit être positive"

		super().__init__(self, id, name)
		self.expiration = expiration

	def __str__(self):
		return f"[id {self.id}, name {self.name}, expiration {self.expiration}]"

	"""
	Réduit la durée d'expiration du consommable
	"""
	def update(self):
		if self.expiration > 0:
			self.expiration -= 1
		else:
			self.delete()

	"""
	Supprime un consommable
	"""
	def delete(self):
		print(f"{self.name} ({self.id}) a expiré")
		self.__del__()

	def __del__(self):
		pass