'''
- Extraire les noms des présidents à partir des noms des fichiers texte fournis ;
- Associer à chaque président un prénom ;
- Afficher la liste des noms des présidents (attention aux doublons) ;
- Convertir les textes des 8 fichiers en minuscules et stocker les contenus dans de nouveaux fichiers. Les
nouveaux fichiers doivent être stockés dans un nouveau dossier appelé « cleaned ». Ce dossier doit se
situer dans le répertoire principal où se trouve le programme main.py et au même niveau que le répertoire
« speeches »
- Pour chaque fichier stocké dans le répertoire « cleaned », parcourir son texte et supprimer tout caractère
de ponctuation. Le résultat final doit donner un fichier avec des mots séparés par des espaces. Attention,
certains caractères comme l’apostrophe (‘) ou le tiret (-) nécessitent un traitement spécial pour ne pas
causer une concaténation de deux mots (exemple : « elle-même » devrait devenir « elle même » et non
pas « ellemême »). Les modifications réalisées à cette étape devraient être stockées dans les mêmes
fichiers du répertoire « cleaned ».
'''

from BaseFunctions2 import *

basefolder = "speeches"
cleanfolder = "cleaned"

presidents_surnames = extractNames(basefolder, "txt")
print(presidents_surnames)

presidents_names_lastname = []
for name in presidents_surnames:
    presidents_names_lastname.append((associateName(name), name))
print(presidents_names_lastname)

presidents_speeches = presidentsSpeeches(presidents_surnames, basefolder)
print(presidents_speeches, sep='\n')

files = getTextFilesName(basefolder)

createFolder(cleanfolder)
createCleanedFiles(files, basefolder)
removePunctuation(cleanfolder)





