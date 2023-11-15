#Version sidney de Basefunctions.py
import os

#Ressources de bases

presidentsNames = {"Chirac": "Jacques", "Giscard dEstaing": "Valérie", "Hollande": "François", "Macron": "Emmanuel",
                   "Mitterrand": "François", "Sarkozy": "Nicolas"}
punctuation_to_space = ['!', '"','#','$','%','&',"'",')','*','+',',','-','.','/']
punctuation_to_delete = []


########################################################################################################################
#FONCTIONS COMPLEMENTAIRES (pas demandées dans la consigne)
########################################################################################################################

def createFolder(folder):  # Crée un dossier dans le répertoire actuel, ayant pour nom l'argument folder.
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

def presidentsSpeeches(presidents, folder):                    # Retourne un dictionnaire associant chaque président à
    president_speeches = {}                                    # son ou ses fichiers de discours.
    for president in presidents:
        for file in getTextFilesName(folder):
            if president in file:
                if(president in president_speeches.keys()):
                    president_speeches[president].append(file)
                else:
                    president_speeches[president] = [file]

    return president_speeches

########################################################################################################################
#FONCTIONS DE BASE
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

def showNames(folder):                  # Affiche la liste des noms des présidents extraits
    print(extractNames(folder))         # des fichiers.

def createCleanedDirectory():                # Crée le dossier "cleaned" et renvoie
    cleanFolder = "./cleaned/"               # l'emplacement de ce dossier.
    createFolder(cleanFolder)
    return cleanFolder

def createCleanedFiles(files, basefolder):              # Crée le dossier "cleaned" et y place des copies
    cleanedfolder = createCleanedDirectory()            # des fichiers files, avec son contenu en minuscules.
    for file in files:
        basepath = basefolder+"/"+file
        with open(basepath, 'r') as base:
            lines = base.readlines()
            for line in range(len(lines)):
                lines[line] = list(lines[line])
                for character in range(len(lines[line])):
                    if 'A'<=lines[line][character]<='Z':
                        lines[line][character] = chr(ord(lines[line][character])-(ord('A')-ord('a')))
                lines[line] = ''.join(lines[line])


            cleanedpath = "" + cleanedfolder + "/"+file
            with open(cleanedpath, 'w+') as clean:
                for line in lines:
                    clean.write(line)

def removePunctuation(cleanedfolder):                   #cette fonction ne marche pas, mais elle est censée
    cleaned_files = getTextFilesName(cleanedfolder)     #retirer la ponctuation de tous les fichiers d'un
    for file in cleaned_files:                          #dossier folder.
        cleanedpath = cleanedfolder + "/" + file
        with open(cleanedpath, "r") as clean:
            lines = clean.readlines()
            for line in range(len(lines)):
                for symbol in punctuation_to_space:
                    lines[line] = " ".join(lines[line].split(symbol))
            with open(cleanedpath, "w") as clean:
                clean.writelines(lines)

#pas fini, j'en ai marre !

