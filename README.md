## tomo

- [Objectif](#objectif)
- [Description](#description)
- [Prérequis](#prérequis)    
  - [Windows](#windows)    
  - [Linux](#linux)        
    - [Famille Debian](#famille-debian)        
    - [Famille RedHat](#famille-redhat)
- [Lancer le jeu](#lancer-le-jeu)    
  - [Windows](#windows-1)    
  - [Linux](#linux-1)

## Objectif

L’objectif de ce projet est de développer un jeu graphique 2D de type [Tamagotchi](https://fr.wikipedia.org/wiki/Tamagotchi) en langage Python de manière interactive en direct sur Twitch avec la communauté du streamer [Jachampagne](https://www.twitch.tv/jachampagne). 

## Description

L’utilisateur peut créer un petit animal et interagir avec ce dernier pour le faire vivre le plus longtemps possible.

## Prérequis

Pour tester le jeu, vous devez au préalable installer l'interpréteur python sous sa version 3.

### Windows

Ouvrez une fenêtre de votre navigateur et télécharger et exécuter le [dernièr exécutable python](https://www.python.org/downloads/).

### Linux

#### Famille Debian

Mettez à jour la liste de vos dépôts et télécharger ensuite le paquet python :

```shell
apt update -y
apt install -y python3
```

#### Famille RedHat

Mettez à jour la liste de vos dépôts et téléchargez ensuite le paquet `python3` :

```shell
yum update -y
yum install -y python3
```

## Lancer le jeu

### Windows

Ouvrez votre console powershell ou cmd, placez-vous à la racine du projet et tapez ensuite la commande suivante :

```
python main.py
```

### Linux

Ouvrez votre terminal, placez-vous à la racine du projet et tapez ensuite la commande suivante :

```
python3 main.py
```
