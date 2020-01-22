from packages.p_biomes_creation import *
from packages.p_decisional import *
from packages.p_board_functions import *
from packages.p_image_creation import *
import random

# CORPS DU PROGRAMME
# Appelle les fonctions maitresses.

seed = {}
seed['Tx'] = random.randint(-100000,100000)
seed['Ty'] = random.randint(-100000,100000)
seed['Px'] = random.randint(-100000,100000)
seed['Py'] = random.randint(-100000,100000)


Biomes = Creation_Constantes_Biomes()

nbx=eval(input("x = "))
nby=eval(input("y = "))
Plateau = Creer_Plateau_Vide(nbx,nby)

for i in range (len(Plateau)) :
	for j in range (len(Plateau[0])) :
		Plateau[i][j] = Placer_Case(Biomes, i, j, seed)
	print("Vectorial creation of the map : ",round((i + 1)/len(Plateau)*100,2),"%", end = '\r')
print("")

#Afficher_Plateau(Plateau)

image_creation(Plateau)
