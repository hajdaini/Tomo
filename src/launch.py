#!/usr/bin/python3.6
#coding:utf-8
from src.app.saver.saver import Saver
from src.app.tomo.tomo import Tomo

"""
Démarre le jeu et propose le menu principal
"""
def init():
	saver = Saver()
	saver.connect()
	saver.create_table()
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
		saver.store_data(tomo)
	elif choice == 'load':
		data = saver.load_tomo()
		tomo = Tomo(data[1], data[2], data[3], data[4])
		print(tomo)
	else:
		print("Confinement difficile ? Go Alt + F4")

	saver.disconnect()


if __name__ == '__main__':
	pass