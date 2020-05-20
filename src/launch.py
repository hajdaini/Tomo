#!/usr/bin/python3.6
#coding:utf-8
from src.app.database.database import Database
from src.app.database.scheduler import Scheduler
from src.app.tomo.tomo import Tomo
from src.app.item.food import Food
import sys

"""
Démarre le jeu et propose le menu principal
"""
def init():
	db = Database()
	#TODO Scheduler.initialize(db)

	foo = Food(1, "Pain", 15, 25)
	tomo = Tomo("Ralouf", 12)

	choice = input("> ")
	if choice == 'create':
		# Créer un Tomo (qui sera stockée dans la BDD)
		tomo = None
		while tomo is None:
			name = input("Choisir un nom à votre futur Tomo : ")
			try:
				tomo = Tomo(name)
			except AssertionError as e:
				print(e)
		tomo.create_tomo(db)
	elif choice == 'load':
		data = tomo.get_tomo(db)
		if data is not None:
			print(data)
	else:
		print("Confinement difficile ? Go Alt + F4")

	db.disconnect()


if __name__ == '__main__':
	pass