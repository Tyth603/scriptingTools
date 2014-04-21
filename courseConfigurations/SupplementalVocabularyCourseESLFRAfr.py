__author__ = 'vagrant'
# -*- coding: utf-8 -*-

from CourseConfiguration import courseConfiguration

projectName = "supplementalVocabCoursesESLFRAfr"
languageDict = [
    ["x for French speakers", "English"],
]
unitNameList = [
u"Rendez-vous et Salutations",
u"Vous Faire Aider dans l'Apprentissage de la Langue",
u"Vous Faire Aider Davantage dans l'Apprentissage de la Langue",
u"Formules de Politesse",
u"Formes et Couleurs",
u"Vêtements",
u"Faire des Achats et Magasins",
u"Maisons et Appartements",
u"Pièces d'une Maison",
u"Famille",
u"Bureau et Professions",
u"Parties du Corps",
u"Urgences",
u"Endroits et Demander des Directions",
u"École",
u"Instruments de Musique",
u"Récréation",
u"Nature",
u"Animaux",
u"Nourriture 1",
u"Nourriture 2",
u"Aller au Restaurant",
u"Langues",
u"Pays",
u"Voyages",
u"Acheter des Billets",
u"Prendre un Taxi",
u"Séjourner à l'Hôtel",
u"Aller à la Banque",
u"Nombres",
u"Jours de la Semaine et L'Heure",
u"Saisons et La Météo",
u"Adjectifs et Adverbes",
u"Verbes",
u"Prépositions et Conjonctions"]
unitMap = {unitNameList[0]: ["Meeting-and-Greeting-1",
                                        "Meeting-and-Greeting-2"],
           unitNameList[1]: ["Communication-Facilitation-1",
                                                         "Communication-Facilitation-2",
                                                         "Communication-Facilitation-3",
                                                         "Communication-Facilitation-4",
                                                         "Communication-Facilitation-5",
                                                         "Communication-Facilitation-6",
                                                         "Communication-Facilitation-7"],
           unitNameList[2]: ["Helper-Relationship-Facilitation",
                                                             "Language-Learning-Facilitation-1",
                                                             "Language-Learning-Facilitation-2",
                                                             "Translation-Facilitation"],
           unitNameList[3]: ["Polite-Conversation-1",
                                      "Polite-Conversation-2",
                                      "Polite-Conversation-3",
                                      # "Useful-Expressions-1",
                                      # "Useful-Expressions-2"
           ],
           unitNameList[4]: ["Shapes",
                                                    "Colors"],
           unitNameList[5]: ["Clothing-1",
                       "Clothing-2",
                       "Clothing-3"],
           unitNameList[6]: ["Shopping-Stores",
                                         "Shopping-1",
                                         "Shopping-2",
                                         "Shopping-3",
                                         "Shopping-4",
                                         "Shopping-5"],
           unitNameList[7]: ["House-Apartment-1",
                                        "House-Apartment-2"],
           unitNameList[8]: ["Living-Room",
                                       "Dining-Room",
                                       "Kitchen",
                                       "Bathroom-1",
                                       "Bathroom-2",
                                       "Bedroom"],
           unitNameList[9]: ["Family-1",
                          "Family-2",
                          "Family-3",
                          "Family-4"],
           unitNameList[10]: ["Office-1",
                                            "Office-2",
                                            "Professions-1",
                                            "Professions-2"],
           unitNameList[11]: ["Parts-of-the-Body-1",
                                     "Parts-of-the-Body-2"],
           unitNameList[12]: ["Emergencies-1",
                           "Emergencies-2",
                           "Emergencies-3",
                           "Emergencies-4",
                           "Emergencies-5"],
           unitNameList[13]: ["Places-1",
                                                 "Places-2",
                                                 "Asking-for-Directions-1",
                                                 "Asking-for-Directions-2"],
           unitNameList[14]: ["School-1",
                          "School-2",
                          "School-3"],
           unitNameList[15]: ["Musical-Instruments-1",
                                          "Musical-Instruments-2"],
           unitNameList[16]: ["Recreation-1",
                            "Recreation-2",
                            "Recreation-3"],
           unitNameList[17]: ["Nature-1",
                             "Nature-2"],
           unitNameList[18]: ["Animals-1",
                            "Animals-2"],
           unitNameList[19]: ["Meals",
                           "Beverages",
                           "Fruit",
                           "Vegetables",
                           "Grains"],
           unitNameList[20]: ["Dairy",
                           "Meat",
                           "Seafood",
                           # "Spices-Condiments",
                           "Dessert"],
           unitNameList[21]: ["At-the-Restaurant-1",
                                   "At-the-Restaurant-2",
                                   "At-the-Restaurant-3",
                                   "At-the-Restaurant-4",
                                   "At-the-Restaurant-5"],
           unitNameList[22]: ["Languages-1",
                           "Languages-2",
                           "Languages-3",
                           "Languages-4"],
           unitNameList[23]: ["Continents",
                          "Countries-1",
                          "Countries-2",
                          "Countries-3"],
           unitNameList[24]: ["Travel-1",
                      "Travel-2",
                      "Travel-3",
                      "Travel-4",
                      "Travel-5"],
           unitNameList[25]: ["Buying-Tickets-1",
                                "Buying-Tickets-2",
                                "Buying-Tickets-3"],
           unitNameList[26]: ["Taking-a-Taxi-1",
                             "Taking-a-Taxi-2",
                             "Taking-a-Taxi-3"],
           unitNameList[27]: ["At-the-Hotel-1",
                                    "At-the-Hotel-2",
                                    "At-the-Hotel-3",
                                    "At-the-Hotel-4"],
           unitNameList[28]: ["Going-to-the-Bank-1",
                           "Going-to-the-Bank-2",
                           "Going-to-the-Bank-3",
                           "Going-to-the-Bank-4"],
           unitNameList[29]: ["Numbers-Cardinal-1",
                           "Numbers-Cardinal-2",
                           "Numbers-Cardinal-3",
                           "Numbers-Cardinal-4",
                           "Numbers-Ordinal",
                           "Numbers-Other"],
           unitNameList[30]: ["Days-of-the-Week-1",
                                     "Days-of-the-Week-2",
                                     "Time-1",
                                     "Time-2",
                                     "Asking-the-Time"],
           unitNameList[31]: ["Months",
                                          "Seasons",
                                          "Weather-1",
                                          "Weather-2"],
           # unitNameList[32]: ["Personal-Pronouns",
           #                                                  "Possessive-Adjectives",
           #                                                  "Conjunctions"],
           unitNameList[32]: ["Adjectives-1",
                                             "Adjectives-2",
                                             "Adjectives-3",
                                             "Adverbs"],
           unitNameList[33]: ["Verbs-1",
                          "Verbs-2",
                          "Verbs-3",
                          "Verbs-4",
                          "Verbs-5",
                          "Verbs-6",
                          "Verbs-7",
                          "Verbs-8"],
           unitNameList[34]: ["Prepositions-1",
                             "Prepositions-2",
                             "Prepositions-3",
                             "Prepositions-4"],
}
baseUnitObjectives = u"""

Cette unité va vous aider à …

- mémoriser les mots et les phrases se rapportant au sujet
- apprendre à lire et taper les mots et phrases
- reconnaître les sons et être capable de les prononcer correctement

Commencez par les activités telles que Comparaison de Langues et Exercice de Prononciation pour vous aider à vous familiariser avec les données.

Continuez avec les activités vocales de choix multiples et correspondances pour renforcer votre mémorisation des mots et des phrases.

Ensuite, faites les activités de dictée et de dactylographie pour pratiquer la production et l'écriture de la langue.

Enfin, faites les activités d'évaluation qui se trouvent à la fin de l'unité pour tester votre connaissance des mots et des phrases.
"""
unitObjectives = {
    unitNameList[0]: u"Cette unité enseigne des mots et phrases utiles concernant les rendez-vous et les salutations." + baseUnitObjectives,
    unitNameList[1]: u"Cette unité enseigne des mots et phrases utiles pour vous faire aider dans l'apprentissage de la langue."+ baseUnitObjectives,
    unitNameList[2]: u"Cette unité enseigne des mots et phrases utiles pour vous faire aider davantage dans l'apprentissage de la langue." + baseUnitObjectives,
    unitNameList[3]: u"Cette unité enseigne des mots et phrases utiles concernant les formules de politesse."+ baseUnitObjectives,
    unitNameList[4]: u"Cette unité enseigne des mots et phrases utiles concernant les formes et les couleurs." + baseUnitObjectives,
    unitNameList[5]: u"Cette unité enseigne des mots et phrases utiles concernant les vêtements." + baseUnitObjectives,
    unitNameList[6]: u"Cette unité enseigne des mots et phrases utiles concernant les achats et les magasins."+ baseUnitObjectives,
    unitNameList[7]: u"Cette unité enseigne des mots et phrases utiles concernant les maisons et les appartements." + baseUnitObjectives,
    unitNameList[8]: u"Cette unité enseigne des mots et phrases utiles concernant les pièces d'une maison." + baseUnitObjectives ,
    unitNameList[9]: u"Cette unité enseigne des mots et phrases utiles concernant la famille." + baseUnitObjectives,
    unitNameList[10]: u"Cette unité enseigne des mots et phrases utiles concernant le bureau et les professions." + baseUnitObjectives,
    unitNameList[11]: u"Cette unité enseigne des mots et phrases utiles concernant les parties du corps." + baseUnitObjectives,
    unitNameList[12]: u"Cette unité enseigne des mots et phrases utiles concernant les urgences." + baseUnitObjectives,
    unitNameList[13]: u"Cette unité enseigne des mots et phrases utiles concernant les endroits et pour demander des directions." + baseUnitObjectives,
    unitNameList[14]: u"Cette unité enseigne des mots et phrases utiles concernant l'école." + baseUnitObjectives,
    unitNameList[15]: u"Cette unité enseigne des mots et phrases utiles concernant les instruments de musique." + baseUnitObjectives,
    unitNameList[16]: u"Cette unité enseigne des mots et phrases utiles concernant la récréation." + baseUnitObjectives,
    unitNameList[17]: u"Cette unité enseigne des mots et phrases utiles concernant la nature." + baseUnitObjectives,
    unitNameList[18]: u"Cette unité enseigne des mots et phrases utiles concernant les animaux." + baseUnitObjectives,
    unitNameList[19]: u"Cette unité enseigne des mots et phrases utiles concernant la nourriture." + baseUnitObjectives,
    unitNameList[20]: u"Cette unité enseigne des mots et phrases utiles concernant la nourriture." + baseUnitObjectives,
    unitNameList[21]: u"Cette unité enseigne des mots et phrases utiles pour aller au restaurant." + baseUnitObjectives,
    unitNameList[22]: u"Cette unité enseigne des mots et phrases utiles concernant les langues." + baseUnitObjectives,
    unitNameList[23]: u"Cette unité enseigne des mots et phrases utiles concernant les pays." + baseUnitObjectives,
    unitNameList[24]: u"Cette unité enseigne des mots et phrases utiles concernant les voyages." + baseUnitObjectives,
    unitNameList[25]: u"Cette unité enseigne des mots et phrases utiles pour acheter des billets." + baseUnitObjectives,
    unitNameList[26]: u"Cette unité enseigne des mots et phrases utiles pour prendre un taxi." + baseUnitObjectives,
    unitNameList[27]: u"Cette unité enseigne des mots et phrases utiles pour séjourner à l'hôtel." + baseUnitObjectives,
    unitNameList[28]: u"Cette unité enseigne des mots et phrases utiles pour aller à la banque." + baseUnitObjectives,
    unitNameList[29]: u"Cette unité enseigne des mots et phrases utiles concernant les nombres." + baseUnitObjectives,
    unitNameList[30]: u"Cette unité enseigne des mots et phrases utiles concernant les jours de la semaine et l'heure." + baseUnitObjectives,
    unitNameList[31]: u"Cette unité enseigne des mots et phrases utiles concernant les saisons et la météo." + baseUnitObjectives,
    unitNameList[32]: u"Cette unité enseigne des mots et phrases utiles concernant les adjectifs et les adverbes." + baseUnitObjectives,
    unitNameList[33]: u"Cette unité enseigne des mots et phrases utiles concernant les verbes." + baseUnitObjectives,
    unitNameList[34]: u"Cette unité enseigne des mots et phrases utiles concernant les prépositions et les conjonctions." + baseUnitObjectives,
}

