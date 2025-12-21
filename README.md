# Analyse de fichier audio pour la construction de niveau de jeu

## Contexte
Dans le cadre d'un projet académique du module de projet Génie Logiciel. Nous sommes amené à développer un jeu dont les niveaux sont générés à partir de certaines charactéristiques extraites de fichiers audio de musique.

## Fonctionnalités
Le programme permet d'obtenir un fichier JSON qui contient :

- "key" : La tonalité
- "tempo" : le battement par minute
- "beat_times" : une liste des marquages temporels qui marquent un battement dans la musique


## Pré-requis

Veuillez vous assurer d'avoir installé Python 3.x et FFmpeg (lecture de fichier mp3)

## Installation

### Option 1 (recommandée) : Environnement virtuel
Je vous conseil d'utiliser un environnement virtuel afin de ne pas polluer votre système de toutes les dépendances.

#### Configuration de l'environnement

```bash
# Créer l'environnement virtuel
python -m venv .venv

# Activer l'environnement
# Sur Windows :
.venv\Scripts\activate
# Sur macOS/Linux :
source .venv/bin/activate

# Installation des dépendances :
pip install -r requirement.txt
```
### Option 2 : Installation directe

```bash
pip install librosa numpy
```

## Execution

```bash
python3 main.py
```
> Le resultat sera disponible dans le répertoire `resultat`