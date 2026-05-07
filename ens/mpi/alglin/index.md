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

<article data-date="2026-05-11">
	<h4 class="date">11/05/2026 : Théorème du rang</h4>
	<p>Soient $E$ et $F$ des espaces vectoriels de dimension finie et $f : E \to F$.</p>
	<ol>
		<li>
			<p>Justifier que</p>
			$$0 \le \dim(\im f) \le \dim(F), \qquad \qquad 0 \le \dim(\ker f) \le \dim(E)$$
		</li>
		<li>Enoncer le théorème du rang.</li>
		<li>
			<p>En déduire que</p>
			$$\dim(F) - \dim(\im f) \ge \dim(F)-\dim(E), \qquad \qquad \dim(\ker f) \ge \dim(E)-\dim(F)$$
		</li>
	</ol>

	<details>
		<summary>Solution</summary>
		<ol>
			<li><p>On a les inclusions $\set{0_E} \subset \ker f \subset E$ et $\set{0_F} \subset \im f \subset F$ donc en prenant les dimension</p>
			$$0 \le \dim(\im f) \le \dim(F), \qquad \qquad 0 \le \dim(\ker f) \le \dim(E)$$
			</li>
			<li>
				<p>Le théorème du rang donne la relation :</p>
				$$\dim(E) = \dim(\im(f)) + \dim(\ker(f))$$
			</li>
			<li>
				<p>On a donc</p>
				$$\begin{align*}
				\dim(F) - \dim(\im f) &= \dim(F) - \dim(E) + \dim(\ker f) \\
				&\ge \dim(F) - \dim(E)
				\end{align*}$$
				<p>et</p>
				$$\begin{align*}
				\dim(\ker f) &= \dim(E) - \dim(\im f) \\
				&\ge \dim(E) - \dim(F)
				\end{align*}$$
			</li>
		</ol>
	</details>
</article>

<article data-date="2026-05-10">
	<h4 class="date">10/05/2026 : Majoration de la dimension de l'image</h4>
	<p>Soit $f : \R^2 \to \R^6$ linéaire.</p>
	<ol>
		<li>Enoncer le théorème du rang.</li>
		<li>
			<p>Montrer que</p>
			$$\dim(\im f) \le 2$$
		</li>
	</ol>

	<details>
		<summary>Question 1</summary>
		<p>D'après le théorème du rang :</p>
		$$\dim(\R^2) = 2 = \dim(\im f) + \dim(\ker f)$$
	</details>
	<details>
		<summary>Question 2</summary>
		<p>On a donc :</p>
		$$\begin{align*}
			\dim(\im(f)) &= 2 - \dim(\ker f) \\
			&\le 2 \\
		\end{align*}$$
	</details>
</article>

<article data-date="2026-05-09">
	<h4 class="date">9/05/2026 : Minoration de la dimension du noyau</h4>
	<p>Soit $f : \R^8 \to \R^5$ linéaire.</p>
	<ol>
		<li>
			<p>Montrer que</p>
			$$\dim(\im f) \le 5$$
		</li>
		<li>Enoncer le théorème du rang.</li>
		<li>
			<p>En déduire que</p>
			$$\dim(\ker f) \ge 3$$
		</li>
	</ol>

	<details>
		<summary>Question 1</summary>
		
		<p>On a l'inclusion $\im f \subset \R^5$, donc en prenant les dimensions :</p>
		$$\dim(\im f) \le 5$$
	</details>
	<details>
		<summary>Question 2</summary>
			<p>Le théorème du rang donne la relation :</p>
			$$\dim(\R^8) = 8 = \dim(\im(f)) + \dim(\ker(f))$$
	</details>
	<details>
		<summary>Question 3</summary>
		<p>On a donc</p>
		$$\begin{align*}
			\dim(\ker(f)) &= 8 - \dim(\im f) \\
			&\ge 8 - 5 \\
			&\ge 3
		\end{align*}$$
	</details>
</article>

