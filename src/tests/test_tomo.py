#!/usr/bin/python3.6
#coding:utf-8
import sys
sys.path.append("../")

from app.tomo.tomo import Tomo
import unittest
import random

"""
Tests unitaires du Tomo
"""
class TestTomo(unittest.TestCase):
	names = ["Ralof", "Ralax", "Ralitte", "Rasta", "Ra", "Rastapopoulossopossot"]

	def setUp(self):
		self.tomo_list = [
			Tomo("Ralof", 2, 100, ["Bâton de sorcier"]), 
			Tomo("Delex", 23, []), 
			Tomo("Ra", 9, [])
		]

	def test_name_attribute(self):
		for tomo in self.tomo_list:
			try:
				self.assertTrue(tomo.name.isalpha())
			except AssertionError:
				print(f"[ERREUR] {tomo.name} : Le nom du Tomo ne doit être composé que de lettres")

			try:
				self.assertTrue(len(tomo.name) > 3 and len(tomo.name) <= 20)
			except AssertionError:
				print(f"[ERREUR] {tomo.name} : Le nom du Tomo doit contenir entre 3 et 20 caractères")

	def test_feed_method(self):
		for tomo in self.tomo_list:
			try:
				self.assertGreater(tomo.health > tomo.max_health)
			except:
				print(f"[ERREUR] Vie maximum déjà atteinte ({tomo.health}) pour {tomo.name} !")

			pts = random.randint(-100, 100)
			try:
				print(f"{tomo.health} : Gain de +{pts} au Tomo (vie actuelle : {tomo.health}")
				self.assertGreaterEqual(pts >= 0)
			except:
				print(f"[ERREUR] {tomo.health} : Le nombre de points de soin doit être supérieur ou égal à 0")

	def test_use_method(self):
		pass

if __name__ == '__main__':
	unittest.main()