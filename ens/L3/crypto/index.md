---
layout: page
title: Cryptographie
permalink: /ens/L3/crypto/
hidden : True
---


# Cryptographie

L'objectif de l'UE est d'être une introduction à la cryptographie et la cryptanalyse par la pratique. Le principe est de progresser à travers une série de messages chiffrés de difficulté croissante. Leur déchiffrement nécessite la compréhension de l'algorithme de chiffrement, mais aussi de ses faiblesses, et la mise en pratique informatique d'une attaque exploitant celles-ci.

## Messages chiffrés

Voici les messages au format `txt`. Téléchargez directement le fichier et placez-le dans le répertoire où se trouve votre code (ne faites pas un copier-coller depuis le navigateur ou le bloc-note au risque de rencontrer des problème d'encodage!). Pour ouvrir un fichier en Python, on peut utiliser la syntaxe

{% highlight python %}
import os
# […]
with open('nom_du_fichier.txt', 'r') as file:
    # on fait des choses avec le fichier
    message = file.read() # chaîne de caractère avec le contenu du fichier
    # bla
# à partir d'ici, le fichier est fermé
{% endhighlight %}
Pour plus de renseignements sur l'utilisation des fichiers en Python, vous pouvez voir [ce cours](https://python.sdv.univ-paris-diderot.fr/07_fichiers/) de l'université Paris Diderot. 

* 📄 [Message 1](message1.txt)
* 📄 [Message 2](message2.txt)
* 📄 [Message 3](message3.txt)
* 📄 [Message 4](message4.txt)
* 📄 [Message 5](message5.txt)
* 📄 [Message 6](message6.txt)

## Documents utiles

Pour vous guider dans le déchiffrement des messages, vous pouvez suivre les activités proposées par les liens suivants :

* [Chaines de caractères](https://github.com/villebon-charpak/chaines)
* [Chiffre de Vigenère](https://github.com/villebon-charpak/vigenere)

Pour aller plus loin sur l'histoire de la cryptographie, voici quelques références :

- [Histoire de la cryptologie](https://fr.wikipedia.org/wiki/Histoire_de_la_cryptologie) sur Wikipédia
- **Histoire des codes secrets** *De l'Egypte des pharaons à l'ordinateur quantique*, Simon Singh 

## Évaluation

### Modalités d'évaluation


- **Rendu du code** via un repository GitHub (ou git équivalent). Seuls les commits effectués sur votre projet avant cette date seront pris en compte.

-   **Présentation de 15 minutes**, questions comprises. Les soutenance ont lieu le vendredi 24 avril 2020. Il est possible (souhaitable?) de s'aider d'un support visuel pour sa présentation.

-	**Déchiffrement d'un nouveau message** le jour de l'évaluation. Il faut donc vous assurer que votre code n'est pas trop spécifique à des messages particulier. Il s'agit ici d'évaluer à quel point vous vous êtes appropriés les concepts. 

### Critères d’évaluation

-	**Avancement :** jusqu'où vous êtes arrivés dans le déchiffrement des messages

-   **Lisibilité du code et réutilisabilité :** bonne organisation : séparation des tâches dans différents fichiers ou fonctions, noms de variables pertinents, commentaires, etc. Le code peut-il être facilement réutilisé pour déchiffrer d'autres messages ?

-	**Maitrise des concepts et contribution personnelle:** Evaluation des techniques de déchiffrement mises en oeuvre. Le code est-il personnel ? Présente-t-il des idées intéressante ou originales ?

-   **Investissement personnel :** Régularité des commits, travail en séances, assiduité et ponctualité. 

### Barême

Le barême sur 30 (ramené ensuite à 20) est le suivant :

- **Oral** *(6 points)* : 
    * support présentation *(2 points)*
	* qualité présentation *(2 points)*
	* questions *(2 points)*

- **Travail en scéances** *(3 points)* :
	* investissement personnel *(2 points)*
	* régularité des commits *(1 point)*

- **Rendu du code** *(15 points)* :
	* avancement *(6 points)*
	* contribution personnelle *(3 points)*
	* rendu à temps *(2 points)
	* lisibilité du code *(2 points)*
	* réutilisabilité du code *(2 points)*
	
- **Déchiffrement d'un nouveau message** *(4 points)*

- **Divers** *(2 points)* :
	* assiduité, ponctualité *(1 point)*
	* bonus appréciation générale *(1 point)*



