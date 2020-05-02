from Tomo import Tomo
import time

if __name__ == '__main__':
	print("Bienvenue sur Tomo 0.1 !")
	tomo_name = input("Choisissez un nom à votre Tomo : ")

	while len(tomo_name) == 0:
		tomo_name = input("Choisissez un nom valide : ")

	tomo = Tomo(tomo_name, 1)

	while True:
		print(tomo)
		pts = int(input("Combien donnez-vous à manger ? "))
		tomo.eat(pts)