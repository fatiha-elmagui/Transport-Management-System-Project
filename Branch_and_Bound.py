
# Programme Python3 à résoudre
# Problème de vendeur itinérant lors de l'utilisation
# Branche et lié.
import math 
import numpy as np
maxsize = float('inf') 
# Fonction pour copier la solution temporaire à la solution finale
def CopierAuFinal(acc_chem): 
	final_chem[:N + 1] = acc_chem[:] 
	final_chem[N] = acc_chem[0] 
# Fonction pour trouver le coût de bord minimum
# ayant une fin au sommet i
def PremierMin(adj, i): 
	min = maxsize 
	for k in range(N): 
		if adj[i][k] < min and i != k: 
			min = adj[i][k] 

	return min

# fonction pour trouver le deuxième bord minimum
# coût ayant une fin au sommet i
def secondMin(adj, i): 
	first, second = maxsize, maxsize 
	for j in range(N): 
		if i == j: 
			continue
		if adj[i][j] <= first: 
			second = first 
			first = adj[i][j] 

		elif(adj[i][j] <= second and
			adj[i][j] != first): 
			second = adj[i][j] 

	return second 

# fonction qui prend comme arguments:
# acc_bound -> borne inférieure du nœud racine
# acc_weight-> stocke le poids du chemin jusqu'à présent
# niveau-> niveau actuel pendant le déplacement
# dans l'arborescence de l'espace de recherche
# acc_chem [] -> où la solution est stockée
# qui serait plus tard copié dans final_chem [].
# le cas de base est lorsque nous avons atteint le niveau N
# ce qui signifie que nous avons couvert tous les nœuds une fois
# vérifier s'il y a un bord de la dernier sommet du chemin retour au premier sommet
# acc_res a le poids total de la solution que nous avons
# pour tout autre niveau itérer pour tous les sommets
# pour construire l'arborescence de l'espace de recherche de manière récursive
# Considérez le sommet suivant si ce n'est pas le même (entrée diagonale dans la matrice de contiguïté et pas déjà visité).
# calcul différent de acc_bound
# pour le niveau 2 des autres niveaux
# acc_bound + acc_weight est la limite inférieure réelle
# pour le nœud sur lequel nous sommes arrivés.
# Si la borne inférieure actuelle <final_res,
# nous devons explorer davantage le nœud
# Sinon, nous devons élaguer le nœud en réinitialisant
# toutes les modifications apportées à acc_weight et acc_bound

def BABRec(adj, acc_bound, acc_weight, 
			niveau, acc_chem, visite): 
	global final_res 
	

	if niveau == N: 
		

		if adj[acc_chem[niveau - 1]][acc_chem[0]] != 0: 
			

			acc_res = acc_weight + adj[acc_chem[niveau - 1]][acc_chem[0]] 
			if acc_res < final_res: 
				CopierAuFinal(acc_chem) 
				final_res = acc_res 
		return


	for i in range(N): 
		

		if (adj[acc_chem[niveau-1]][i] != 0 and
							visite[i] == False): 
			temp = acc_bound 
			acc_weight += adj[acc_chem[niveau - 1]][i] 


			if niveau == 1: 
				acc_bound -= ((PremierMin(adj, acc_chem[niveau - 1]) +
								PremierMin(adj, i)) / 2) 
			else: 
				acc_bound -= ((secondMin(adj, acc_chem[niveau - 1]) +
								PremierMin(adj, i)) / 2) 

			if acc_bound + acc_weight < final_res: 
				acc_chem[niveau] = i 
				visite[i] = True
				

				BABRec(adj, acc_bound, acc_weight, 
					niveau + 1, acc_chem, visite) 


			acc_weight -= adj[acc_chem[niveau - 1]][i] 
			acc_bound = temp 

			visite = [False] * len(visite) 
			for j in range(niveau): 
				if acc_chem[j] != -1: 
					visite[acc_chem[j]] = True

def BAB(adj): 

	acc_bound = 0
	acc_chem = [-1] * (N + 1) 
	visite = [False] * N 

	for i in range(N): 
		acc_bound += (PremierMin(adj, i) + secondMin(adj, i)) 

	acc_bound = math.ceil(acc_bound / 2) 


	visite[0] = True
	acc_chem[0] = 0

	BABRec(adj, acc_bound, 0, 1, acc_chem, visite) 



adj =[[0,252,243,323,574,530,11,851,498,432],
      [252,0,467,547,798,754,6,1074,663,201],
      [243,467,0,87,338,294,1609,615,535,648],
      [324,547,87,0,251,207,12,528,471,728],
      [574,798,338,251,0,399,304,719,662,979],
      [530,454,294,207,399,0,66,331,350,936],
      [11,6,1609,12,304,66,0,2223,1839,969],
      [851,1074,615,528,719,331,2223,0,553,1257],
      [498,663,535,471,662,350,1839,553,0,830],
      [432,201,648,728,979,936,969,1257,830,0]]
      
      
N = 10

final_chem = [None] * (N + 1) 
visite = [False] * N 
final_res = maxsize 

BAB(adj) 
import pandas as pd 

def villes(filepath):
	L=[]
	csv=pd.read_excel(filepath)
	for i in range (len(csv['villes'])):
         L.append(tuple((i+1,csv['villes'][i])))
	return L
	

def run():
	return final_res

def chemin():
	L=[]
	for i in range(N + 1): 
	    L.append(final_chem[i]+1)
	return L
