#!/usr/bin/python3.6
#coding:utf-8
from . database import Database
from . item import Item
from . food import Food
import sys
import ast

"""
Classe Tomo
- Personnage principal du jeu
"""
class Tomo:
	def __init__(self, name : str, age : int = 0, health : int = 100, inventory : list = []):
		#assert name.isalpha(), "Bah oué pas de JUL_lul"
		#assert len(name) > 3 and len(name) <= 20, "Le nom du Tomo doit être compris entre 3 et 20 caractères."

		self.name = name # nom du Tomo
		self.age = age
		self.max_health = 100
		self.health = health
		self.inventory = inventory
		self.table_name = "tomo"

	def __str__(self):
		return f"[Nom {self.name}, Age {self.age}, VieMax {self.max_health}, Vie {self.health}, Inventaire {self.inventory}]"

	"""
	Nourrit un Tomo
	@param pts Nombre de points à ajouter aux points de vie
	"""
	def feed(self, pts : int):
		#assert pts >= 0, "Le nombre de points ne doit pas être inférieur à 0"
		self.health = min(self.health + pts, self.max_health)

		if self.health <= 0:
			self.die()

	"""
	Tue le Tomo et met fin au jeu
	"""
	def die(self):
		print("Game Over !")
		print(f"Votre Tomo est mort à {self.age} an(s).")
		sys.exit(0)

	"""
	Utilise un objet (de l'inventaire)
	@param item L'objet de l'inventaire
	"""
	def use(self, item : Item):
		#assert isinstance(item, Item), "Le paramètre doit être une instance d'Item"

		#TODO Se décider sur la consommation ou non si vie au max (popup avertissement ?)
		try:
			self.inventory.remove(item)
			self.feed(item.heal)
			item.delete()
		except Exception as e:
			print(e)

	"""
	Enregistre un Tomo en base de données
	"""
	def create_tomo(self, db : Database):
		db.save(self.table_name, {'name' : self.name, 
		                         'age' : self.age, 
								 'health' : self.health, 
								 'items' : self.inventory})

	"""
	Récupère un Tomo depuis la base de données
	"""
	@staticmethod
	def get_tomo(db : Database, name : str):
		try:
			request = db.select("tomo", {'name' : name})
			if request is None:
				print("Ce Tomo n'existe pas :(")
			return Tomo(request[1], request[2], request[3], request[4])
		except Exception as e:
			print(e)

if __name__ == '__main__':
	pass