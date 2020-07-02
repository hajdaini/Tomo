#!/usr/bin/python3.6
#coding:utf-8
from database import Database
import csv
import sys

"""
Classe d'automatisation des données (ajout de contenu)
"""
class Scheduler:
	def __init__(self):
		pass
	
	@staticmethod
	def initialize(db : Database):
		foods = Scheduler.load_from_csv(db)
		Scheduler.synchronize_with_database(db, foods)

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

	@staticmethod
	def load_from_csv(db : Database):
		game_foods = Scheduler.get_data_from_file("../data/foods.csv")
		column = {
			"name": None, 
			"expiration": None, 
			"heal": None
		}

		foods = []

		for row in game_foods:
			row = row[0].split(",")
			column["name"] = row[0]
			column["expiration"] = row[1]
			column["heal"] = row[2]
			foods.append(row)
		
		return foods

	@staticmethod
	def synchronize_with_database(db : Database, foods : list):
		rows = db.cursor.execute("SELECT * FROM foods")
		database_foods = rows.fetchall()
		
		i = 0
		for i in range(0, len(foods)):
			sql = f"SELECT * FROM foods WHERE name = \"{foods[i][0]}\""
			row = db.cursor.execute(sql)
			food = row.fetchone()
			
			if food is None:
				sql = f"INSERT INTO foods(name, expiration, heal) VALUES(\"{foods[i][0]}\", \"{foods[i][1]}\", \"{foods[i][2]}\")"
			else:
				sql = f"UPDATE foods SET expiration = \"{foods[i][1]}\", heal = \"{foods[i][2]}\" WHERE name = \"{foods[i][0]}\""
			
			db.cursor.execute(sql)

if __name__ == '__main__':
	Scheduler.initialize(Database.GetInstance('../data/tomo.db'))