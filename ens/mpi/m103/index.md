---
layout: page
title: Math103 - Algèbre linéaire
permalink: /ens/mpi/m103/
hidden : True
---
<script type="text/javascript">
<!--
    function toggle_visibility(id) {
       var elt = document.getElementById(id);
       if(elt.style.display == 'block')
          elt.style.display = 'none';
       else
          elt.style.display = 'block';
    }
//-->
</script>


# Math 103 - Algèbre linéaire

Il s'agit d'un cours d'introduction à l'algèbre linéaire. Les documents (polycopiés de cours et de TD) se trouvent sur [eCampus](https://ecampus.paris-saclay.fr).


## Enploi du temps

<!-- * Les vacances d'hiver auront lieu du 15 au 23 février. -->
* La partiel aura lieu le 10 mars à partir de 13h45 au bâtiment 337 (durée 2h).
* Les vacances de Pâques auront lieu du 11 au 19 avril.

## Carnet de bord

- <span class="date">6/03/2019 : **Dimension**</span>
- <span class="date">4/03/2019 : **familles libres, génératrices, bases, dimension**</span>
    * Correction du test 2
    * Exercices traités : 2.17
    * A traiter par vous-même : Montrer que la famille de polynômes $(p_0 : x \mapsto 1, p_1: x \mapsto x, p_2: x \mapsto x^2)$ est libre.

- <span class="date">28/02/2019 : **familles libres, génératrices, bases**</span>
    * **Test 1**
    * Exercices traités : 2.15
- <span class="date">26/02/2019 : **familles libres, génératrices, bases**</span>
    * Exercices traités : 2.11, 2.13, 2.14
    
- <span class="date">14/02/2019 : **sous espaces vectoriels, familles libres**</span>
    * Exercices traités : 2.5, 2.6, 2.7
- <span class="date">12/02/2019 : **sous espaces vectoriels, familles libres**</span>
    * Exercices traités : 2.2 *(fin)*, 2.3, 2.4, 2.5 *(question 1)* 
    * A traiter par vous-même : 2.5 *(fin)*

- <span class="date">7/02/2019 :</span> **Systèmes linéaires, sous espaces vectoriels**
    * Exercices traités : 1.5, 1.11, 2.1, 2.2 *(début)*
    * A traiter par vous-même : 2.2 *(fin)*
    
- <span class="date">5/02/2019 :</span> **Systèmes linéaires**
    * Exercices traités : 1.8, 1.9, 1.12 *(début)*
    * A traiter par vous-même : 1.12 *(fin)* <a onclick="toggle_visibility('1.12');">*(afficher/masquer la solution)*</a>
        <div id="1.12" class="sol">
        <p>Appelons $D_3$ la droite perpendiculaire à $D_1$ et $D_2$ (il y a bien une unique telle droite). En faisant le produit vectoriel des vecteurs directeurs de $D_1$ et $D_2$, on trouve le vecteur $(-1,2,-1)$ qui est simultanément perpendiculaire au deux précédents, donc directeur de $D_3$. Il nous reste à déterminer un point de $D_3$. Soient $A_1 \in D_1$ et $A_2 \in D_2$, alors $A_1$ et $A_2$ sont sur $D_3$ si et seulement si le vecteur $\overrightarrow{A_1A_2}$ est colinéaire à $(-1,2,-1)$. Ce qui nous fournit donc un point (et même deux) de la droite $D_3$. On cherche donc $u,t$ tels qu'il existe $v$ tel que</p>
        
        $$(1+u,u,u) - (t,2t,3t) = v.(-1,2,-1)$$
        
        <p>En d'autres termes, si $(t,u,v)$ est solution de ce système, alors les points $(1+u,u,u)$ et $(t,2t,3t)$ seront sur $D_3$. La résolution du système conduit à $(t,u,v) = \frac{1}{6} (-3,-8,-1)$ est donc les points sont $A_1 = -\frac{1}{3}(1,4,4)$ et $A_2 = -\frac{1}{2}(1,2,3)$.</p>
        
        <p><b>Methode alternative :</b> Sans connaître de vecteur directeur pour $D_3$, on peut utiliser une méthode similaire pour trouver deux points de $D_3$ (ce qui nous fournit un point et un vecteur directeur). En effet, si $A_1 \in D_1$ et $A_2 \in D_2$, alors $D_1$ et $D_2$ sont sur $D_3$ si et seulement si le vecteur $\overrightarrow{A_1A_2}$ est simultanément perpendiculaire à $(1,1,1)$ et $(1,2,3)$. En écrivant la nullité des deux produits scalaires, cela donne donc le système</p>
        
        $$
        \left\{\begin{matrix}(1+u-t,u-2t,u-3t) \cdot (1,1,1) & = & 0\\
        (1+u-t,u-2t,u-3t) \cdot (1,2,3) & = & 0\end{matrix}\right.
        $$
        <p>Ce qui donne la même solution $t = -\frac{1}{2}$ et $u = -\frac{4}{3}$ et donc les points $A_1 = -\frac{1}{3}(1,4,4)$ et $A_2 = -\frac{1}{2}(1,2,3)$. Et enfin le vecteur $\overrightarrow{A_1A_2} = \frac{1}{6}(1,-2,1)$ est alors un vecteur directeur de $D_3$.</p>
        </div>
    * Pour aller plus loin : 1.10, 1.13
    

- <span class="date">31/01/2019 :</span> **Systèmes linéaires**
	* Exercices traités : 1.6, 1.7, 1.3 *(début)*
	* A traiter par vous-même : 1.3 *(fin)*
	* **Solution de l'énigme :** <a onclick="toggle_visibility('enigme');">*(afficher/masquer)*</a>
		<div id="enigme" class="sol">
		Soit $h_e$ la hauteur (comptée en nombre de marches) de l'escalator. On note $v_a$ la vitesse d'Alice, $v_e$ la vitesse de l'escalator, et $t_a$ la durée de montée de l'escalator pour Alice. Dans un référentiel fixe, Alice a monté $h_e$ marches à vitesse $v_a+v_e$, donc
		
		$$(v_a + v_e) t_a = h_e$$
		
		Dans le référentiel de l'escalator, Alice à monté 28 marches à vitesse $v_a$, donc
		
		$$v_a t_a = 28$$
		
		En faisant le quotient (ce qui permet de se débarasser de $t_a$), on trouve
		
		$$\frac{h_e}{28} = \frac{v_a+v_e}{v_a} =  1 + \frac{v_e}{v_a} \iff \frac{h_e}{14} = 2 + 2 \frac{v_e}{v_a}$$
		
		De même pour Bob, on trouve l'équation
		
		$$\frac{h_e}{21} = \frac{v_a/2+v_e}{v_a/2} =  1 + 2\frac{v_e}{v_a}$$
		
		En faisant la soustraction (qui permet de se débarraser de $\frac{v_e}{v_a}$), on trouve
		
		$$\pars{\frac{1}{14}-\frac{1}{21}} h_e = 1 \iff h_e = 42$$
	
		<b>Remarque :</b> Si $(v_a, v_e, t_a ,t_b, h_e)$ est une solution de ce problème, alors $(\lambda v_a, \lambda v_e, \lambda^{-1} t_a, \lambda^{-1} t_b, h_e)$) est une autre solution. Donc il n'y a pas une valeur unique pour les vitesses et les durées, et il ne faut pas s'inquiéter de n'avoir écrit que 4 équations pour 5 inconnues.</div>

- <span class="date">29/01/2019 :</span> **Systèmes linéaires**
	* [Présentation de l'UE](m103syllabus.pdf)
	* Exercices traités : 1.1, 1.2, 1.4
	* A traiter par vous-même : 1.5
	* Enigme : Alice et Bob montent en marchant un escalier mécanique en mouvement. Lorsque Bob arrive en haut de l’escalier, il a monté 21 marches alors qu'Alice, avec une vitesse double de celle de Bob en a monté 28. Combien de marches l’escalier possède-t-il au repos ? [Source : Images des Mathématiques](http://images.math.cnrs.fr/Janvier-2019-2e-defi.html)
			
