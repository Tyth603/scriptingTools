import os, sys, shutil


class organizeB4U():
    def __init__(self, unitNameList, languageDict, unitMap, projectName, unitObjectives, lessonOrder, unitNumbers, lessonMap, isESLTrue):
        self.unitNameList = unitNameList
        self.isESLTrue = isESLTrue
        self.lessonMap = lessonMap
        self.unitNumbers = unitNumbers
        self.lessonOrder = lessonOrder
        self.unitObjectives = unitObjectives
        self.languageDict = languageDict
        self.unitMap = unitMap
        self.pathNames = []
        self.pathName = os.path.abspath(os.path.dirname(sys.argv[0]))
        self.proj1Dir = os.path.join(self.pathName, projectName)
        self.areaPrep(self.proj1Dir)
        self.languageCheck()
        self.finalPathNames = []
        for path in self.pathNames:
            learnLang = os.path.basename(path)
            knownlang = os.path.basename(os.path.split(path)[0])
            newPath = os.path.join(self.proj1Dir, knownlang, learnLang)
            self.finalPathNames.append(newPath)
            if os.path.exists(newPath):
                self.getProjLists(path, newPath)
            else:
                if os.path.exists(os.path.split(newPath)[0]):
                    os.mkdir(newPath)
                    self.getProjLists(path, newPath)
                else:
                    os.mkdir(os.path.split(newPath)[0])
                    os.mkdir(newPath)
                    self.getProjLists(path, newPath)


    def areaPrep(self, fullPath):
        if os.path.exists(fullPath):
            pass
        else:
            self.createDir(fullPath)
            print "Failed"

    def languageCheck(self):
        for item in self.languageDict:
            languagePath = os.path.join(self.pathName, 'b4u', os.path.join(item[0], item[1]))
            if os.path.exists(languagePath):
                self.pathNames.append(languagePath)
            else:
                self.pathNames.append(languagePath)


    def createDir(self, fullPath):
        try:
            os.makedirs(fullPath)
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)


    def getProjLists(self, initialDir, finalDir):
        for directory, dirnames, filenames in os.walk(initialDir):
            for file in filenames:
                if file.endswith(".b4u"):
                    if self.unitNameMapCheck(file, self.unitMap) is not None:
                        unitName = self.unitNameMapCheck(file, self.unitMap)
                        finalPath = os.path.join(finalDir, unitName, file)
                        originalPath = os.path.join(directory, file)
                        if os.path.exists(os.path.split(finalPath)[0]):
                            shutil.copyfile(originalPath, finalPath)
                        else:
                            os.mkdir(os.path.split(finalPath)[0])
                            shutil.copyfile(originalPath, finalPath)

                            # if self.unitNameCheck(file, self.proj1UnitNameList) != None:
                            #     unitName = self.unitNameCheck(file, self.proj1UnitNameList)
                            #     finalPath = os.path.join(finalDir, unitName, file)
                            #     originalPath = os.path.join(directory, file)
                            #     if os.path.exists(os.path.split(finalPath)[0]):
                            #         shutil.copyfile(originalPath, finalPath)
                            #     else:
                            #         os.mkdir(os.path.split(finalPath)[0])
                            #         shutil.copyfile(originalPath, finalPath)

    def unitNameMapCheck(self, fileName, unitMap):
        for unitName in unitMap.keys():
            listNames = unitMap[unitName]
            for name in listNames:
                if name in fileName:
                    return "unit" + str(self.unitNumbers(unitName))

    def moveLists(self, file, projDir):
        langDir = os.path.join(projDir, os.path.split(os.path.split(file)[0])[1])
        finalDir = os.path.join(projDir, os.path.split(os.path.split(file)[0])[1], os.path.split(file)[1])
        if not os.path.exists(os.path.join(projDir, os.path.split(file)[1])):
            if os.path.exists(langDir):
                try:
                    if not file == finalDir:
                        shutil.copyfile(file, finalDir)
                except RuntimeError, e:
                    print e.errorno
                    print "Move List Error"
            else:
                self.createDir(langDir)
                try:
                    shutil.copyfile(file, finalDir)
                except:
                    print "Move List Error"
        return finalDir


if __name__ == "__main__":
    organizeB4U()
