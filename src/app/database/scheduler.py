#!/usr/bin/python3.6
#coding:utf-8
from src.app.database.database import Database
import csv

"""
Classe d'automatisation des données (ajout de contenu)
"""
class Scheduler:
	def __init__(self):
		pass
	
	@staticmethod
	def initialize(db : Database):
		foods = Scheduler.load_from_csv_to_database(db)
		Scheduler.update_database(db, foods)

	@staticmethod
	def load_from_csv_to_database(db : Database):
		game_foods = Scheduler.get_data_from_file("src/data/foods.csv")
		column = {
			"name": None, 
			"expiration": None, 
			"heal": None
		}

		foods = []

		# TODO Adapter pour X colonnes
		for row in game_foods:
			column["name"] = row[0]
			column["expiration"] = row[1]
			column["heal"] = row[2]
			foods.append(row)
			db.save("foods", column)
		
		return foods

	@staticmethod
	def update_database(db : Database, foods : list):
		rows = db.cursor.execute("SELECT * FROM foods")
		database_foods = rows.fetchall()
		i = 0
		
		for i in range(0, len(foods)):
			if foods[i][1] != database_foods[i][2] or foods[i][2] != database_foods[i][3]:
				sql = f"UPDATE foods SET expiration = \"{foods[i][1]}\", heal = \"{foods[i][2]}\" WHERE name = \"{foods[i][0]}\""
				db.cursor.execute(sql)

	@staticmethod
	def get_data_from_file(filename):
		with open(filename, "r") as f:
			content = csv.reader(f, delimiter = ';')
			is_first_line = True
			datalist = []

			for row in content:
				if is_first_line:
					is_first_line = False
				else:
					datalist.append(row)

		return datalist
					

if __name__ == '__main__':
	Scheduler.get_data_from_file("../../data/foods.csv")