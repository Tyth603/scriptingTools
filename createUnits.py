import os, shutil

proj2 = ["Possessive-Adjectives","Adjectives", "Adverbs", "Conjunctions", "Personal-Pronouns",  "Prepositions", "Verbs", "Beverages", "Dairy", "Dessert", "Fruit", "Grains", "Meals", "Meat", "Seafood", "Spices-Condiments", "Vegetables", "Bathroom", "Bedroom","Dining-Room", "House-Apartment", "Kitchen", "Living-Room", "Office", "Days-of-the-Week", "Months", "Numbers", "Seasons", "Time", "Animals", "Clothing", "Colors", "Countries", "Family", "Languages", "Musical-Instruments", "Nature", "Parts-of-the-Body", "Places", "Professions", "Recreation", "School", "Shapes", "Useful-Expressions"]

proj1 = ["Meeting-and-Greeting", "Polite-Conversation", "Travel", "Asking-for-Direction", "At-the-Hotel", "Asking-the-Time", "At-the-Restaurant", "Taking-a-Taxi", "Buying-Tickets", "Going-to-the-Bank", "Post-Office", "Shopping", "Emergencies", "Helper-Relationship", "Language-Learning-Facilitation", "Communication-Facilitation", "Translation-Facilitation", "Weather"]



def organizeB4Xs(unitNames, dir):
    languages = os.listdir(dir)
    for lang in languages:
        if lang != "not_enough_units":
            for unit in unitNames:
                path = os.path.join(dir, lang, unit, "B4X_OUTPUT")
                try:
                    listOfB4XDirs = os.listdir(path)
                except WindowsError, e:
                    print e
                    if os.path.exists(path):
                        os.rmdir(path)
                if os.path.exists(path):
                    for b4x in listOfB4XDirs:
                        if unit in b4x:
                            unitDir = os.path.split(path)[0]
                            b4xLocation = os.path.join(path,b4x)
                            finalLocation = os.path.join(unitDir, b4x)
                            if os.path.exists(b4xLocation):
                                if os.path.exists(unitDir):
                                    shutil.move(b4xLocation, finalLocation)
                                else:
                                    os.mkdir(unitDir)
                                    shutil.move(b4xLocation, finalLocation)

#dir = project directory
def organizeB4Us(unitNames, dir, paths):
    for language in paths:
        langDir = os.path.join(dir, language)
        listOfB4Us = os.listdir(langDir)
        for unit in unitNames:
            for b4u in listOfB4Us:
                if unit in b4u:
                    unitDir = os.path.join(langDir, unit)
                    b4uPath = os.path.join(langDir, b4u)
                    finalPath = os.path.join(unitDir, b4u)
                    if os.path.exists(b4uPath):
                        if os.path.exists(unitDir):
                            shutil.move(b4uPath, finalPath)
                        else:
                            os.mkdir(unitDir)
                            shutil.move(b4uPath, finalPath)

if __name__=="__main__":
    proj1Dir = "C:\Users\Delelopment\Desktop\\Efficienc-E\project1"
    #proj2Dir = "C:\Users\Delelopment\Desktop\\Efficienc-E\project2"
    #organizeB4Xs(proj1, proj1Dir)
    #organizeB4Xs(proj2, proj2Dir)
    organizeB4Us(proj1, proj1Dir)