lessonOrder = unitMap
isESLTrue = True
lessonNameToListNameMap = {u"Meeting-and-Greeting-1":"Meeting-and-Greeting-1",
u"Meeting-and-Greeting-2":"Meeting-and-Greeting-2",
u"Communication-Facilitation-1":"Communication-Facilitation-1",
u"Communication-Facilitation-2":"Communication-Facilitation-2",
u"Communication-Facilitation-3":"Communication-Facilitation-3",
u"Communication-Facilitation-4":"Communication-Facilitation-4",
u"Communication-Facilitation-5":"Communication-Facilitation-5",
u"Communication-Facilitation-6":"Communication-Facilitation-6",
u"Communication-Facilitation-7":"Communication-Facilitation-7",
u"Helper-Relationship-Facilitation":"Helper-Relationship-Facilitation",
u"Language-Learning-Facilitation-1":"Language-Learning-Facilitation-1",
u"Language-Learning-Facilitation-2":"Language-Learning-Facilitation-2",
u"Translation-Facilitation":"Translation-Facilitation",
u"Polite-Conversation-1":"Polite-Conversation-1",
u"Polite-Conversation-2":"Polite-Conversation-2",
u"Polite-Conversation-3":"Polite-Conversation-3",
u"Useful-Expressions":"Useful-Expressions",
u"Shapes":"Shapes",
u"Colors":"Colors",
u"Clothing-1":"Clothing-1",
u"Clothing-2":"Clothing-2",
u"Clothing-3":"Clothing-3",
u"Shopping-Stores":"Shopping-Stores",
u"Shopping-1":"Shopping-1",
u"Shopping-2":"Shopping-2",
u"Shopping-3":"Shopping-3",
u"Shopping-4":"Shopping-4",
u"Shopping-5":"Shopping-5",
u"House-Apartment-1":"House-Apartment-1",
u"House-Apartment-2":"House-Apartment-2",
u"Living-Room":"Living-Room",
u"Dining-Room":"Dining-Room",
u"Kitchen":"Kitchen",
u"Bathroom-1":"Bathroom-1",
u"Bathroom-2":"Bathroom-2",
u"Bedroom":"Bedroom",
u"Family-1":"Family-1",
u"Family-2":"Family-2",
u"Family-3":"Family-3",
u"Family-4":"Family-4",
u"Office-1":"Office-1",
u"Office-2":"Office-2",
u"Professions-1":"Professions-1",
u"Professions-2":"Professions-2",
u"Parts-of-the-Body-1":"Parts-of-the-Body-1",
u"Parts-of-the-Body-2":"Parts-of-the-Body-2",
u"Emergencies-1":"Emergencies-1",
u"Emergencies-2":"Emergencies-2",
u"Emergencies-3":"Emergencies-3",
u"Emergencies-4":"Emergencies-4",
u"Emergencies-5":"Emergencies-5",
u"Places-1":"Places-1",
u"Places-2":"Places-2",
u"Asking-for-Directions-1":"Asking-for-Directions-1",
u"Asking-for-Directions-2":"Asking-for-Directions-2",
u"School-1":"School-1",
u"School-2":"School-2",
u"School-3":"School-3",
u"Musical-Instruments-1":"Musical-Instruments-1",
u"Musical-Instruments-2":"Musical-Instruments-2",
u"Recreation-1":"Recreation-1",
u"Recreation-2":"Recreation-2",
u"Recreation-3":"Recreation-3",
u"Nature-1":"Nature-1",
u"Nature-2":"Nature-2",
u"Animals-1":"Animals-1",
u"Animals-2":"Animals-2",
u"Meals":"Meals",
u"Beverages":"Beverages",
u"Fruit":"Fruit",
u"Vegetables":"Vegetables",
u"Grains":"Grains",
u"Dairy":"Dairy",
u"Meat":"Meat",
u"Seafood":"Seafood",
u"Dessert":"Dessert",
u"At-the-Restaurant-1":"At-the-Restaurant-1",
u"At-the-Restaurant-2":"At-the-Restaurant-2",
u"At-the-Restaurant-3":"At-the-Restaurant-3",
u"At-the-Restaurant-4":"At-the-Restaurant-4",
u"At-the-Restaurant-5":"At-the-Restaurant-5",
u"Languages-1":"Languages-1",
u"Languages-2":"Languages-2",
u"Languages-3":"Languages-3",
u"Languages-4":"Languages-4",
u"Continents":"Continents",
u"Countries-1":"Countries-1",
u"Countries-2":"Countries-2",
u"Countries-3":"Countries-3",
u"Travel-1":"Travel-1",
u"Travel-2":"Travel-2",
u"Travel-3":"Travel-3",
u"Travel-4":"Travel-4",
u"Travel-5":"Travel-5",
u"Buying-Tickets-1":"Buying-Tickets-1",
u"Buying-Tickets-2":"Buying-Tickets-2",
u"Buying-Tickets-3":"Buying-Tickets-3",
u"Taking-a-Taxi-1":"Taking-a-Taxi-1",
u"Taking-a-Taxi-2":"Taking-a-Taxi-2",
u"Taking-a-Taxi-3":"Taking-a-Taxi-3",
u"At-the-Hotel-1":"At-the-Hotel-1",
u"At-the-Hotel-2":"At-the-Hotel-2",
u"At-the-Hotel-3":"At-the-Hotel-3",
u"At-the-Hotel-4":"At-the-Hotel-4",
u"Going-to-the-Bank-1":"Going-to-the-Bank-1",
u"Going-to-the-Bank-2":"Going-to-the-Bank-2",
u"Going-to-the-Bank-3":"Going-to-the-Bank-3",
u"Going-to-the-Bank-4":"Going-to-the-Bank-4",
u"Numbers-Cardinal-1":"Numbers-Cardinal-1",
u"Numbers-Cardinal-2":"Numbers-Cardinal-2",
u"Numbers-Cardinal-3":"Numbers-Cardinal-3",
u"Numbers-Cardinal-4":"Numbers-Cardinal-4",
u"Numbers-Ordinal":"Numbers-Ordinal",
u"Numbers-Other":"Numbers-Other",
u"Days-of-the-Week-1":"Days-of-the-Week-1",
u"Days-of-the-Week-2":"Days-of-the-Week-2",
u"Time-1":"Time-1",
u"Time-2":"Time-2",
u"Asking-the-Time":"Asking-the-Time",
u"Months":"Months",
u"Seasons":"Seasons",
u"Weather-1":"Weather-1",
u"Weather-2":"Weather-2",
u"Adjectives-1":"Adjectives-1",
u"Adjectives-2":"Adjectives-2",
u"Adjectives-3":"Adjectives-3",
u"Adverbs":"Adverbs",
u"Verbs-1":"Verbs-1",
u"Verbs-2":"Verbs-2",
u"Verbs-3":"Verbs-3",
u"Verbs-4":"Verbs-4",
u"Verbs-5":"Verbs-5",
u"Verbs-6":"Verbs-6",
u"Verbs-7":"Verbs-7",
u"Verbs-8":"Verbs-8",
u"Prepositions-1":"Prepositions-1",
u"Prepositions-2":"Prepositions-2",
u"Prepositions-3":"Prepositions-3",
u"Prepositions-4":"Prepositions-4",
u"Conjunctions":"Conjunctions",
}
isTranslit = False

def createSVCConfiguration():
    """
    takes the above information and builds a course object for the rest of the scripts

    :return: a filled out course object
    """
    configObject = courseConfiguration()
    configObject.projectName = projectName
    configObject.unitNameList = unitNameList
    configObject.languageDict = languageDict
    configObject.unitMap = unitMap
    configObject.unitObjectives = unitObjectives
    configObject.lessonOrder = lessonOrder
    configObject.unitNumbers = configObject.createUnitNumbers(unitNameList)
    configObject.lessonToList = lessonNameToListNameMap
    configObject.isESLTrue = isESLTrue
    configObject.unitNumberToNames = configObject.createUnitNumberToNames(unitNameList)
    configObject.isTranslit = isTranslit

    return configObject