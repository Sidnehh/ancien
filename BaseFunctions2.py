#Version sidney de Basefunctions.py
import os

#Ressources de bases

presidentsNames = {"Chirac": "Jacques", "Giscard dEstaing": "Valérie", "Hollande": "François", "Macron": "Emmanuel",
                   "Mitterrand": "François", "Sarkozy": "Nicolas"}
punctuation = ['!', '"','#','$','%','&',"'",')','*','+',',','-','.','/']


########################################################################################################################
#Fonctions complémentaires (pas demandées dans la consigne)
########################################################################################################################

def CreateFolder(folder):  # Crée un dossier dans le répertoire actuel, ayant pour nom l'argument folder.
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)
    except OSError:
        print("Error creating directory : ", folder)

def getTextFilesName(folder, extension="txt"):  # Retourne une liste des noms des fichiers
    files_name = []                             # contenus dans un dossier folder.
    for filename in os.listdir(folder):
        if filename.endswith(extension):
            files_name.append(filename)
    return files_name

########################################################################################################################
#Fonctions de base
########################################################################################################################

def extractNames(folder, extension="txt"):            # Retourne une de tous les noms des présidents
    files_name = getTextFilesName(folder, extension)  # extraits depuis un fichier folder.
    presidents = []
    for i in range(len(files_name)):
        name = files_name[i]
        name = name[len("Nomination_"):-(len(extension)+1)]
        if '0' <= name[-1] <= '9':
            name = name[:-1]
        if name not in presidents:
            presidents.append(name)

    return presidents

def associateName(lastname):            # Associe un prénom à un nom de président.
    return presidentsNames[lastname]

def ShowNames(folder):                  # Affiche la liste des noms des présidents extraits
    print(extractNames(folder))         # des fichiers.

def createCleanedDirectory():                # Crée le dossier "cleaned" et renvoie
    cleanFolder = "./cleaned/"               # l'emplacement de ce dossier.
    CreateFolder(cleanFolder)
    return cleanFolder

def createCleanedFiles(files, basefolder):              # Crée le dossier "cleaned" et y place des copies
    cleanedfolder = createCleanedDirectory()            # des fichiers files, avec son contenu en minuscules.
    for file in files:
        basepath = "./"+basefolder+"/"+file
        with open(basepath, 'r') as base:
            lines = base.readlines()
            for line_id, line in enumerate(lines):
                lines[line_id] = line.lower()
        cleanedpath = "./"+cleanedfolder+"/"+file
        with open(cleanedpath, 'w+') as clean:
            for line in lines:
                clean.write(line)

def removePunctuation(cleanedfolder):                   #cette fonction ne marche pas, mais elle est censée
    cleaned_files = getTextFilesName(cleanedfolder)     #retirer la ponctuation de tous les fichiers d'un
    for file in cleaned_files:                          #dossier folder.
        cleanedpath = "./" + cleanedfolder + "/" + file
        with open(cleanedpath, "r") as clean:
            lines = clean.readlines()
            for line in lines:
                for symbol in punctuation:
                    line = "".join(line.split(symbol))
                    print(line)

#pas fini, j'en ai marre !

