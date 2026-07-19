# BDB — tentative d'import depuis Sefaria

## Objectif

Importer le dictionnaire BDB (Brown-Driver-Briggs Hebrew Lexicon) depuis l'API de
[Sefaria](https://www.sefaria.org), en parcourant la chaîne de navigation prev/next
entre les entrées.

## Approche 1
Utilisation du fichier BDB.html qui est visiblement une export et conversion du fichier BDB qui était dans Bibleworks. Mais le fichier contient des problèmes de conversions unicode de l'hébreu (qui sont d'ailleurs toujours présent sur le bdb en ligne de sefaria)


## Approche 2

J'ai tenté de récupérer le dictionnaire directement en interrogeant l'API Sefaria entrée par entrée en suivant les liens de navigation. Pour chaque entrée, le code extrait le headword hébreu,
la translitération et la définition HTML.

## Pourquoi c'est abandonné

Deux problèmes bloquants :

1. **Chaîne de navigation cassée** : dans la section ע, les liens prev/next de Sefaria
   sont brisés, rendant impossible la traversée complète du dictionnaire.
2. Les données de Sefaria sont mal encodée, il y a des fautes dans l'hébreu... donc trop de travail pour un résultat non valable


## État des fichiers

| Fichier | Description |
|---|---|
| `bdb_mongo_sefaria.ipynb` | Notebook conversion du bdb.html de sefaria ou de scraping Sefaria  |
| `bdb_mongodb.py` | Script Python équivalent |
| `BDB.json` | 11 772 entrées parsées depuis le HTML source (complet) |
| `bdb_complete.json` | 9 359 entrées récupérées depuis Sefaria (incomplet) |
| `BDB_dict.html` / `BDB_intro.html` / `BDB_original.html` | Fichiers HTML source |

## Suite

L'import a été repris depuis le fichier `bdb.csv` (10 022 entrées, format
TSV), traité dans `data/bdb_to_json.ipynb`. C'est cette source qui sert de
base pour le JSON final utilisé par l'API.
