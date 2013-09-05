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

def createSVCConfiguration():
    configObject = courseConfiguration()
    configObject.projectName = projectName
    configObject.unitNameList = unitNameList
    configObject.languageDict = languageDict
    configObject.unitMap = unitMap
    return configObject