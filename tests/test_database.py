#!/usr/bin/python3.6
#coding:utf-8
import sys
sys.path.append("..")

from src.database import Database
from src.tomo import Tomo
import unittest
import random

"""
Tests unitaires de Database
"""
class TestDatabase(unittest.TestCase):
	def setUp(self):
		self.tomo = Tomo("Smith", 25, 100, [])
		self.food = Food(1, "Raclette", 50, 38)

	def test_insert_tomo(self):
		#TODO Préciser le type d'exception
		try:
			self.tomo.create_tomo(Database.GetInstance())
		except:
			print("Création du Tomo échouée")

	def test_get_tomo(self):
		self.tomo = None
		try:
			self.tomo = Tomo.get_tomo(Database.GetInstance(), "Smith")
			print(self.tomo)
		except:
			print("Récupération du Tomo impossible")

	def test_insert_food(self):
		pass

	def test_get_food(self):
		pass

	def tearDown(self):
		#self.db.disconnect()
		pass

if __name__ == '__main__':
	unittest.main()