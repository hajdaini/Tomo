#!/usr/bin/python3.6
#coding:utf-8
import sys
sys.path.append("..")

from src.food import Food
import unittest
import random

"""
Tests unitaires de Food (et d'Item, implicitement)
"""
class TestFood(unittest.TestCase):
	def setUp(self):
		self.foods_list = [
			Food(1, "Raclette", -2, 10),
			Food(2, "Petit sushi des poubelles", 10, -5)
			#Food(-6, "Bâton", 12, 24), 
			#Food(2, "Potion", 53, 10), 
			#Food(3, "01644", 10, 10), 
			#Food(4, "Tomooooooooooooooooooooooooooooooooooooo", 5, 1)
		]

	def test_id_attribute(self):
		for food in self.foods_list:
			try:
				self.assertGreater(food.id, 0)
			except AssertionError:
				print(f"\n[ERREUR] {food.id} : L'ID de l'objet doit être positif")

	def test_name_attribute(self):
		for food in self.foods_list:
			try:
				self.assertTrue(food.name.isalpha())
			except AssertionError:
				print(f"\n[ERREUR] {food.name} : Le nom de l'aliment ne doit être composé que de lettres")

			try:
				self.assertTrue(len(food.name) > 3 and len(food.name) <= 20)
			except AssertionError:
				print(f"\n[ERREUR] {food.name} : Le nom de l'aliment doit contenir entre 4 et 20 caractères")

	def test_expiration_attribute(self):
		for food in self.foods_list:
			try:
				self.assertGreater(food.expiration, 0)
			except AssertionError:
				print(f"\n[ERREUR] {food.expiration} : L'expiration du consommable doit être une valeur positive")

	def test_heal_attribute(self):
		for food in self.foods_list:
			try:
				self.assertGreater(food.heal, 0)
			except AssertionError:
				print(f"\n[ERREUR] {food.heal} : La quantité de soins de l'aliment doit être une valeur positive")



if __name__ == '__main__':
	unittest.main()