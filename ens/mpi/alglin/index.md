---
layout: page
title: Daily Challenge
permalink: /ens/mpi/linalg/
hidden : True
---
<script>
document.addEventListener("DOMContentLoaded", () => {
  const today = new Date();
  today.setHours(0,0,0,0);

  document.querySelectorAll("article[data-date]").forEach(article => {
    const [y, m, d] = article.dataset.date.split("-");

    const exoDate = new Date(Number(y), Number(m) - 1, Number(d));

    if (exoDate > today) {
      article.style.display = "none";
    }
  });
});
</script>


# Algèbre linéaire

<article style="display:block; clear: both;">
	<h2>Daily challenge</h2>
	<div id="name">
		<img src="/img/add2homescreen.png" alt="Ajoute cette page à l'écran d'acceuil de ton téléphone !" style="float:left; max-height:200px">
		<p>A l'approche de l'examen, je vous propose le challenge suivant : <strong>chaque jour</strong> un petit exercice court d'algèbre linéaire. Pour vous <strong>entrainer</strong>, pour <strong>reviser</strong> pour <strong>progresser</strong>. Prenez 5 à 10 minutes dans votre journée pour essayer de le résoudre, puis lire le corrigé. Promis, cette habitude devrait payer (non seulement sur votre note à l'examen mais aussi et surtout, je l'espère, sur votre maitrise à long terme de l'algèbre linéaire !). Pour y penser tous les jours, pensez à <strong>ajouter cette page sur l'écran d'accueil de votre téléphone</strong>.</p>
		<p>Si vous avez des questions, ou que vous pensez avoir trouvé une erreur, n'hésitez pas à me contacter !</p>
	</div>
</article>





<!-- 
<article>
	<h4 class="date">xx/04/2026 : Titre</h4>
	<img src="/img/daily/exon.jpg" style="border-radius : 1em;"/>
	<details>
		<summary>Solution</summary>
		<img src="/img/daily/exonsol.jpg" style="border-radius : 1em;"/>
	</details>
</article>
 -->

<article data-date="2026-05-03">
	<h4 class="date">3/05/2026 : Formule de changement de base</h4>
	<p><img src="/img/daily/exo9.png" style="border-radius : 1em;"/></p>
	<p>Bonus :</p>
	<p><img src="/img/daily/exo9_2.png" style="border-radius : 1em;"/></p>


	<details>
		<summary>Question 1</summary>
		<img src="/img/daily/exo9sol1.png" style="border-radius : 1em;"/>
	</details>
	<details>
		<summary>Question 2</summary>
		<img src="/img/daily/exo9sol2.png" style="border-radius : 1em;"/>
	</details>
	<details>
		<summary>Question 3</summary>
		<img src="/img/daily/exo9sol3.png" style="border-radius : 1em;"/>
	</details>
	<details>
		<summary>Question 4</summary>
		<img src="/img/daily/exo9sol4.png" style="border-radius : 1em;"/>
	</details>
</article>

<article data-date="2026-05-02">
	<h4 class="date">2/05/2026 : Noyau et image</h4>
	<img src="/img/daily/exo8.jpg" style="border-radius : 1em;"/>

	<details>
		<summary>Solution</summary>
		<img src="/img/daily/exo8sol.jpg" style="border-radius : 1em;"/>
	</details>
</article>

<article data-date="2026-04-30">
	<h4 class="date">30/04/2026 : Un automorphisme de $\R_3[X]$</h4>
	<img src="/img/daily/exo7.jpg" style="border-radius : 1em;"/>
	<strong>Bonus :</strong>
	<p>Montrer que $\varphi$ est un automorphisme et si $P = \sum_{k \le 3} a_k X^k$, déterminer l'expression de $\varphi^{-1}(P)$.</p>

	<details>
		<summary>Questions 1 et 2</summary>
		<img src="/img/daily/exo7sol1.jpg" style="border-radius : 1em;"/>
	</details>
	<details>
		<summary>Bonus</summary>
		<img src="/img/daily/exo7sol2.jpg" style="border-radius : 1em;"/>
	</details>
</article>


