---
layout: page
title: Math103 - Algèbre linéaire
permalink: /ens/mpi/m103/
hidden : True
---


# Math 103 - Algèbre linéaire

Il s'agit d'un cours d'introduction à l'algèbre linéaire. Les documents (polycopiés de cours et de TD) se trouvent sur [Dokéos](http://formation.u-psud.fr).

## Dates à retenir

* Le test 1 aura lieu le jeudi 21 février à 8h15
* Le partiel est prévu le mardi 12 mars.

## Carnet de bord
- <span class="date">14/02/2019 :</span> **Suites génératrices, suites libres**
	* Exercices traités : 2.3, 2.4, 2.5

- <span class="date">7/02/2019 :</span> **Systèmes linéaires, sous-espaces vectoriels**
	* Exercices traités : 1.7 *(fin)*, 1.8, 1.9, 2.1, 2.2 *(sauf 2.c)*
	* A traiter par vous-même : 1.10, 1.11, 1.12, 1.13
	* Solution de l'énigme : 
		
		Soit $h_e$ la hauteur (comptée en nombre de marches) de l'escalator. On note $v_a$ la vitesse d'Alice, $v_e$ la vitesse de l'escalator, et $t_a$ la durée de montée de l'escalator pour Alice. Dans un référentiel fixe, Alice a monté $h_e$ marches à vitesse $v_a+v_e$, donc
		
		$$(v_a + v_e) t_a = h_e$$
		
		Dans le référentiel de l'escalator, Alice à monté 21 marches à vitesse $v_a$, donc
		
		$$v_a t_a = 21$$
		
		En faisant le quotient, on trouve
		
		$$\frac{h_e}{21} = \frac{v_a+v_e}{v_a} =  1 + \frac{v_e}{v_a}$$
		
		De même pour Bob, on trouve l'équation
		
		$$\frac{h_e}{28} = \frac{2v_a+v_e}{2v_a} \Longleftrightarrow \frac{h_e}{14} =  2 + \frac{v_e}{v_a}$$
		
		En faisant la soustraction, on trouve
		
		$$\pars{\frac{1}{14}-\frac{1}{21}} h_e = 1 \Longleftrightarrow h_e = 42$$
	
		**Remarque :** Si $(v_a, v_e, t_a ,t_b, h_e)$ est une solution de ce problème, alors $(\lambda v_a, \lambda v_e, \lambda^{-1} t_a, \lambda^{-1} t_b, h_e)$) est une autre solution. Donc il n'y a pas une valeur unique pour les vitesses et les durées, et il ne faut pas s'inquiéter de n'avoir écrit que 4 équations pour 5 inconnues.
	* Erratum exercice 1.7 :

- <span class="date">31/01/2019 :</span> **Systèmes linéaires**
	* Exercices traités : 1.1, 1.2, 1.4, 1.6, 1.7 *(partie)*
	* A traiter par vous-même : 1.5, 1.7 *(fin)*
	* [Enigme](http://images.math.cnrs.fr/Janvier-2019-2e-defi.html)		
