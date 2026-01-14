---
layout: page
title: DU3R - projet mathématique
permalink: /ens/DU3R/
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


<!-- <link rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/prismjs/themes/prism.css"> -->
<script src="https://cdn.jsdelivr.net/npm/prismjs/prism.js"></script>
<script src="https://cdn.jsdelivr.net/npm/prismjs/components/prism-glsl.min.js"></script>

<style>
	.example {
	  display: flex;
	  flex-direction: column;
	  gap: 0px;
	  align-items: stretch;
	  margin: 2em 0;
	}

	.shader {
	  width: 100%;
	  min-height: 30em;
	  background: black;
	  /*flex-shrink: 0;*/
	  border-radius : 10px;
	}

	pre {
	  f/*lex: 1;*/
	  margin: 0;
	  padding: .2em;
	  overflow: visible;
	  font-size: 11px;
	  border : none;
	}
	@media (max-width: 700px) {
	  .example {
	    flex-direction: column;
	  }
	  .shader {
	    width: 100%;
	  }
	}
</style>
<script type="module">
import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';

function createShader(container, shaderId) {

  // 1. Read user shader (Shadertoy-style)
  const userShader =
    document.getElementById(shaderId).textContent.trim();

  // 2. Inject boilerplate
  const fragmentShader = `
uniform vec3 iResolution;
uniform float iTime;
uniform vec4 iMouse; // xy = current, zw = click

${userShader}

void main() {
  mainImage(gl_FragColor, gl_FragCoord.xy);
}
`;

  // 3. Show FINAL shader code
  const codeBlock = container.nextElementSibling.querySelector('code');
  codeBlock.textContent = userShader;
  Prism.highlightElement(codeBlock);

  // --- Three.js boilerplate ---
  const scene = new THREE.Scene();
  const camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);

  const renderer = new THREE.WebGLRenderer();
  
  container.appendChild(renderer.domElement);

  const material = new THREE.ShaderMaterial({
    fragmentShader,
    uniforms: {
      iTime: { value: 0 },
      iResolution: { value: new THREE.Vector3() },
      iMouse: { value: new THREE.Vector4() }
    }
  });
  
  // Update from mouse events
  container.addEventListener('mousemove', e => {
    const r = container.getBoundingClientRect();
    material.uniforms.iMouse.value.x = e.clientX - r.left;
    material.uniforms.iMouse.value.y = r.height - (e.clientY - r.top);
  });

  container.addEventListener('mousedown', () => {
    material.uniforms.iMouse.value.z = material.uniforms.iMouse.value.x;
    material.uniforms.iMouse.value.w = material.uniforms.iMouse.value.y;
  });

  const mesh = new THREE.Mesh(
    new THREE.PlaneGeometry(2, 2),
    material
  );
  scene.add(mesh);

  function resize() {
    const w = container.clientWidth;
    const h = container.clientHeight;
    renderer.setSize(w, h, false);
    material.uniforms.iResolution.value.set(w, h, 1);
  }
  resize();

  function animate(time) {
    material.uniforms.iTime.value = time * 0.001;
    renderer.render(scene, camera);
    requestAnimationFrame(animate);
  }
  requestAnimationFrame(animate);

  window.addEventListener('resize', resize);
}

// Init all shaders
document.querySelectorAll('.shader').forEach(div => {
  createShader(div, div.dataset.shader);
});
</script>


# Présentation

Ces notes cours sont en grande partie tirées de l'excellent [cours](https://shaders.stevejtrettel.site) de [Steve Trettel](https://stevejtrettel.site). Si vous êtes curieux et souhaitez aller plus loin, je vous recommande la lecture de ses notes (en anglais).


## Objectif

Le but de ce cours est d'être une courte introduction aux shaders, programmes qui permettent d'utiliser la puce graphique de votre ordinateur pour générer des images et animations. Il ne s'agit en aucun cas d'une présentation exhaustive du sujet donc je ne suis pas expert.

C'est une occasion pour mettre en application vos connaissances mathématiques notamment en géométrie, mais aussi j'espère, les étendre dans divers domaines. Le but est de vous faire comprendre ce qui se passe dans l'ordinateur quand une image s'affiche, et vous montrer en particulier comment les mathématiques y interviennent. Mais c'est aussi une opportunité pour vous amuser à créer et explorer ! Ci-dessous un exemple de shader (celui qu'on trouvera par défaut sur shadertoy), avec le code associé. On voit que quelques seulement lignes de codes ont suffi à produire cet exemple !


<div class="example">
  <div class="shader" data-shader="shader1"></div>
  <pre>
	<code id="code1" class="language-glsl"></code>
	
	<script type="x-shader/x-fragment" id="shader1">
	void mainImage(out vec4 fragColor, in vec2 fragCoord) {
	  vec2 uv = fragCoord / iResolution.xy;
	  vec3 col = 0.5 + 0.5 * cos(iTime + uv.xyx + vec3(0,2,4));
	  fragColor = vec4(col, 1.0);
	}
	</script>
</pre>
</div>

Notre but sera notamment d'en comprendre le fonctionnement.

## Prérequis

Ce cours nécessite l'accès à un ordinateur connecté à internet. On écrira du code pour produire nos images et animations donc une expérience préalable de la programmation peut être utile, mais n'est pas nécessaire car on va repartir de la base. Et on ne suppose pas de familiarité avec ce langage en particulier. Je vous propose de suivre en écrivant le code même temps que moi. En cas de besoin, il est possible de le copier-coller du code directement depuis ce site.

## Shadertoy

