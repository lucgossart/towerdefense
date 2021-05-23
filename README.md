# towerdefense

## Installation

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`    
`brew install git`     
`git clone https://github.com/lucgossart/towerdefense`    
`cd towerdefense`     
`brew install python`     
`pip install pygame`

## Jouer

`python main.py`

## Touches par défaut

- 'j' : curseur vers le bas
- 'k' : curseur vers le haut
- 'l' : curseur vers la droite
- 'h' : curseur vers la gauche

- 'q' : tour pourpre (standard) sur le curseur
- 's' : tour orange (splash) sur le curseur
- 'd' : tour bleue sur le curseur

- 'Entrée' : poser la tour
- 'TAB'    : sélectionner une tour
- 'u'      : améliorer la tour sélectionnée

## Configurer

Configuration :
1. des vagues dans `waves_config.py`,
2. des tours dans tower_config.py,
3. d'autres trucs dans constants.py.

## Télécharger la dernière version
`git add -u`  
`git commit -m "message non vide quelqconque"`  
`git pull`
