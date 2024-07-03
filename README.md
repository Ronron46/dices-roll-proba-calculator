# dices-roll-proba-calculator

Ce programme permet de calculer les différents résultats d'un lancé de dés ainsi que leur probabilités.

Actuellement, l'utilisateur peut utiliser des dés avec n'importe quel nombre de face ainsi que générer des dés avec un "avantage" ou un "désavantage" selon les règles de D&D.
(pour un dé avec avantage, deux dés sont jeté, seulement le meilleur résultat est gardé, pour un désavantage, le pire des deux est gardé).

Ce programme a pour objectif d'être très performant. Ainsi, même si les fonctionnalités de jets sont assez limité pour le moment, il est possible de calculer le résultat de 100d100 (10^200 combinaisons) en environ 9 secondes.

ce programme a été réalisé pour etre au final hébergé sur un serveur, pour cela il a été réalisé avec le framework Django.
L'affichage graphique utilise chart.js.

Pour l'utiliser, ce programme nécessite l'installation de Django

# Installation

ce programme nécessite python3 ainsi que l'utilitaire pip (normalement de base avec python3)

afin d'installer les conposantes nécessaire au fonctionnement du programme, une fois dans le dossier où a été téléchargé ou cloné ce repo, il convient de commencer par lancer un environnement virtuel python avev venv, pour cela il effectuer la commande suivante pour creer l'environnement : 

```sh
python -m venv env
```
pour lancer l'environnement virtuel, faite la commande suivante:

sous linux :

```sh
source env/bin/activate
```

sous windows :

```sh
.\env\script\activate.bat
```

une fois l'environnement lancé, effectuer l'installation de toutes les composantes avec la commande suivante :

```sh
pip install -r requirement.txt
```

une fois cela fait, rendez vous dans le dossier Dice avec la commande 

```sh
cd Dice
```

puis lancez le serveur en entrant la commande 

```sh
python manage.py runserver
```

une fois le serveur lancé, il suffit de rejoindre l'url suivante pour utiliser le programme :

[[127.0.0.1:8000/dice-calculator](http://127.0.0.1:8000/dice-calculator/)]