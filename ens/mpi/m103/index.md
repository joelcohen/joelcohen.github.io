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

* Les vacances d'hiver auront lieu du 15 au 23 février.
* La partiel aura lieu la semaine du 9 au 13 mars.
* Les vacances de Pâques auront lieu du 11 au 19 avril.

## Carnet de bord


- <span class="date">31/01/2019 :</span> **Systèmes linéaires**
	* Exercices traités : 1.6, 1.7, 1.3 *(début)*
	* A traiter par vous-même : 1.3 *(fin)*
	* **Solution de l'énigme :** <span onclick="toggle_visibility('enigme');">*(afficher/masquer)*</span>
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
	
		**Remarque :** Si $(v_a, v_e, t_a ,t_b, h_e)$ est une solution de ce problème, alors $(\lambda v_a, \lambda v_e, \lambda^{-1} t_a, \lambda^{-1} t_b, h_e)$) est une autre solution. Donc il n'y a pas une valeur unique pour les vitesses et les durées, et il ne faut pas s'inquiéter de n'avoir écrit que 4 équations pour 5 inconnues.</div>

- <span class="date">29/01/2019 :</span> **Systèmes linéaires**
	* [Présentation de l'UE](m103syllabus.pdf)
	* Exercices traités : 1.1, 1.2, 1.4
	* A traiter par vous-même : 1.5
	* Enigme : Alice et Bob montent en marchant un escalier mécanique en mouvement. Lorsque Bob arrive en haut de l’escalier, il a monté 21 marches alors qu'Alice, avec une vitesse double de celle de Bob en a monté 28. Combien de marches l’escalier possède-t-il au repos ? [Source : Images des Mathématiques](http://images.math.cnrs.fr/Janvier-2019-2e-defi.html)
			
