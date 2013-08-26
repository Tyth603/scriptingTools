import organizeB4Us
import convertB4Us
import createUnits
import createConfigYAML
import os, time, shutil
import translitCheck

proj2 = ["Possessive-Adjectives","Adjectives", "Adverbs", "Conjunctions", "Personal-Pronouns",  "Prepositions", "Verbs", "Beverages", "Dairy", "Dessert", "Fruit", "Grains", "Meals", "Meat", "Seafood", "Spices-Condiments", "Vegetables", "Bathroom", "Bedroom","Dining-Room", "House-Apartment", "Kitchen", "Living-Room", "Office", "Days-of-the-Week", "Months", "Numbers", "Seasons", "Time", "Animals", "Clothing", "Colors", "Countries", "Family", "Languages", "Musical-Instruments", "Nature", "Parts-of-the-Body", "Places", "Professions", "Recreation", "School", "Shapes", "Useful-Expressions"]

proj1 = ["Meeting-and-Greeting", "Polite-Conversation", "Travel", "Asking-for-Direction", "At-the-Hotel", "Asking-the-Time", "At-the-Restaurant", "Taking-a-Taxi", "Buying-Tickets", "Going-to-the-Bank", "Post-Office", "Shopping", "Emergencies", "Helper-Relationship", "Language-Learning-Facilitation", "Communication-Facilitation", "Translation-Facilitation", "Weather"]

#dir = project level directory
def runCreateYAML(dir):
    for language in os.listdir(dir):
        langDir = os.path.join(dir, language)
        for unit in os.listdir(langDir):
            unitDir = os.path.join(langDir, unit)
            if os.path.isdir(unitDir) == True:
                createConfigYAML.createYAML(unitDir)
            else:
                pass    

#dir = project level directory
def cleanUp(dir):
    for language in os.listdir(dir):
        langDir = os.path.join(dir, language)
        for unit in os.listdir(langDir):
            if unit != "not_enough_units":
                unitDir = os.path.join(langDir, unit)
                for B4X in os.listdir(unitDir):
                    b4xDir = os.path.join(unitDir, B4X)
                    if B4X == "B4X_OUTPUT":
                        os.rmdir(b4xDir)
                    elif unit.endswith(".b4u"):
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
                dst = os.path.join(dir,"not_enough_units", language)
                shutil.move(src, dst)

#dir = project level directory
def createRevision(dir):
    for lang in os.listdir(dir):
        langDir = os.path.join(dir, lang)
        if lang != "not_enough_units":
            fileName = "revision.txt"
            filePath = os.path.join(langDir, fileName)
            if os.path.exists(filePath):
                pass
            else:
                f = open(filePath, "w+")
                f.write("1")
                f.close
            

    

if __name__ == "__main__":
    organize = organizeB4Us.organizeB4U()
    translitCheck.translitCheck(organize.proj1Dir, organize)
    translitCheck.translitCheck(organize.proj2Dir, organize)
    createUnits.organizeB4Us(organize.proj1UnitNameList, organize.proj1Dir)
    createUnits.organizeB4Us(organize.proj2UnitNameList, organize.proj2Dir)
    checkNumberOfUnits(organize.proj1Dir, organize.proj1UnitNameList)
    checkNumberOfUnits(organize.proj2Dir, organize.proj2UnitNameList)
    convertB4Us.convert(organize.proj1Dir)
    convertB4Us.convert(organize.proj2Dir)
    createUnits.organizeB4Xs(organize.proj1UnitNameList, organize.proj1Dir)
    createUnits.organizeB4Xs(organize.proj2UnitNameList, organize.proj2Dir)
    time.sleep(5)
    cleanUp(organize.proj1Dir)
    cleanUp(organize.proj2Dir)
    runCreateYAML(organize.proj1Dir)
    runCreateYAML(organize.proj2Dir)
    createRevision(organize.proj1Dir)
    createRevision(organize.proj2Dir)
    
    
    #path = "C:\Users\Delelopment\Desktop\Efficienc-E\project2" 
    #createUnits.organizeB4Xs(proj2, path)    
    #checkNumberOfUnits("C:\Users\Delelopment\Desktop\Efficienc-E\project1", proj1)
    #checkNumberOfUnits("C:\Users\Delelopment\Desktop\Efficienc-E\project2", proj2)