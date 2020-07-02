#!/usr/bin/python3.6
#coding:utf-8
from abc import ABC, abstractmethod

"""
Objet du jeu
"""
class Item(ABC):
	@abstractmethod
	def __init__(self, identifier : int, name : str):
		# assert id > 0, "L'ID de l'Item doit être supérieur à 0"
		# assert name.isalpha(), "C'pas la bonneuh syntaxeuuh"
		# assert len(name) > 3 and len(name) <= 20, "Le nom de l'Item doit être compris entre 3 et 20 caractères."

		self.id = identifier
		self.name = name

	"""
	TODO pour plus tard
	"""
	def update(self):
		pass

if __name__ == '__main__':
	pass