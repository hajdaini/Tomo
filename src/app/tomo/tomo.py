#!/usr/bin/python3.6
#coding:utf-8
from src.app.database.database import Database
from src.app.item.item import Item
from src.app.item.food import Food
import sys

"""
Classe Tomo
- Personnage principal du jeu
"""
class Tomo:
	def __init__(self, name : str, age : int = 0, health : int = 100, inventory : list = []):
		assert name.isalpha(), "ça, le film"
		assert len(name) > 3 and len(name) <= 20, "Le nom du Tomo doit être compris entre 3 et 20 caractères."

		self.name = name # nom du Tomo
		self.age = age
		self.max_health = 100
		self.health = health
		self.inventory = inventory

	def __str__(self):
		return f"[Nom {self.name}, Age {self.age}, VieMax {self.max_health}, Vie {self.health}, Inventaire {self.inventory}]"

	"""
	Nourrit un Tomo
	@param pts Nombre de points à ajouter aux points de vie
	"""
	def feed(self, pts : int):
		assert pts >= 0, "Le nombre de points ne doit pas être inférieur à 0"

		self.health += pts
		if self.health > self.max_health:
			self.health = self.max_health
		elif self.health <= 0:
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
		assert isinstance(item, Item), "Le paramètre doit être une instance d'Item"

		self.feed(item.heal)
		self.inventory.remove(item)
		item.delete()

	"""
	Enregistre un Tomo en base de données
	"""
	def create_tomo(self, db : Database):
		sql = "INSERT INTO tomo(name, age, health, items) VALUES(?, ?, ?, ?)"
		data = (self.name, self.age, self.health, str(self.inventory))
		db.cursor.execute(sql, data)

	"""
	Récupère un Tomo depuis la base de données
	"""
	def get_tomo(self, db : Database):
		sql = "SELECT * FROM tomo"
		data = db.cursor.execute(sql).fetchone()
		parsed = [elt for elt in data]
		parsed[4] = literal_eval(parsed[4])
		return parsed

if __name__ == '__main__':
	pass