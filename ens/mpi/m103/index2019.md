---
layout: page
title: Math103 - Algèbre linéaire
permalink: /ens/mpi/m103/2019/
hidden : True
---


# Math 103 - Algèbre linéaire

Il s'agit d'un cours d'introduction à l'algèbre linéaire. Les documents (polycopiés de cours et de TD) se trouvent sur [Dokéos](http://formation.u-psud.fr).

## Enploi du temps

* **Le TD de l'après midi est déplacé au matin 10h30-12h30**
* Le test 2 aura lieu le jeudi 18 avril à 8h15
* L'examen est prévu le jeudi 16 mai de 13h45 à 15h45

## Carnet de bord

- <span class="date">11/04/2019 :</span> **Applications linéaires**
    * Exercices traités : 5.3, 5.4, 5.8, 5.9
    * A traiter par vous-même : 5.1, 5.5

- <span class="date">4/04/2019 :</span> **Matrices et applications linéaires**
    * Exercices traités : 4.7, 4.8, 4.9, 5.2

- <span class="date">28/03/2019 :</span> **Matrices**
	* Exercices traités : 4.1, 4.2, 4.3, 4.4, 4.5, 4.6

- <span class="date">21/03/2019 :</span> **Dimension. Intersection et somme de sous-espaces. Equations cartésiennes** 
    * Exercices traités : 3.7, 3.8, 3.11, 3.13
    * A traiter par vous-même : 3.2, 3.3, 3.4, 3.9
	* Fin de l'exercice 3.13 : 
		1. On pose $T_0 = 1$, $T_1(x) = x$ et $T_{n+2} = 2 X T_{n+1} - T_n$. Vérifions par récurrence que pour tout $n \in \N$ et tout $\theta \in \R$, $T_n(\cos \theta) = \cos(n \theta)$. Pour $n = 0$ et $n = 1$, c'est évident. Supposons désormais la propriété vrai **jusqu'au** rang $n+1$, et montrons-la au rang $n+2$. Pour $\theta \in \R$, on a

			$$\begin{align*} T_{n+2}(\cos(\theta)) &= 2 \cos(\theta) T_{n+1}(\cos \theta) - T_n(\cos \theta) \\
			&= 2 \cos(\theta) \cos((n+1)\theta) - \cos(n \theta) \\
			&= \cos((n+1) \theta + \theta) + \cos((n+1) \theta - \theta) - \cos(n \theta)\\
			&= \cos((n+2) \theta)\end{align*}$$
			
		2. Comme $\deg T_k = k$ pour tout $k \in \N$, alors la famille $(T_0, T_1, \ldots T_d)$ est une base de $\R_d[X]$ (cf exercice 3.12 question 1).
		
		3. On a
			
			$$\int_0^{\pi} T_n(\cos \theta) \times T_m(\cos \theta) \, d\theta = \begin{cases} 0 & \text{si } m \ne n \\ \frac{\pi}{2} & \text{si } m = n\end{cases}$$
			
			D'après la question 2, la famille $(T_0, T_1, \ldots T_d)$ est une base de $\R_d[X]$, donc tout polynôme $P \in \R_d[X]$ s'écrit de manière unique
			
			$$P = \sum_{k = 0}^d \lambda_k T_k$$
			
			avec $\lambda_0, \lambda_1, \ldots, \lambda_d \in \R$. Soit $0 \le i \le d$ un entier. Pour trouver le coefficient $\lambda_i$, on peut intégrer $P(\cos \theta) T_i(\cos \theta)$ :
			
			$$\int_0^{\pi} P(\cos \theta) \times T_i(\cos \theta) \, d\theta =  \sum_{k = 0}^d \lambda_k \underbrace{\int_0^{\pi} T_k(\cos \theta) \times T_i(\cos \theta) \, d\theta}_{\text{nul si } k \ne i} = \frac{\pi}{2} \lambda_i$$
			
		    d'où on tire la formule
			
			$$\lambda_i = \frac{2}{\pi} \int_0^{\pi} P(\cos \theta) \times T_i(\cos \theta) \, d\theta$$
		
	
- <span class="date">28/02/2019 :</span> **Dimension, Opérations sur les sous-espaces**
	* Exercices traités : 3.1, test 1.11, test 1.5, 3.5, 3.6
	
- <span class="date">21/02/2019 :</span> **Bases, coordonnées, dimension**
	* Exercices traités : 2.12, 2.13, 2.14, 2.17, 3.12
	* A traiter par vous-même : 2.15
	* Base canonique de $\mathcal{P}_n(\R)$ *(solution)*:
		1. Commençons par montrer que la famille $(e_0, \ldots, e_n)$ est **génératrice** de $\mathcal{P}_n(\R)$ : Soit $P \in \mathcal{P}_n(\R)$. Nommons les coefficients de $P$, on écrit
			
			$$P(x) = a_n x^n + a_{n-1} x^{n-1} + \ldots + a_1 x + a_0$$
			
			Cette écriture nous donne directement que $P$ est une combinaison linéaire des $e_i$. En effet, l'égalité ci-dessus se traduit par la relation vectorielle
			
			$$P = a_n . e_n + a_{n-1} . e_{n-1} + \ldots + a_1 . e_1 + a_0 . e_0$$
			
			Montrons désormais que la famille $(e_0, \ldots, e_n)$ est **libre**. Pour cela on montre par récurrence sur $n \ge 0$ la propriété suivante : pour $n \in \N$, la famille $(e_0, \ldots, e_n)$ est libre.
			
			**Pour $n = 0$ :** Nous devons montrer que la famille $(e_0)$ est libre. Soit $\lambda_0 \in \R$, tel que $\lambda_0 . e_0 = 0$, ce qui nous donne $\lambda_0 \times 1 = 0$, donc $\lambda_0 = 0$. Donc la famille $(e_0)$ est effectivement libre.
			
			**Hérédité :** Soit $n \ge 1$. Supposons la propriété vraie jusqu'au rang $n-1$, et montrons-la au rang $n$. On se donne $\lambda_0, \lambda_1, \ldots, \lambda_{n} \in \R$ tels que 
			$\lambda_0 . e_0 + \lambda_1 . e_1 + \ldots + \lambda_{n}.e_{n} = 0$
			c'est-à-dire que pour tout $x \in \R$, on a
			
			$$\lambda_0  + \lambda_1 x + \ldots + \lambda_{n} x^n = 0$$
			
			On souhaite montrer que les $\lambda_i$ sont tous nuls. En $x=0$, on trouve $\lambda_0 = 0$. Et donc pour tout $x \in \R$, on a
			
			$$x \pars{\lambda_1 + \ldots + \lambda_{n} x^{n-1}} = 0$$
			
			Ainsi, pour tout $x \in \R^*$, on a
			
			$$\lambda_1 + \ldots + \lambda_{n} x^{n-1} = 0$$
			
			Et en passant à la limite à $0$, l'égalité ci-dessus reste vraie en $0$; donc elle est vraie sur $\R$ tout entier. En d'autres termes, on a $\lambda_1 . e_0 + \lambda_1 . e_0 + \ldots + \lambda_{n}.e_{n-1} = 0$. Or par hypothèse de récurrence, la famille $(e_0, \ldots, e_{n-1})$ est libre, ce qui implique que $\lambda_1 = \ldots = \lambda_n = 0$. Et on a fini !
			
			La conclusion est que la famille $(e_0, e_1, \ldots, e_n)$ est une base de $\mathcal{P}_n(\R)$ (en particulier, cela montre que l'espace vectoriel $\mathcal{P}_n(\R)$ est de dimension $n+1$).
			
		2. Si $P(x) = Q(x)$ pour tout $x \in \R$, on obtient en faisant la différence
			
			$$(a_n - b_n) x^n + (a_{n-1} - b_{n-1}) x^{n-1} + \ldots + (a_0 - b_0) = 0$$
			
			et d'après la question précédente, cela implique $a_n - b_n = a_{n-1} - b_{n-1} = \ldots = a_0 - b_0 = 0$, c'est-à-dire que 
			
			$$a_n = b_n, \ a_{n-1}=b_{n-1}, \ldots , \ a_0 = b_0$$
			
			En d'autres termes, on a montré que si deux fonctions polynomiales prennent les mêmes valeurs sur $\R$, alors leurs coefficients sont égaux.
			
- <span class="date">14/02/2019 :</span> **Suites génératrices, suites libres**
	* Exercices traités : 2.3, 2.4, 2.5, 2.7, 2.9, 2.11 (début)
    * A traiter par vous-même : 2.6, 2.8, 2.10
	* Base canonique de $\mathcal{P}_n(\R)$ *(laissé en exercice)* :
		1. Pour $k \in \N$, on définit le polynôme $e_k : x \mapsto x^k$. Montrer que la famille $(e_0, \ldots, e_n)$ est une base de $\mathcal{P}_n(\R)$ *(pour la liberté, on pourra procéder par récurrence sur $n \ge 0$)*.
		2. Soient $P, Q \in \mathcal{P}_n(\R)$.
		
			On note $P(x) = a_n x^n + \ldots + a_1 x + a_0$ et $Q(x) = b_n x^n + \ldots + b_1 x + b_0$. On suppose que pour tout $x \in \R$, $P(x) = Q(x)$, montrer que $a_n = b_n$, $a_{n-1}=b_{n-1}$, $\ldots$ , $a_0 = b_0$.

- <span class="date">7/02/2019 :</span> **Systèmes linéaires, sous-espaces vectoriels**
	* Exercices traités : 1.7 *(fin)*, 1.8, 1.9, 2.1, 2.2 *(sauf 2.c)*
	* A traiter par vous-même : 1.10, 1.11, 1.12, 1.13
	* **Solution de l'énigme :** 
		
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