<article data-date="2026-05-08">
	<h4 class="date">8/05/2026 : Un projecteur</h4>
	<p>On note $\mathcal{B}_0 = (e_1, e_2, e_3)$ la base canonique de $\R^3$, et on pose</p>
	$$u_1 = (1,0,0), \quad u_2 = (2,1,0), \quad u_3 = (0,0,1), \quad \mathcal{B} = (u_1,u_2,u_3)$$
	<p>Soit $E = \Vect(u_1, u_2)$ et $F = \Vect(u_3)$. Soit $p$ le projecteur sur $E$ parallèlement à $F$.</p>
	<ol>
		<li>Exprimer $A := \mat_{\mathcal{B}}(p)$ la matrice de $p$ dans la base $\mathcal{B}$.</li>
		<li>Exprimer $P := P(\mathcal{B}_0 \leftarrow \mathcal{B})$ la matrice de passage de $\mathcal{B}_0$ à $\mathcal{B}$</li>
		<li>Exprimer $B := \mat_{\mathcal{B}_0}(p)$ en fonction de $A$ et $P$.</li>
	</ol>
	<details>
		<summary>1. Matrice dans $\mathcal{B}$</summary>
		<p>Comme $p$ est le projecteur sur $\Vect(u_1, u_2)$ parallèlement à $\Vect(u_3)$ alors $p(u_1) = u_1$, $p(u_2) = u_2$ et $p(u_3) = 0$. On a donc</p>
		$$A = \mat_{\mathcal{B}}(p) = \begin{pmatrix}1 & \color{lightgray}{0} & \color{lightgray}{0} \\ \color{lightgray}{0} & 1 & \color{lightgray}{0} \\ \color{lightgray}{0} & \color{lightgray}{0} & 0\end{pmatrix}$$
	</details>
	<details>
		<summary>2. Matrice de passage</summary>
		<p>La matrice de passage de $\mathcal{B}_0$ à $\mathcal{B} est</p>
				$$P = P(\mathcal{B}_0 \leftarrow \mathcal{B}) = \begin{pmatrix}1 & 2 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix}$$
	</details>
	<details>
		<summary>3. Matrice dans la base canonique</summary>
		<p>La formule de changement de base nous donne</p>
		$$\begin{align*}
			B &= \mat_{\mathcal{B}_0}(p) \\
			&= P(\mathcal{B}_0 \times \leftarrow \mathcal{B}) \times \mat_{\mathcal{B}}(p) \times P(\mathcal{B} \leftarrow \mathcal{B}_0) \\
			&= P  \, A \, P^{-1} \\
		\end{align*}$$
		<h6>Remarque :</h6>
		<p>Ici, le calcul donnerait :</p>
		$$\begin{align*}
		B &= \begin{pmatrix}1 & 2 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix}
		\begin{pmatrix}1 & \color{lightgray}{0} & \color{lightgray}{0} \\ \color{lightgray}{0} & 1 & \color{lightgray}{0} \\ \color{lightgray}{0} & \color{lightgray}{0} & 0\end{pmatrix}
		\begin{pmatrix}1 & -2 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix} \\
		&=
		\begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0\end{pmatrix}
		\end{align*}$$
		<p>La simplicité du résultat s'explique par le fait que $(e_1,e_2, e_3)$ est aussi une base adaptée à $p$ (au sens où $E = \Vect(e_1,e_2)$ et $F = \Vect(e_3)$).</p>
	</details>
</article>

