#!/usr/bin/python3.6
#coding:utf-8
from src.database import Database

#TODO à isoler dans un autre module (Scene ? Game ? Universe ?)
def menu_create():
	print("CREATE")

def menu_load():
	print("LOAD")

def menu_quit():
	print("Au revoir !")
	exit(0)

"""
Démarre le jeu et propose le menu principal
"""
def init():
	db = Database.GetInstance('data/tomo.db')
	menu_launched = True

	commands = {
		'create': menu_create, 
		'load'  : menu_load, 
		'quit'  : menu_quit
	}

	while menu_launched:
		choice = input("> ")

		try:
			commands[choice]()
		except KeyError:
			print("Commande non reconnue")

	db.disconnect()