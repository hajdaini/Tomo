#!/usr/bin/python3.6
#coding:utf-8

from src.tomo import Tomo

def menu_create(db):
	name = input("Choisir un nom pour votre Tomo : ")
	print("Tomo créé !")
	tomo = Tomo(name)
	tomo.create_tomo(db)
	return tomo

def menu_load(db):
	name = input("Quel est le nom du Tomo ? ")
	print(f"Chargement de {name} en cours...")
	return Tomo.get_tomo(db, name)

def menu_quit(db):
	db.disconnect()
	print("A bientôt")
	print("Contacter le support Ralof par Minitel au 3615 code ASCII")
	exit(0)