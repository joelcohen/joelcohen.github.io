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
* 📄 [Message 7](message7.txt)
* 📄 [Message 8](message8.txt)

Pour le message 8 :

```[35, 168, 224, 13, 127, 135, 26, 229, 2, 175, 104, 246, 221, 195, 149, 69, 38, 123, 10, 171, 31, 65, 114, 178, 105, 42, 37, 165, 191, 190, 172, 66, 154, 90, 86, 228, 156, 66, 125, 15, 54, 10, 139, 95, 125, 200, 165, 197, 152, 168, 115, 225, 186, 7, 164, 10, 4, 139, 98, 250, 231, 130, 118, 190, 219, 171, 162, 50, 157, 7, 178, 23, 128, 120, 114, 152, 171, 56, 235, 121, 53, 172, 119, 207, 128, 45, 232, 87, 189, 191, 68, 174, 250, 72, 137, 78, 215, 139, 89, 135, 98, 254, 238, 10, 12, 10, 45, 232, 88, 96, 255, 68, 97, 99, 3, 216, 51, 69, 169, 172, 62, 58, 29, 8, 177, 27, 5, 166, 50, 251, 200, 36, 117, 22, 198, 196, 251, 41, 227, 109, 77, 12, 86, 117, 42, 192, 208, 195, 228, 198, 141, 64, 121, 33, 59, 0, 91, 188, 133, 161, 70, 20, 118, 120, 10, 158, 104, 78, 123, 120, 236, 85, 112, 109, 62, 196, 174, 132, 101, 216, 42, 228, 145, 182, 160, 198, 34, 151, 152, 105, 179, 14, 3, 189, 80, 54, 229, 78, 167, 127, 31, 222, 21, 184, 49, 54, 89, 72, 149, 254, 229, 159, 191, 29, 46, 79, 66, 5, 22, 133, 45, 136, 61, 32, 182, 61, 170, 137, 52, 103, 194, 109, 18, 251, 38, 143, 111, 22, 90, 227, 131, 187, 71, 97, 83, 1, 176, 148, 242, 238, 56, 192, 54, 171, 8, 24, 16, 226, 46, 105, 127, 215, 169, 22, 183, 28, 139, 201, 250, 231, 10, 240, 181, 219, 172, 230, 177, 163, 153, 131, 132, 74, 158, 202, 191, 12, 148, 38, 39, 53, 103, 120, 141, 137, 162, 27, 141, 218, 110, 153, 104, 213, 169, 248, 228, 241, 240, 183, 179, 95, 25, 191, 165, 101, 192, 99, 165, 176, 214, 135, 160, 11, 225, 22, 246, 107, 90, 188, 149, 118, 8, 25, 127, 180, 254, 131, 77, 79, 133, 159, 194, 236, 112, 219, 138, 129, 4, 6, 9, 180, 144, 226, 192, 178, 69, 213, 150, 170, 25, 17, 95, 135, 57, 90, 130, 199, 173, 250, 111, 6, 159, 84, 196, 106, 239, 181, 28, 12, 220, 137, 197, 91, 203, 166, 99, 36, 146, 243, 31, 56, 173, 2, 92, 100, 209, 82, 205, 154, 54, 77, 177, 138, 108, 177, 101, 117, 226, 20, 246, 3, 251, 64, 160, 29, 90, 133, 46, 51, 126, 136, 193, 161, 102, 215, 67, 236, 217, 62, 176, 14, 123, 124, 91, 156, 93, 223, 181, 254, 226, 246, 1, 116, 74, 244, 100, 254, 190, 46, 156, 82, 59, 105, 187, 95, 101, 95, 109, 194, 59, 33, 182, 222, 197, 33, 91, 64, 108, 199, 225, 37, 152, 69, 130, 16, 186, 61, 169, 40, 192, 60, 189, 12, 34, 214, 96, 134, 88, 178, 125, 247, 57, 28, 76, 164, 234, 168, 143, 161, 62, 238, 248, 103, 200, 234, 113, 42, 164, 3, 222, 127, 107, 41, 77, 71, 209, 45, 137, 206, 102, 31, 95, 138, 253, 187, 140, 67, 239, 198, 143, 148, 185, 88, 188, 35, 241, 253, 230, 114, 21, 61, 171, 64, 147, 184, 217, 47, 114, 48, 97, 164, 225, 215, 36, 132, 157, 115, 34, 182, 208, 54, 110, 91, 175, 77, 236, 237, 202, 206, 249, 241, 194, 110, 189, 176, 190, 98, 238, 36, 127, 251, 214, 40, 73, 110, 225, 76, 215, 72, 24, 26, 147, 69, 222, 80, 144, 7, 63, 161, 9, 160, 12, 191, 165, 216, 91, 87, 58, 94, 13, 129, 189, 213, 217, 229, 246, 250, 243, 110, 217, 251, 125, 32, 238, 97, 138, 22, 168, 18, 206, 24, 160, 46, 137, 156, 139, 241, 128, 99, 188, 210, 18, 0, 13, 232, 152, 202, 251, 43, 7, 166, 74, 4, 151, 255, 49, 109, 155, 244, 154, 98, 231, 210, 61, 252, 232, 224, 246, 88, 205, 98, 187, 131, 175, 171, 144, 128, 190, 188, 196, 103, 187, 3, 230, 67, 46, 189, 130, 1, 54, 161, 84, 123, 159, 30, 143, 185, 166, 81, 33, 43, 0, 249, 228, 9, 25, 237, 142, 141, 141, 241, 17, 138, 228, 251, 64, 83, 82, 129, 1, 209, 222, 94, 15, 229, 163, 18, 70, 73, 165, 39, 244, 196, 247, 40, 73, 91, 220, 177, 224, 58, 43, 160, 174, 214, 39, 180, 77, 135, 33, 63, 206, 210, 45, 91, 38, 51, 72, 154, 122, 117, 210, 180, 56, 67, 233, 109, 141, 54, 194, 99, 206, 77, 70, 51, 1, 129, 211, 28, 249, 57, 155, 241, 49, 234, 211, 212, 159, 245, 66, 161, 176, 220, 89, 180, 130, 189, 102, 183, 21, 250, 55, 52, 113, 141, 22, 98, 97, 248, 74, 87, 225, 235, 84]```

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



