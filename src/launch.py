#!/usr/bin/python3.6
#coding:utf-8
from . database import Database
from . scheduler import Scheduler
from . tomo import Tomo
from . food import Food

"""
Démarre le jeu et propose le menu principal
"""
def init():
	db = Database()
	#TODO Scheduler.initialize(db)
	
	choice = input("> ")
	if choice == 'create':
		# Créer un Tomo (qui sera stockée dans la BDD)
		
		while tomo is None:
			name = input("Choisir un nom à votre futur Tomo : ")
			try:
				tomo = Tomo(name)
			except AssertionError as e:
				print(e)
		tomo.create_tomo(db)
	elif choice == 'load':
		tomo_name = input("Quel nom porte votre Tomo ? ")
		tomo = Tomo.get_tomo(db, tomo_name)
		print(tomo)
	else:
		print("Déconfinement difficile ? Go Alt + F4")

	db.disconnect()


if __name__ == '__main__':
	pass