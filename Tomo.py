#!/usr/bin/python3.6
#coding:utf-8
import sys

class Tomo:
	def __init__(self, name : str, age : int):
		self.name = name # nom du Tomo
		self.age = age # age du Tomo
		self.max_health = 100
		self.health = self.max_health # vie (TODO : faim à implémenter)

	def __str__(self):
		return f"[Nom {self.name}, Age {self.age}, VieMax {self.max_health}, Vie {self.health}]"

	"""
	Nourrit un Tomo
	pts : nombre de points à ajouter à la vie
	"""
	def eat(self, pts : int):
		self.health += pts
		if self.health > self.max_health:
			self.health = self.max_health
		elif self.health <= 0:
			self.die()

	def die(self):
		print("Game Over !")
		print(f"Votre Tomo est mort à {self.age} an(s).")
		sys.exit(0)

if __name__ == '__main__':
	tomo = Tomo("Test", 1)
	print(tomo)
	tomo.eat(-5)
	print(tomo)
	tomo.eat(2)
	print(tomo)