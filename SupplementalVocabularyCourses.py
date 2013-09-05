__author__ = 'vagrant'

from CourseConfiguration import courseConfiguration

projectName = "supplementalVocabCoursesNonESL"

unitNameList = ["Meeting and Greeting", "Getting Help with your Language Learning",
                     "Getting More Help with your Language Learning", "Polite Conversation",
                     "Shapes and Colors", "Clothing", "Shopping and Stores", "Houses and Apartments",
                     "Rooms in a House", "Family", "Office and Professions", "Parts of the Body",
                     "Emergencies", "Places and Asking for Directions", "School", "Musical Instruments",
                     "Recreation", "Nature", "Animals", "Food 1", "Food 2", "Going to a Restaurant",
                     "Languages", "Countries", "Travel", "Buying Tickets", "Taking a Taxi",
                     "Staying at a Hotel", "Going to the Bank", "Numbers", "Days of the Week and Time",
                     "Seasons and Weather", "Personal Pronouns and", "Possessive Adjectives",
                     "Adjectives and Adverbs", "Verbs", "Prepositions"]

languageDict = [
    ["x for English speakers", "Spanish"],
    ["x for English speakers", "Chinese, Mandarin"],
    ["x for English speakers", "Japanese"],
    ["x for Chinese speakers", "English"],
    ["x for Spanish speakers", "English"],
    ["x for Indonesian Speakers", "English"],
]
unitMap = {"Meeting and Greeting": ["Meeting-and-Greeting"],
                "Getting Help with your Language Learning": ["Communication-Facilitation"],
                "Getting More Help with your Language Learning": ["Helper-Relationship",
                                                                  "Language-Learning-Facilitation",
                                                                  "Translation-Facilitation"],
                "Polite Conversation": ["Polite-Conversation", "Useful-Expressions"],
                "Shapes and Colors": ["Shapes", "Colors"],
                "Clothing": ["Clothing"],
                "Shopping and Stores": ["Shopping"],
                "Houses and Apartments": ["House-Apartment"],
                "Rooms in a House": ["Living-Room", "Dining-Room", "Kitchen", "Bathroom", "Bedroom"],
                "Family": ["Family"],
                "Office and Professions": ["Office", "Professions"],
                "Parts of the Body": ["Parts-of-the-Body"],
                "Emergencies": ["Emergencies"],
                "Places and Asking for Directions": ["Places", "Asking-for-Directions"],
                "School": ["School"],
                "Musical Instruments": ["Musical-Instruments"],
                "Recreation": ["Recreation"],
                "Nature": ["Nature"],
                "Animals": ["Animals"],
                "Food 1": ["Meals", "Beverages", "Fruit", "Vegetables", "Grains"],
                "Food 2": ["Dairy", "Meat", "Seafood", "Spices-Condiments", "Dessert"],
                "Going to a Restaurant": ["At-the-Restaurant"],
                "Languages": ["Languages"],
                "Countries": ["Continents", "Countries"],
                "Travel": ["Travel"],
                "Buying Tickets": ["Buying-Tickets"],
                "Taking a Taxi": ["Taking-a-Taxi"],
                "Staying at a Hotel": ["At-the-Hotel"],
                "Going to the Bank": ["Going-to-the-Bank"],
                "Numbers": ["Numbers-Cardinal", "Numbers-Ordinal", "Numbers-Other"],
                "Days of the Week and Time": ["Days-of-the-Week", "Time", "Asking-the-Time"],
                "Seasons and Weather": ["Months", "Seasons", "Weather"],
                "Personal Pronouns and Possessive Adjectives": ["Personal-Pronouns",
                                                                "Possessive-Adjectives", "Conjunctions"],
                "Adjectives and Adverbs": ["Adjectives", "Adverbs"],
                "Verbs": ["Verbs"],
                "Prepositions": ["Prepositions"],
}
unitObjectives = {
    "Meeting and Greeting":"""This unit teaches useful words and phrases related to meeting and greeting.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Getting Help with your Language Learning":"This unit teaches useful words and phrases related to getting help with your language learning.",
    "Getting More Help with your Language Learning":"This unit teaches useful words and phrases related to getting more help with your language learning.",
    "Polite Conversation":"This unit teaches useful words and phrases related to polite conversation.",
    "Shapes and Colors":"This unit teaches useful words and phrases related to shapes and colors.",
    "Clothing":"This unit teaches useful words and phrases related to clothing.",
    "Shopping and Stores":"This unit teaches useful words and phrases related to shopping and stores.",
    "Houses and Apartments":"This unit teaches useful words and phrases related to houses and apartments.",
    "Rooms in a House":"This unit teaches useful words and phrases related to rooms in a house.",
    "Family":"This unit teaches useful words and phrases related to family.",
    "Office and Professions":"This unit teaches useful words and phrases related to office and professions.",
    "Parts of the Body":"This unit teaches useful words and phrases related to parts of the body.",
    "Emergencies":"This unit teaches useful words and phrases related to emergencies.",
    "Places and Asking for Directions":"This unit teaches useful words and phrases related to places and asking for directions.",
    "School":"This unit teaches useful words and phrases related to school.",
    "Musical Instruments":"This unit teaches useful words and phrases related to musical instruments.",
    "Recreation":"This unit teaches useful words and phrases related to recreation.",
    "Nature":"This unit teaches useful words and phrases related to nature.",
    "Animals":"This unit teaches useful words and phrases related to animals.",
    "Food 1":"This unit teaches useful words and phrases related to food.",
    "Food 2":"This unit teaches useful words and phrases related to food.",
    "Going to a Restaurant":"This unit teaches useful words and phrases related to going to a restaurant.",
    "Languages":"This unit teaches useful words and phrases related to languages.",
    "Countries":"This unit teaches useful words and phrases related to countries.",
    "Travel":"This unit teaches useful words and phrases related to travel.",
    "Buying Tickets":"This unit teaches useful words and phrases related to buying tickets.",
    "Taking a Taxi":"This unit teaches useful words and phrases related to taking a taxi.",
    "Staying at a Hotel":"This unit teaches useful words and phrases related to staying at a hotel.",
    "Going to the Bank":"This unit teaches useful words and phrases related to going to the bank.",
    "Numbers":"This unit teaches useful words and phrases related to numbers.",
    "Days of the Week and Time":"This unit teaches useful words and phrases related to days of the week and time.",
    "Seasons and Weather":"This unit teaches useful words and phrases related to seasons and weather.",
    "Personal Pronouns and Possessive Adjectives":"This unit teaches useful words and phrases related to personal pronouns and possessive adjectives.",
    "Adjectives and Adverbs":"This unit teaches useful words and phrases related to adjectives and adverbs.",
    "Verbs":"This unit teaches useful words and phrases related to verbs.",
    "Prepositions":"This unit teaches useful words and phrases related to prepositions.",
    }

def createSVCConfiguration():
    configObject = courseConfiguration()
    configObject.projectName = projectName
    configObject.unitNameList = unitNameList
    configObject.languageDict = languageDict
    configObject.unitMap = unitMap
    configObject.unitObjectives = unitObjectives
    return configObject