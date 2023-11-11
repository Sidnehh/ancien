import os

presidentsNames = {"Chirac": "Jacques", "Giscard dEstaing": "Valérie", "Hollande": "François", "Macron": "Emmanuel",
                   "Mitterrand": "François", "Sarkozy": "Nicolas"}


def CreateFolder(folder):  # crée un folder
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)
    except OSError:
        print("Error creating directory : ", folder)


def getTextFilesName(folder, extension="txt"):  # extrait les noms des fichiers textes contenus dans folder
    files_name = []
    for filename in os.listdir(folder):
        if filename.endswith(extension):
            files_name.append(filename)
    return files_name


def extractNames(folder):  # fait un peu le café, extrait les noms des présidents, et compte combien de fois ils apparaissent
    extension = "txt"
    files_name = getTextFilesName(folder, extension)
    presidents = {}
    for i in range(len(files_name)):
        name = files_name[i]
        name = name[len("Nomination_"):-len(extension)]
        if '0' <= name[-1] <= '9':
            name = name[:-1]

        if name in presidents.keys():
            presidents[name]["count"] += 1
        else:
            presidents[name] = {"name": presidentsNames[name], "count": 1}
    print(presidentsNames)


def createCleanedDirectory(files_names):
    cleanFolder = "./cleaned/"
    CreateFolder(cleanFolder)
    for file_name in files_names:
        with open(cleanFolder + file_name, 'w') as f:
            f.write("")
        with open(cleanFolder + file_name, 'a') as f:


def createCleanedFiles(files, basefolder, cleanedfolder):
    for file in files:
        with open(basefolder + file, 'r') as base:
            lines = base.readlines()
            for line_id, line in enumerate(lines):
                lines[line_id] = lower(line)
            punctuation = ['!', '"','#','$','%','&',"'",')','*','+',',','-','.','/',' ']
                for char in line:
                    if char in punctuation:
                        if char == "'" or char=='-':




            with open(cleanedfolder + file, 'w') as clean:
                clean.write("")


            with open(cleanedfolder + file, 'a') as clean:
                clean.write("")
