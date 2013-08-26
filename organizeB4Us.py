import os, sys, re, shutil, convertB4Us, createUnits, createConfigYAML

class organizeB4U():
    def __init__(self):
        self.proj1UnitNameList = ["Meeting-and-Greeting", "Polite-Conversation", "Travel", "Asking-for-Direction", "At-the-Hotel", "Asking-the-Time", "At-the-Restaurant", "Taking-a-Taxi", "Buying-Tickets", "Going-to-the-Bank", "Post-Office", "Shopping", "Emergencies", "Helper-Relationship", "Language-Learning-Facilitation", "Communication-Facilitation", "Translation-Facilitation", "Weather"]
        self.proj2UnitNameList = ["Possessive-Adjectives", "Adjectives", "Adverbs", "Conjunctions", "Personal-Pronouns", "Prepositions", "Verbs", "Beverages", "Dairy", "Dessert", "Fruit", "Grains", "Meals", "Meat", "Seafood", "Spices-Condiments", "Vegetables", "Bathroom", "Bedroom","Dining-Room", "House-Apartment", "Kitchen", "Living-Room", "Office", "Days-of-the-Week", "Months", "Numbers", "Seasons", "Time", "Animals", "Clothing", "Colors", "Countries", "Family", "Languages", "Musical-Instruments", "Nature", "Parts-of-the-Body", "Places", "Professions", "Recreation", "School", "Shapes", "Useful-Expressions"]    
        self.pathName = os.path.abspath(os.path.dirname(sys.argv[0]))
        self.proj1Dir = os.path.join(self.pathName, "project1")
        self.proj2Dir = os.path.join(self.pathName, "project2")
        self.areaPrep(self.proj1Dir)
        self.areaPrep(self.proj2Dir)
        self.projLists = self.getProjLists()
        self.proj1List = []
        self.proj2List = []
        for file in self.projLists[0]:
            newLocation = self.moveLists(file, self.proj1Dir)
            self.proj1List.append(newLocation)
        for file in self.projLists[1]:
            newLocation = self.moveLists(file, self.proj2Dir)
            self.proj2List.append(newLocation)
    
    def areaPrep(self, fullPath):    
        if os.path.exists(fullPath):
            pass
        else:
            self.createDir(fullPath)
            print "Failed"    
    
    def createDir(self, fullPath):
        try:
            os.makedirs(fullPath)
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)    
        
    
    
    def getProjLists(self):
        proj1 = []
        proj2 = []
        for directory, dirnames, filenames in os.walk(self.pathName):      
            for file in filenames:
                if file.endswith(".b4u"):
                    if self.unitNameCheck(file, self.proj1UnitNameList) != None:
                        proj1.append(os.path.join(directory, file))
                    if self.unitNameCheck(file, self.proj2UnitNameList) != None:
                        proj2.append(os.path.join(directory, file))
        outList = [proj1, proj2]
        return outList    
    
    def unitNameCheck(self, fileName, unitList):
        for unitName in unitList:
            if unitName in fileName:
                return fileName
            else:
                pass
    
    def moveLists(self, file, projDir):
        langDir = os.path.join(projDir, os.path.split(os.path.split(file)[0])[1])
        finalDir = os.path.join(projDir,os.path.split(os.path.split(file)[0])[1], os.path.split(file)[1])
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
