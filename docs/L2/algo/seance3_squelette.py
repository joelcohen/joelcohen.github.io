#!/usr/bin/env python
# encoding: utf-8

"""
TD Informatique L2 - Algorithmique
Institut Villebon-Charpak
"""
import os
from math   import *    # package pour les fonctions mathématiques (pi, cos, exp,...)
from random import *    # package pour les nombres (pseudo)-aléatoires
from time   import *    # package pour mesurer le temps d'éxecution

debut = time() # début d'execution
##################################

def tri_naif(t):
    # retourne un tableau dans lequel les éléments de t (avec répétitions) sont rangés par ordre croissant
    pass
   
def fusion(l1, l2):
    # retourne une liste qui est la fusion des deux listes triées l1 et l2
    pass
        
def tri_fusion(t):
    # trie le tableau t avec l'algorithme merge sort qui découpe la liste en deux, trie les deux moitiées récursivement, puis fusionne les deux moitiées triées
    pass

def minuter(f, arg):
    # renvoie le couple (f(arg), duree)
    # où la variable duree est le temps d'exécution du calcul de f(arg)
    pass
  

  
# quelques tests

t0 = []
t1 = range(1000)
t2 = range(1000, 2000)
t3 = range(2000)
t4 = map(lambda x : 2 * x, t1)
t5 = map(lambda x : 2 * x + 1, t1)

# test de la fonction fusion
assert fusion(t0, t1) == t1
assert fusion(t1, t2) == t3
assert fusion(t4, t5) == t3


t1 = []
t2 = [1]
t3 = [3,2,1]
t4 = [143,0,1,2,12,100,0,644,3,-7,20,14,198,17,7,91,8,18,-21,-90,37,67,-8,19,3,1,0,-1,2,3,-8,18,2,0,10,2,144,37,-9,432,0,-3,17,91,23,12,930,149,15,-17,20,0,9,5,3,2,-1,0,39,10,27,0,-1,23,1,3,1,1,1,7,100,12,11,-78,101,121,134,34,-24,34,-45,-90,39,143,198,-15,4,0,432,100,9,7,0,91,-23,231,930,9,23,-23,4,7,39,45,47,0,34,67,-144,149,1,152,431,12,23,23,23,230,432,125,1024,268,80,64,75,71,82,85, 100,0,3,5,65,-67,39,54,643,643,938,5392,644,3,204,294,358,2,34,53,43,39,29,-4,10,43,53,54,-29,39,48,28,43,2949,284,-83,384,284,4,3824,28,29,19,83,2,-1,0]
t5 = range(10000)
t5.reverse()

assert tri_fusion(t1) == []
assert tri_fusion(t2) == [1]
assert tri_fusion(t3) == [1,2,3]
assert tri_fusion(t4) == tri_naif(t4)  
assert tri_fusion(t5) == range(10000)
  
  

chemin = os.path.dirname(os.path.realpath(__file__)) # chemin du répértoire courant
with open(chemin + '/popWomen.txt', 'r') as file: # ouvrir le fichier de manière à assurer sa fermeture
    nombres = map(float, file.read().split())
    nombres = []
    
    
    # Essai du tri fusion
    nombres_fusion, duree_fusion = minuter(tri_fusion,nombres)
    print("Temps d'execution du tri fusion : " + str(duree_fusion))
    
    
    # Essai de la fonction sort de Python
    debut_sort = time()
    nombres.sort() # fonction de tri native de python
    fin_sort = time()
    duree_sort = fin_sort - debut_sort
    print("Temps d'execution de la fonction sort : " + str(duree_sort))
    

#################################
fin = time() # fin d'execution
duree = fin - debut # durée d'execution
print("Ce code s'execute en " + str(duree) + " secondes.")
