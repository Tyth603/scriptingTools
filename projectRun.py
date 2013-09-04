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

unitNumbers = {"Meeting and Greeting": 1,
               "Getting Help with your Language Learning": 2,
               "Getting More Help with your Language Learning": 3,
               "Polite Conversation": 4,
               "Shapes and Colors": 5,
               "Clothing": 6,
               "Shopping and Stores": 7,
               "Houses and Apartments": 8,
               "Rooms in a House": 9,
               "Family": 10,
               "Office and Professions": 11,
               "Parts of the Body": 12,
               "Emergencies": 13,
               "Places and Asking for Directions": 14,
               "School": 15,
               "Musical Instruments": 16,
               "Recreation": 17,
               "Nature": 18,
               "Animals": 19,
               "Food 1": 20,
               "Food 2": 21,
               "Going to a Restaurant": 22,
               "Languages": 23,
               "Countries": 24,
               "Travel": 25,
               "Buying Tickets": 26,
               "Taking a Taxi": 27,
               "Staying at a Hotel": 28,
               "Going to the Bank": 29,
               "Numbers": 30,
               "Days of the Week and Time": 31,
               "Seasons and Weather": 32,
               "Personal Pronouns and Possessive Adjectives": 33,
               "Adjectives and Adverbs": 34,
               "Verbs": 35,
               "Prepositions": 36}
#dir = project level directory
def runCreateYAML(dir):
    for learnLanguage in os.listdir(dir):
        learnDir = os.path.join(dir, learnLanguage)
        for knownLanguage in os.listdir(learnDir):
            knownDir = os.path.join(learnDir, knownLanguage)
            for unit in os.listdir(knownDir):
                unitDir = os.path.join(knownDir, unit, "data")
                if os.path.isdir(unitDir) == True:
                    createConfigYAML.createYAML(unitDir)
                else:
                    pass

                    #dir = project level directory


def cleanUp(dir):
    for language in os.listdir(dir):
        knownLangPath = os.path.join(dir, language)
        for learnLangDir in os.listdir(knownLangPath):
            #print learnLangDir
            if learnLangDir == "revision.txt":
                pass
            else:
                learnLangPath = os.path.join(knownLangPath, learnLangDir)
                for unit in os.listdir(learnLangPath):
                    unitDir = os.path.join(learnLangPath, unit)
                    print unitNumbers[unit]
                    finalUnitDir = os.path.join(learnLangPath, "unit" + str(unitNumbers[unit]))
                    os.rename(unitDir, finalUnitDir)
                    if unit == "revision.txt":
                        pass
                    else:
                        if unit == "config.yaml":
                            os.remove(finalUnitDir)
                        else:
                            for B4X in os.listdir(finalUnitDir):
                                print B4X
                                b4xDir = os.path.join(finalUnitDir, B4X)
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
                cmd = 'python "D:\working\\forChuck\\unit_generator.py" -u -p "%s"' % unitDir
                os.system(cmd)


if __name__ == "__main__":
    organize = organizeB4Us.organizeB4U()
    createUnits.tmpOrganize(organize.finalPathNames)
    runCreateYAML(organize.proj1Dir)
    runUnitGenerator(organize.proj1Dir)
    createRevision(organize.proj1Dir)
    cleanUp(organize.proj1Dir)