import organizeB4Us
import convertB4Us
import createUnits
import createConfigYAML
import os
import time
import shutil
import translitCheck

proj2 = ["Possessive-Adjectives", "Adjectives", "Adverbs", "Conjunctions", "Personal-Pronouns", "Prepositions", "Verbs",
         "Beverages", "Dairy", "Dessert", "Fruit", "Grains", "Meals", "Meat", "Seafood", "Spices-Condiments",
         "Vegetables", "Bathroom", "Bedroom", "Dining-Room", "House-Apartment", "Kitchen", "Living-Room", "Office",
         "Days-of-the-Week", "Months", "Numbers", "Seasons", "Time", "Animals", "Clothing", "Colors", "Countries",
         "Family", "Languages", "Musical-Instruments", "Nature", "Parts-of-the-Body", "Places", "Professions",
         "Recreation", "School", "Shapes", "Useful-Expressions"]

proj1 = ["Meeting-and-Greeting", "Polite-Conversation", "Travel", "Asking-for-Direction", "At-the-Hotel",
         "Asking-the-Time", "At-the-Restaurant", "Taking-a-Taxi", "Buying-Tickets", "Going-to-the-Bank", "Post-Office",
         "Shopping", "Emergencies", "Helper-Relationship", "Language-Learning-Facilitation",
         "Communication-Facilitation", "Translation-Facilitation", "Weather"]

#dir = project level directory
def runCreateYAML(dir):
    for learnLanguage in os.listdir(dir):
        learnDir = os.path.join(dir, learnLanguage)
        for knownLanguage in os.listdir(learnDir):
            knownDir = os.path.join(langDir, knownLanguage)
            for unit in os.listdir(knownDir):
                unitDir = os.path.join(knownDir, unit)
                if os.path.isdir(unitDir) == True:
                    createConfigYAML.createYAML(unitDir)
                else:
                    pass

                #dir = project level directory


def cleanUp(dir):
    for language in os.listdir(dir):
        knownLangPath = os.path.join(dir, language)
        for learnLangDir in os.listdir(knownLangPath):
            print learnLangDir
            if learnLangDir == "revision.txt":
                pass
            else:
                learnLangPath = os.path.join(knownLangPath, learnLangDir)
                for unit in os.listdir(learnLangPath):
                    unitDir = os.path.join(learnLangPath, unit)
                    if unit == "revision.txt":
                        pass
                    else:
                        if unit == "config.yaml":
                            os.remove(unitDir)
                        else:
                            for B4X in os.listdir(unitDir):
                                print B4X
                                b4xDir = os.path.join(unitDir, B4X)
                                if B4X == "OUTPUT_B4Xs_1":
                                    os.rmdir(b4xDir)
                                elif unit.endswith(".b4u"):
                                    os.remove(b4xDir)
                                elif unit.endswith(".yaml"):
                                    os.remove(b4xDir)

#dir = project level directory
def checkNumberOfUnits(dir, projUnitNameList):
    nameList = projUnitNameList
    for language in os.listdir(dir):
        langDir = os.path.join(dir, language)
        if language != "not_enough_units":
            if len(nameList) == len(os.listdir(langDir)):
                pass
            else:
                src = langDir
                dst = os.path.join(dir, "not_enough_units", language)
                shutil.move(src, dst)

#dir = project level directory
def createRevision(dir):
    for lang in os.listdir(dir):
        langDir = os.path.join(dir, lang)
        for lang2 in os.listdir(langDir):
            if lang2 != "not_enough_units":
                lang2Dir = os.path.join(langDir, lang2)
                fileName = "revision.txt"
                filePath = os.path.join(lang2Dir, fileName)
                if os.path.exists(filePath):
                    pass
                else:
                    f = open(filePath, "w+")
                    f.write("1")
                    f.close()


def runUnitGenerator(paths):
    for knownLanguage in os.listdir(paths):
        knownDir = os.path.join(paths, knownLanguage)
        for learnLanguage in os.listdir(knownDir):
            learnDir = os.path.join(knownDir, learnLanguage)
            for unit in os.listdir(learnDir):
                unitDir = os.path.join(learnDir, unit)
                cmd = 'python "D:\working\\forChuck\\unit_generator.py" -p "%s"' % unitDir
                os.system(cmd)


if __name__ == "__main__":
    organize = organizeB4Us.organizeB4U()
    createUnits.tmpOrganize(organize.finalPathNames)
    runCreateYAML(organize.proj1Dir)
    runUnitGenerator(organize.finalPathNames)
    createRevision(organize.proj1Dir)
    cleanUp(organize.proj1Dir)