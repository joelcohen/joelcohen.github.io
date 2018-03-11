#!/usr/bin/env python
# encoding: utf-8

"""
Institut Villebon-Charpak
"""

from math   import *    # package pour les fonctions mathématiques (pi, cos, exp,...)
from random import *    # package pour les nombres (pseudo)-aléatoires

a = 1
b = 1024
continuer = True

while continuer:
    secret = randrange(a,b)
    print("*"*80)
    print('Je pense a un nombre entre entier ' + str(a) + ' et ' + str(b) + ', devine lequel !')
    found = False
    tries = 0
    while not found:
        guess = int(input())
        if guess < secret :
            print('Non, mon nombre est plus grand. Essaie encore.')
        elif guess > secret :
            print("Non, mon nombre est plus petit. Essaie encore.")
        else :
            found = True
        tries += 1
    print("Bravo ! Tu as devine que mon nombre etait " + str(secret) + ". Il t'a fallu " + str(tries) + " essais.")
    print("*"*80)
    print("Veux-tu rejouer ?")
    answer = raw_input()
    if answer[0] == "n" or answer[0] == "N":
        continuer = False
  
continuer = True

print('On va changer les rôles !')
while continuer:
    print("*"*80)
    print('Penses a un nombre entre entier ' + str(a) + ' et ' + str(b) + ", et je vais tenter de le deviner. Pense d'abord a ton nombre et appuie sur n'importe quelle touche pour commencer.")
    x = raw_input()
    found = False
    tries = 0
    c , d = a, b
    while not found:
        guess = (c+d)/2
        print("Est que ton nombres est " + str(guess) + " ?")
        answer = raw_input()+ " " # l'ajout de " " évite que la chaîne soit vide
        if answer[0] == ">":
                c, d = guess, d
        elif answer[0] == "<":
                c,d = c, guess
        else :
            found = True
        tries += 1
    print("Youhou, j'ai trouve ! Il m'a fallu " + str(tries) + " essais.")      
    print("Veux-tu rejouer ?")
    answer = raw_input()
    if answer[0] == "n" or answer[0] == "N":
        continuer = False
    