<article data-date="2026-05-07">
	<h4 class="date">7/05/2026 : Une symétrie</h4>
	<p>On note $\mathcal{B}_0 = (e_1, e_2)$ la base canonique de $\R^2$, et on pose</p>
	$$u_1 = (1,1), \quad u_2 = (1,-1), \quad \mathcal{B} = (u_1,u_2)$$
	<p>Soit $D_1 = \Vect(u_1)$ et $D_2 = \Vect(u_2)$. Soit $s$ la symétrie par rapport à $D_1$ parallèlement à $D_2$.</p>
	<ol>
		<li>Faire un dessin des droites $D_1$, $D_2$, et pour un vecteur quelconque $u \in \R^2$, de son symétrique $s(u)$</li>
		<li>Exprimer $A := \mat_{\mathcal{B}}(s)$ la matrice de $s$ dans la base $\mathcal{B}$.</li>
		<li>Exprimer $P := P(\mathcal{B}_0 \leftarrow \mathcal{B})$ la matrice de passage de $\mathcal{B}_0$ à $\mathcal{B}$</li>
		<li>Exprimer $B := \mat_{\mathcal{B}_0}(s)$ en fonction de $A$ et $P$.</li>
	</ol>
	
	
	<details>
		<summary>1. Dessin</summary>
		<img src="/img/daily/symetrie.png" alt="Symetrie" style="border-radius : 1em;">
	</details>
	<details>
		<summary>2. Matrice dans $\mathcal{B}$</summary>
		<p>Comme $s$ est la symétrie sur $\Vect(u_1)$ parallèlement à $\Vect(u_2)$ alors $s(u_1) = u_1$ et $s(u_2) = -u_2$, donc</p>
		$$A = \mat_{\mathcal{B}}(s) = \begin{pmatrix}1 & \color{lightgray}{0} \\ \color{lightgray}{0} & -1\end{pmatrix}$$
	</details>
	<details>
		<summary>3. Matrice de passage</summary>
		<p>On a</p>
		$$P = P(\mathcal{B}_0 \leftarrow \mathcal{B}) = \begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix}$$
	</details>
	<details>
		<summary>4. Matrice dans $\mathcal{B}_0$</summary>
		<p>La formule de changement de base nous donne</p>
		$$\begin{align*}
			B
			&= \mat_{\mathcal{B}_0}(s) \\
			&= P(\mathcal{B}_0 \leftarrow \mathcal{B}) \times \mat_{\mathcal{B}}(s) \times P(\mathcal{B} \leftarrow \mathcal{B}_0) \\
			&= P \, A \, P^{-1}
		\end{align*}$$
	</details>
</article>

<article data-date="2026-05-06">
	<h4 class="date">6/05/2026 : De cartésien à paramétrique</h4>
	<p>Soit $E = \set{(x,y,z,t) \in \R^4 | x + 2y - z = t = 0}$ trouver la dimension et une base de $E$.</p>


	<details>
		<summary>Dimension</summary>
		<p>Soit $(x,y,z,t) \in \R^4$, on a</p>
		$$\begin{align*}(x,y,z,t) \in E
		&\iff
		(S)\left\{\begin{array}{llllc}
			x &+ 2y &- z & &= 0 \\
			&&&t &= 0
		\end{array}\right.
		\end{align*}$$
		<p>Le système $(S)$ est échelonné avec $2$ paramètres ($y$, $z$), donc $\dim(E) = 2$.</p>
	</details>
	<details>
		<summary>Base</summary>
		<p>Le système $(S)$ est déjà réduit, on paramètre ses solutions :</p>
		$$\begin{align*}(S)
		&\iff
		\left\{\begin{array}{rlrr}
			x &=& -2y &+ z \\
			y &=& y \\
			z &=& & z \\
			t &=& 0
		\end{array}\right. \\
		&\iff (x,y,z,t) = y . (-2,1,0,0) + z . (1,0,1,0)
		\end{align*}$$
		<p>Donc la famille $((-2,1,0,0),(1,0,1,0))$ est génératrice de $E$ et par dimension c'est une base de $E$.</p>
	</details>
</article>

<article data-date="2026-05-05">
	<h4 class="date">5/05/2026 : De paramétrique à cartésien</h4>
	<p><img src="/img/daily/exo11.jpg" style="border-radius : 1em;"/></p>


	<details>
		<summary>Question 1</summary>
		<img src="/img/daily/exo11sol1.jpg" style="border-radius : 1em;"/>
	</details>
	<details>
		<summary>Question 2</summary>
		<img src="/img/daily/exo11sol2.jpg" style="border-radius : 1em;"/>
	</details>
</article>

<article data-date="2026-05-04">
	<h4 class="date">4/05/2026 : Formule de changement de base (2)</h4>
	<p><img src="/img/daily/exo10.jpg" style="border-radius : 1em;"/></p>


	<details>
		<summary>Question 1</summary>
		<img src="/img/daily/exo10sol1.jpg" style="border-radius : 1em;"/>
	</details>
	<details>
		<summary>Question 2</summary>
		<img src="/img/daily/exo10sol2.jpg" style="border-radius : 1em;"/>
	</details>
</article>

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
		<img src="/img/daily/exo4sol.pdf" style="border-radius : 1em;"/>
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