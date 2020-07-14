#!/usr/bin/python3.6
#coding:utf-8
from src.database import Database
from src.game import *
import pygame

"""
Démarre le jeu et propose le menu principal
"""
def init():
	screen_size = (640, 480)
	liberation_sans = 'Liberation Sans'
	open_sans = 'Open Sans'
	background_color = (25, 25, 25)
	inactive_color = (40, 100, 240)
	active_color = (60, 180, 190)

	pygame.init()
	screen = pygame.display.set_mode(screen_size)
	pygame.display.set_caption('Tomo - 0.1 build 1423 (rev 23)')
	screen.fill(background_color)

	db = Database.GetInstance('data/tomo.db')

	sql = "SELECT * FROM tomo"
	tomo_exists = db.cursor.execute(sql).fetchone()

	clock = pygame.time.Clock()
	title_font = pygame.font.SysFont(liberation_sans, 120)
	menu_font = pygame.font.SysFont(open_sans, 30)

	active_menulist = [True, False]

	pygame.display.flip()

	window_opened = True
	while window_opened:
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				window_opened = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					active_menulist.reverse()
				if event.key == pygame.K_RETURN:
					if active_menulist[0]:
						if tomo_exists is None:
							menu_create(db)
						else:
							menu_load(db)
					else:
						menu_quit(db)

		menu_title = title_font.render('TOMO', True, (200, 200, 255))
		screen.blit(menu_title, (screen_size[0] // 2 - menu_title.get_width() // 2, 80))

		if tomo_exists is None:
			menu_create_text = menu_font.render('Créer un Tomo', True, active_color if active_menulist[0] else inactive_color)
			screen.blit(menu_create_text, (screen_size[0] // 2 - menu_create_text.get_width() // 2, 280))
		else:
			menu_load_text = menu_font.render('Charger une partie', True, active_color if active_menulist[0] else inactive_color)
			screen.blit(menu_load_text, (screen_size[0] // 2 - menu_load_text.get_width() // 2, 280))

		menu_quit_text = menu_font.render('Quitter le jeu', True, active_color if active_menulist[1] else inactive_color)
		screen.blit(menu_quit_text, (screen_size[0] // 2 - menu_quit_text.get_width() // 2, 350))
		
		pygame.display.update()