Dans ce cours, on utilisera l'outil [shadertoy](https://www.shadertoy.com/) pour écrire notre code. C'est une plateforme en ligne qui va simplifier le travail en vous évitant de devoir installer quoi que ce soit en local sur votre machine. Je vous conseille de commencer par créer un compte sur le site afin de pouvoir sauvegarder votre travail. Attention : la sauvegarde n'est pas automatique, vous devez enregistrer à la main !

## Modélisation

### Cadre

Pour nous, le cadre d'une image (ou canevas) c'est une région rectangulaire du plan. Un point du cadre est décrit par ses coordonnées $(x,y)$.

### Couleurs

Sur un écran, les couleurs sont affichées par combinaison de lumières rouge, verte et bleue. Chaque couleur produite par l'écran est donc décrite par les valeurs de luminosité du rouge, vert et bleu entre $0$ et $1$ ($1$ représentant l'intensité maximale). Ainsi une couleur sera représentée par un triplet de valeur $(r,g,b)$ qui varient entre $0$ et $1$. Ainsi, $(0,0,0)$ représente le noir, $(1,1,1)$ le blanc, $(1,0,0)$ le rouge pur, $(0,1,0)$ le bleu pur, $(0,0,1)$ le vert pur.

- $(0,0,0)$ : noir
- $(1,1,1)$ : blanc
- $(1,0,0)$ : rouge
- $(0,1,0)$ : vert
- $(0,0,1)$ : bleu

À ces 3 coordonnées, shadertoy ajoute egalement une quatrième coordonnée $(r,g,b,a)$ pour prendre en compte la transparence ($0$ pour complètement transparent, $1$ pour totalement opaque). Cette dernière valeur vaudra toujours $1$ pour nous.

### Image

Une image, c'est simplement la donnée pour chaque point $(x,y) du cadre de sa couleur $(r,g,b)$. En mathématiques, on dirait qu'une image est donc une fonction :

$$\text{image} : (x,y) \longmapsto (r, g, b)$$

Et c'est aussi comme ça qu'on peut penser quand on génère une image : décrire une image revient à décider pour chaque pixel, de quelle couleur il sera.


# Premiers pas

## 


Dans shaderToy, la fonction s'appelle `mainImage` :

```
void mainImage(out vec4 fragColor, in vec2 fragCoord)
{
    // votre code ici
}
```

## Couleur unie

Commençons par l'exemple le plus basique : afficher une couleur unie sur toute l'image.

<div class="example">
  <div class="shader" data-shader="shader2"></div>
  <pre>
	<code id="code2" class="language-glsl"></code>
	<script type="x-shader/x-fragment" id="shader2">

	void mainImage(out vec4 fragColor, in vec2 fragCoord)
	{
	    fragColor = vec4(0.0, 0.0, 1.0, 1.0);
	}
	</script>
</pre>
</div>

On voit un écran tout bleu. Que signifie ce code ? Regardons en particulier la ligne suivante :

```
	fragColor = vec4(0.0, 0.0, 1.0, 1.0);
```
Dans shaderToy, la variable `fragColor` désigne la couleur que l'on va afficher. Ici l'instruction consiste à assigner la valeur `vec4(0.0, 0.0, 1.0, 1.0)` à cette variable (ce qui correspond à la couleur bleue).

### Exercice

Comment modifier le code ci-dessus pour afficher du rouge, vert, blanc, jaune, cyan, magenta, gris ?

## Prise en compte de la position

Pour rendre les choses plus intéressantes, essayons désormais de colorer l'image en fonction de la position. Pour commencer, colorons la gauche de l'écran en bleu sur 100 pixels de large, et le reste en rouge.


<div class="example">
  <div class="shader" data-shader="shader3"></div>
  <pre>
	<code id="code3" class="language-glsl"></code>
	<script type="x-shader/x-fragment" id="shader3">

	void mainImage(out vec4 fragColor, in vec2 fragCoord)
	{
	    if (fragCoord.x < 100.0){
			fragColor = vec4(0.0, 0.0, 1.0, 1.0); // bleu
		}
		else {
			fragColor = vec4(1.0, 0.0, 0.0, 1.0); // rouge
		}
		
	}
	</script>
</pre>
</div>

Décortiquons ce code pour comprendre ce qu'il fait. On réconnait la structure d'une conditionnel `if ... else` :
```
if (condition){
	// oui
}
else {
	// non
}
```
Le code dans le premier bloc sera éxecuté si la condition est vérifiée, et sinon c'est le code dans le second bloc qui sera éxecuté. 

Dans shadertoy, la variable `fragCoord` désigne les coordonnées $(x,y)$ du pixel dont on calcule la couleur, et `fragCoord.x` ou `fragCoord.y` désignent la valeur de $x$ ou $y$ respectivement. Ainsi, la condition `fragCoord.x < 100.0` teste donc si $x < 100$, auquel cas on affiche du bleu, et sinon on affiche du rouge (else).

### Exercice

Comment modifier le code pour colorer le haut de l'écran en bleu sur 100 pixels de haut, et le reste en rouge ?
	
## Références


- [GPU-Accelerated Mathematical Illustration](https://shaders.stevejtrettel.site), *[Steve Trettel](https://stevejtrettel.site)*
- [The Book of Shaders](https://thebookofshaders.com), *[Patricio Gonzalez Vivo](http://patriciogonzalezvivo.com) & [Jen Lowe](https://www.jenlowe.net)*
- [Shader](https://fr.wikipedia.org/wiki/Shader), Wikipédia


