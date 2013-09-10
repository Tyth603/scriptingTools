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
                     "Seasons and Weather", "Personal Pronouns and Possessive Adjectives",
                     "Adjectives and Adverbs", "Verbs", "Prepositions"]

languageDict = [
    ["x for English speakers", "Spanish"],
    ["x for English speakers", "Chinese, Mandarin"],
    ["x for English speakers", "Japanese"],
    # ["x for Chinese speakers", "English"],
    # ["x for Spanish speakers", "English"],
    # ["x for Indonesian Speakers", "English"],
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
    "Getting Help with your Language Learning":"""This unit teaches useful words and phrases related to getting help with your language learning.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Getting More Help with your Language Learning":"""This unit teaches useful words and phrases related to getting more help with your language learning.""",
    "Polite Conversation":"""This unit teaches useful words and phrases related to polite conversation.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Shapes and Colors":"""This unit teaches useful words and phrases related to shapes and colors.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Clothing":"""This unit teaches useful words and phrases related to clothing.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Shopping and Stores":"""This unit teaches useful words and phrases related to shopping and stores.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Houses and Apartments":"""This unit teaches useful words and phrases related to houses and apartments.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Rooms in a House":"""This unit teaches useful words and phrases related to rooms in a house.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Family":"""This unit teaches useful words and phrases related to family.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Office and Professions":"""This unit teaches useful words and phrases related to office and professions.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Parts of the Body":"""This unit teaches useful words and phrases related to parts of the body.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Emergencies":"""This unit teaches useful words and phrases related to emergencies.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Places and Asking for Directions":"""This unit teaches useful words and phrases related to places and asking for directions.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "School":"""This unit teaches useful words and phrases related to school.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Musical Instruments":"""This unit teaches useful words and phrases related to musical instruments.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Recreation":"""This unit teaches useful words and phrases related to recreation.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Nature":"""This unit teaches useful words and phrases related to nature.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Animals":"""This unit teaches useful words and phrases related to animals.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Food 1":"""This unit teaches useful words and phrases related to food.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Food 2":"""This unit teaches useful words and phrases related to food.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Going to a Restaurant":"""This unit teaches useful words and phrases related to going to a restaurant.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Languages":"""This unit teaches useful words and phrases related to languages.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Countries":"""This unit teaches useful words and phrases related to countries.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Travel":"""This unit teaches useful words and phrases related to travel.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Buying Tickets":"""This unit teaches useful words and phrases related to buying tickets.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Taking a Taxi":"""This unit teaches useful words and phrases related to taking a taxi.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Staying at a Hotel":"""This unit teaches useful words and phrases related to staying at a hotel.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Going to the Bank":"""This unit teaches useful words and phrases related to going to the bank.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Numbers":"""This unit teaches useful words and phrases related to numbers.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Days of the Week and Time":"""This unit teaches useful words and phrases related to days of the week and time.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Seasons and Weather":"""This unit teaches useful words and phrases related to seasons and weather.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Personal Pronouns and Possessive Adjectives":"""This unit teaches useful words and phrases related to personal pronouns and possessive adjectives.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Adjectives and Adverbs":"""This unit teaches useful words and phrases related to adjectives and adverbs.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Verbs":"""This unit teaches useful words and phrases related to verbs.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    "Prepositions":"""This unit teaches useful words and phrases related to prepositions.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven Multiple Choice and Matching activities to reinforce your recall of the words and phrases.

Then, complete the Dictation and other typing activities to practice producing and writing the language.

Finally, complete the assessment activities at the end of the unit to test your knowledge of the words and phrases.""",
    }