<article data-date="2026-04-29">
	<h4 class="date">29/04/2026 : Somme et intersection en paramétrique</h4>
	<p>Soient $E$ et $F$ ses sous-espaces vectoriels de $\R^7$. On se donne $\mathcal{B}_E = (e_1, e_2, e_3, e_4, e_5)$ une base de $E$ et $\mathcal{B}_F = (f_1, f_2, f_3, f_4)$ une base de $F$. On suppose que l'on échelonne la système :</p>
	$$\lambda_1 . e_1 + \ldots + \lambda_5 . e_5 + \lambda_6 . f_1 + \ldots + \lambda_9 . f_9 = 0$$
	<p>Et on trouve la forme échelonnée réduite suivante :</p>
	<p><img src="/img/daily/exo6.png" style="border-radius : 1em;"/></p>
	<details>
		<summary>Dimension et base de $E+F$</summary>
		<img src="/img/daily/exo6sol1.png" style="border-radius : 1em;"/>
	</details>
	<details>
		<summary>Dimension et base de $E \cap F$ <em>(pour la base, voir prop 35 du poly)</em></summary>
		<img src="/img/daily/exo6sol2.png" style="border-radius : 1em;"/>
	</details>
</article>

<article data-date="2026-04-28">
	<h4 class="date">28/04/2026 : Projection</h4>
	<img src="/img/daily/exo5.jpg" style="border-radius : 1em;"/>
	<details>
		<summary>Solution</summary>
		<img src="/img/daily/exo5sol.jpg" style="border-radius : 1em;"/>
	</details>
</article>

<article data-date="2026-04-27">
	<h4 class="date">27/04/2026 : Dimension et base en paramétrique</h4>
	<img src="/img/daily/exo4.jpg" style="border-radius : 1em;"/>
	<details>
		<summary>Solution</summary>
		<img src="/img/daily/exo4sol.jpg" style="border-radius : 1em;"/>
	</details>
</article>

<article data-date="2026-04-26">
	<h4 class="date">26/04/2026 : Supplémentaires</h4>
	<img src="/img/daily/exo3.jpg" style="border-radius : 1em;"/>
	<details>
		<summary>Solution</summary>
		<img src="/img/daily/exo3sol.jpg" style="border-radius : 1em;"/>
	</details>
</article>

<article data-date="2026-04-25">
	<h4 class="date">25/04/2026 : Dimension et base</h4>
	<img src="/img/daily/exo2.png" style="border-radius : 1em;"/>
	<details>
		<summary>Solution pour $E_1$</summary>
		<img src="/img/daily/exo2sol1.png" style="border-radius : 1em;"/>
	</details>
	<details>
		<summary>Solution pour $E_2$</summary>
		<img src="/img/daily/exo2sol2.png" style="border-radius : 1em;"/>
	</details>
	<details>
		<summary>Solution pour $E_3$</summary>
		<img src="/img/daily/exo2sol3.png" style="border-radius : 1em;"/>
	</details>
	<details>
		<summary>Solution pour $E_4$</summary>
		<img src="/img/daily/exo2sol4.png" style="border-radius : 1em;"/>
	</details>
</article>


<article data-date="2026-04-24">
	<h4 class="date">24/04/2026 : Changement de bases</h4>
	<img src="/img/daily/exo1.png" style="border-radius : 1em;"/>
	<details>
		<summary>Solution</summary>
		<img src="/img/daily/exo1sol.png" style="border-radius : 1em;"/>
	</details>
</article>

<article data-date="2026-04-23">
	<h4 class="date">23/04/2026 : Dimension et base en cartésien</h4>
	<img src="/img/daily/exo0.png" style="border-radius : 1em;"/>
	<details>
		<summary>Solution</summary>
		<img src="/img/daily/exo0sol.png" style="border-radius : 1em;"/>
	</details>
</article> 


<!-- On note $\mathcal{B}_0$ la base canonique de $\R^2$. Et soient

$$u_1 = \begin{pmatrix}5 \\ 0\end{pmatrix} \qquad u_2 = \begin{pmatrix}2 \\ -1\end{pmatrix} \qquad \mathcal{B} = (u_1 , u_2)$$.

1. Que vaut $P_{\mathcal{B}_0 \leftarrow \mathcal{B}}$ ?
2. Calculer $P_{\mathcal{B} \leftarrow \mathcal{B}_0}$.
3. Coordonnées du vecteur $(x,y)$ dans la base $\mathcal{B}$ ?

*-->