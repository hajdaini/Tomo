#!/usr/bin/python3.6
#coding:utf-8
from abc import ABC, abstractmethod

"""
Objet du jeu
"""
class Item(ABC):
	@abstractmethod
	def __init__(self, id : int, name : str):
		self.id = id
		self.name = name

	"""
	TODO mais on ne sait pas quoi...
	"""
	def update(self):
		pass