lessonOrder = {"Meeting and Greeting": ["Meeting-and-Greeting-1",
                                        "Meeting-and-Greeting-2"],

             "Getting Help with your Language Learning": ["Communication-Facilitation-1",
                                                          "Communication-Facilitation-2",
                                                          "Communication-Facilitation-3",
                                                          "Communication-Facilitation-4",
                                                          "Communication-Facilitation-5",
                                                          "Communication-Facilitation-6",
                                                          "Communication-Facilitation-7",],

             "Getting More Help with your Language Learning": ["Helper-Relationship-Facilitation",
                                                               "Language-Learning-Facilitation-1",
                                                               "Language-Learning-Facilitation-2",
                                                               "Translation-Facilitation"],

             "Polite Conversation": ["Polite-Conversation-1",
                                     "Polite-Conversation-2",
                                     "Polite-Conversation-3",
                                     "Useful-Expressions"],

             "Shapes and Colors": ["Shapes",
                                   "Colors"],

             "Clothing": ["Clothing-1",
                          "Clothing-2",
                          "Clothing-3",],

             "Shopping and Stores": ["Shopping-Stores",
                                     "Shopping-1",
                                     "Shopping-2",
                                     "Shopping-3",
                                     "Shopping-4",
                                     "Shopping-5",],

             "Houses and Apartments": ["House-Apartment-1",
                                       "House-Apartment-2",
                                       ],

             "Rooms in a House": ["Living-Room",
                                  "Dining-Room",
                                  "Kitchen",
                                  "Bathroom-1",
                                  "Bathroom-2",
                                  "Bathroom-3",
                                  "Bedroom"],

             "Family": ["Family-1",
                        "Family-2",
                        "Family-3",
                        "Family-4",],

             "Office and Professions": ["Office-1",
                                        "Office-2",
                                        "Professions-1",
                                        "Professions-2"],

             "Parts of the Body": ["Parts-of-the-Body-1",
                                   "Parts-of-the-Body-2"],

             "Emergencies": ["Emergencies-1",
                             "Emergencies-2",
                             "Emergencies-3",
                             "Emergencies-4",
                             "Emergencies-5",],

             "Places and Asking for Directions": ["Places-1",
                                                  "Places-2",
                                                  "Asking-for-Directions-1",
                                                  "Asking-for-Directions-2"],

             "School": ["School-1",
                        "School-2",
                        "School-3",],

             "Musical Instruments": ["Musical-Instruments-1",
                                     "Musical-Instruments-2",],

             "Recreation": ["Recreation-1",
                            "Recreation-2",
                            "Recreation-3",],

             "Nature": ["Nature-1",
                        "Nature-2",],

             "Animals": ["Animals-1",
                         "Animals-2",],

             "Food 1": ["Meals",
                        "Beverages",
                        "Fruit",
                        "Vegetables",
                        "Grains"],

             "Food 2": ["Dairy",
                        "Meat",
                        "Seafood",
                        "Spices-Condiments",
                        "Dessert"],

             "Going to a Restaurant": ["At-the-Restaurant-1",
                                       "At-the-Restaurant-2",
                                       "At-the-Restaurant-3",
                                       "At-the-Restaurant-4",
                                       "At-the-Restaurant-5",],

             "Languages": ["Languages-1",
                           "Languages-2",
                           "Languages-3",
                           "Languages-4",],

             "Countries": ["Continents",
                           "Countries-1",
                           "Countries-2",
                           "Countries-3",],

             "Travel": ["Travel-1",
                        "Travel-2",
                        "Travel-3",
                        "Travel-4",
                        "Travel-5",],

             "Buying Tickets": ["Buying-Tickets-1",
                                "Buying-Tickets-2",
                                "Buying-Tickets-3"],

             "Taking a Taxi": ["Taking-a-Taxi-1",
                               "Taking-a-Taxi-2",
                               "Taking-a-Taxi-3",],

             "Staying at a Hotel": ["At-the-Hotel-1",
                                    "At-the-Hotel-2",
                                    "At-the-Hotel-3",
                                    "At-the-Hotel-4",],

             "Going to the Bank": ["Going-to-the-Bank-1",
                                   "Going-to-the-Bank-2",
                                   "Going-to-the-Bank-3",
                                   "Going-to-the-Bank-4",],

             "Numbers": ["Numbers-Cardinal-1",
                         "Numbers-Cardinal-2",
                         "Numbers-Cardinal-3",
                         "Numbers-Cardinal-4",
                         "Numbers-Ordinal",
                         "Numbers-Other"],

             "Days of the Week and Time": ["Days-of-the-Week-1",
                                           "Days-of-the-Week-2",
                                           "Time-1",
                                           "Time-2",
                                           "Asking-the-Time"],

             "Seasons and Weather": ["Months",
                                     "Seasons",
                                     "Weather-1",
                                     "Weather-2",],

             "Personal Pronouns and Possessive Adjectives": ["Personal-Pronouns",
                                                             "Possessive-Adjectives",
                                                             "Conjunctions"],

             "Adjectives and Adverbs": ["Adjectives-1",
                                        "Adjectives-2",
                                        "Adjectives-3",
                                        "Adverbs"],
             "Verbs": ["Verbs-1",
                       "Verbs-2",
                       "Verbs-3",
                       "Verbs-4",
                       "Verbs-5",
                       "Verbs-6",
                       "Verbs-7",
                       "Verbs-8",],

             "Prepositions": ["Prepositions-1",
                              "Prepositions-2",
                              "Prepositions-3",
                              "Prepositions-4",],
}

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
isESLTrue = False
lessonNameToListNameMap = ""


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
    configObject.unitNumbers = unitNumbers
    configObject.lessonToList = lessonNameToListNameMap
    configObject.isESLTrue = isESLTrue
    configObject.unitNumberToNames = configObject.createUnitNumberToNames(unitNameList)

    return configObject
createSVCConfiguration()