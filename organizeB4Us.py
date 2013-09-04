import os, sys, re, shutil, convertB4Us, createUnits, createConfigYAML


class organizeB4U():
    def __init__(self, unitNameList, languageDict, unitMap):
        self.proj1UnitNameList = unitNameList
        # self.proj1UnitNameList = ["Meeting and Greeting", "Getting Help with your Language Learning",
        #                           "Getting More Help with your Language Learning", "Polite Conversation",
        #                           "Shapes and Colors", "Clothing", "Shopping and Stores", "Houses and Apartments",
        #                           "Rooms in a House", "Family", "Office and Professions", "Parts of the Body",
        #                           "Emergencies", "Places and Asking for Directions", "School", "Musical Instruments",
        #                           "Recreation", "Nature", "Animals", "Food 1", "Food 2", "Going to a Restaurant",
        #                           "Languages", "Countries", "Travel", "Buying Tickets", "Taking a Taxi",
        #                           "Staying at a Hotel", "Going to the Bank", "Numbers", "Days of the Week and Time",
        #                           "Seasons and Weather", "Personal Pronouns and", "Possessive Adjectives",
        #                           "Adjectives and Adverbs", "Verbs", "Prepositions"]
        self.languageDict = languageDict
        # self.languageDict = [
        #     ["x for English speakers", "Spanish"],
        #     ["x for English speakers", "Chinese, Mandarin"],
        #     ["x for English speakers", "Japanese"],
        #     ["x for Chinese speakers", "English"],
        #     ["x for Spanish speakers", "English"],
        #     ["x for Indonesian Speakers", "English"],
        # ]
        self.proj1UnitMap = unitMap
        # self.proj1UnitMap = {"Meeting and Greeting": ["Meeting-and-Greeting"],
        #                      "Getting Help with your Language Learning": ["Communication-Facilitation"],
        #                      "Getting More Help with your Language Learning": ["Helper-Relationship",
        #                                                                        "Language-Learning-Facilitation",
        #                                                                        "Translation-Facilitation"],
        #                      "Polite Conversation": ["Polite-Conversation", "Useful-Expressions"],
        #                      "Shapes and Colors": ["Shapes", "Colors"],
        #                      "Clothing": ["Clothing"],
        #                      "Shopping and Stores": ["Shopping"],
        #                      "Houses and Apartments": ["House-Apartment"],
        #                      "Rooms in a House": ["Living-Room", "Dining-Room", "Kitchen", "Bathroom", "Bedroom"],
        #                      "Family": ["Family"],
        #                      "Office and Professions": ["Office", "Professions"],
        #                      "Parts of the Body": ["Parts-of-the-Body"],
        #                      "Emergencies": ["Emergencies"],
        #                      "Places and Asking for Directions": ["Places", "Asking-for-Directions"],
        #                      "School": ["School"],
        #                      "Musical Instruments": ["Musical-Instruments"],
        #                      "Recreation": ["Recreation"],
        #                      "Nature": ["Nature"],
        #                      "Animals": ["Animals"],
        #                      "Food 1": ["Meals", "Beverages", "Fruit", "Vegetables", "Grains"],
        #                      "Food 2": ["Dairy", "Meat", "Seafood", "Spices-Condiments", "Dessert"],
        #                      "Going to a Restaurant": ["At-the-Restaurant"],
        #                      "Languages": ["Languages"],
        #                      "Countries": ["Continents", "Countries"],
        #                      "Travel": ["Travel"],
        #                      "Buying Tickets": ["Buying-Tickets"],
        #                      "Taking a Taxi": ["Taking-a-Taxi"],
        #                      "Staying at a Hotel": ["At-the-Hotel"],
        #                      "Going to the Bank": ["Going-to-the-Bank"],
        #                      "Numbers": ["Numbers-Cardinal", "Numbers-Ordinal", "Numbers-Other"],
        #                      "Days of the Week and Time": ["Days-of-the-Week", "Time", "Asking-the-Time"],
        #                      "Seasons and Weather": ["Months", "Seasons", "Weather"],
        #                      "Personal Pronouns and Possessive Adjectives": ["Personal-Pronouns",
        #                                                                      "Possessive-Adjectives", "Conjunctions"],
        #                      "Adjectives and Adverbs": ["Adjectives", "Adverbs"],
        #                      "Verbs": ["Verbs"],
        #                      "Prepositions": ["Prepositions"],
        # }
        self.pathNames = []
        self.pathName = os.path.abspath(os.path.dirname(sys.argv[0]))
        self.proj1Dir = os.path.join(self.pathName, "project1")
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
                    if self.unitNameMapCheck(file, self.proj1UnitMap) is not None:
                        unitName = self.unitNameMapCheck(file, self.proj1UnitMap)
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
                    return unitName

    def unitNameCheck(self, fileName, unitList):
        for unitName in unitList:
            if unitName in fileName:
                return unitName
            else:
                pass

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
