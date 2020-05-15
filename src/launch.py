#!/usr/bin/python3.6
#coding:utf-8
from src.app.database.database import Database
from src.app.tomo.tomo import Tomo
from src.app.item.food import Food

"""
Démarre le jeu et propose le menu principal
"""
def init():
	db = Database()
	db.connect()

	foo = Food(1, "Pain", 15, 25)
	tomo = Tomo("Ralouf", 12)
	db.create(tomo, foo)

	db.create_table()
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
		tomo.create_tomo(tomo, db)
	elif choice == 'load':
		data = tomo.get_tomo()
		tomo = Tomo(data[1], data[2], data[3], data[4])
		print(tomo)
	else:
		print("Confinement difficile ? Go Alt + F4")

	db.disconnect()


if __name__ == '__main__':
	pass