__author__ = 'vagrant'
from CourseConfiguration import courseConfiguration


englishForIndonesianProjectName = "QS_ESL_Courses"
englishForIndonesianLessonOrder = {
    "Start Cepat Unit 1": [
        "Pelajaran 1",
        "Pelajaran 2",
        "Pelajaran 3"
    ],
    "Start Cepat Unit 2": [
        "Pelajaran 4",
        "Pelajaran 5",
        "Pelajaran 6"
    ],
    "Start Cepat Unit 3": [
        "Pelajaran 7",
        "Pelajaran 8",
        "Pelajaran 9",
        "Pelajaran 10"
    ]
}

englishForIndonesianUnitNameList = englishForIndonesianLessonOrder.keys()
languageDict = [
    ["x for Indonesian Speakers", "English"],
]
unitMapEnglishForIndonesian = {
    "Start Cepat Unit 1": [
        "01-Quick-Start",
        "02-Quick-Start",
        "03-Quick-Start",
    ],
    "Start Cepat Unit 2": [
        "04-Quick-Start",
        "05-Quick-Start",
        "06-Quick-Start",
    ],
    "Start Cepat Unit 3": [
        "07-Quick-Start",
        "08-Quick-Start",
        "09-Quick-Start",
        "10-Quick-Start",
    ]
}
baseText = """
Unit ini akan membantu Anda...

- mengingat kata-kata dan frasa-frasa yang terkait dengan topik ini
- belajar membaca dan menulis kata-kata dan frasa-frasa tersebut
- mengenal bunyi dan bisa mengucapkannya dengan benar

Mulailah dengan aktivitas seperti Language Comparison (Perbandingan Bahasa) dan Pronunciation Practice (Latihan Pengucapan) untuk membantu Anda menjadi terbiasa dengan materi ini.

Lanjutkan dengan aktivitas pilihan ganda dan menjodohkan yang berbasis wicara untuk meningkatkan pemahaman Anda atas kata-kata dan frasa-frasa yang diberikan.

Kemudian, lengkapi aktivitas menyimak dan mengetik untuk mempraktikkan produksi dan penulisan bahasa.

Akhirnya, lengkapi aktivitas penilaian pada akhir unit untuk menguji pengetahuan Anda atas kata-kata dan frasa-frasa yang diberikan."""

englishForIndonesianUnitObjectives = {"Start Cepat Unit 1": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan sapaan umum, frasa dasar yang sopan, tempat-tempat sekitar, dan menyewa kamar di hotel." + "\n" + baseText,
"Start Cepat Unit 2": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan berbelanja di toko atau pasar, memesan di restoran, hari-hari dalam seminggu, cuaca, dan waktu." + "\n" + baseText,
"Start Cepat Unit 3": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan keterampilan bahasa Inggris, memberikan arah ke suatu lokasi, dan meminta bantuan dalam situasi darurat." + "\n" + baseText,
}

unitNumbers = {"Start Cepat Unit 1": 1,
               "Start Cepat Unit 2": 2,
               "Start Cepat Unit 3": 3}

lessonNameToListNameMap = {
    "01-Quick-Start": "Pelajaran 1",
    "02-Quick-Start": "Pelajaran 2",
    "03-Quick-Start": "Pelajaran 3",
    "04-Quick-Start": "Pelajaran 4",
    "05-Quick-Start": "Pelajaran 5",
    "06-Quick-Start": "Pelajaran 6",
    "07-Quick-Start": "Pelajaran 7",
    "08-Quick-Start": "Pelajaran 8",
    "09-Quick-Start": "Pelajaran 9",
    "10-Quick-Start": "Pelajaran 10",
}
unitList = ["Start Cepat Unit 1", "Start Cepat Unit 2", "Start Cepat Unit 3"]

isESLTrue = True
isTranslit = False

#######################################################################################################################
englishForThaiProjectName = "QS_ESL_Courses"
englishForThaiLessonOrder = {
    "Quick Start Unit 1": [
        "Lesson 1",
        "Lesson 2",
        "Lesson 3"
    ],
    "Quick Start Unit 2": [
        "Lesson 4",
        "Lesson 5",
        "Lesson 6"
    ],
    "Quick Start Unit 3": [
        "Lesson 7",
        "Lesson 8",
        "Lesson 9",
        "Lesson 10"
    ]
}
englishForThaiUnitNameList = englishForThaiLessonOrder.keys()
languageDictEnglishForThai = [
    ["x for Thai Speakers", "English"],
]
unitMapEnglishForThai = {
    "Quick Start Unit 1": [
        "01-Quick-Start",
        "02-Quick-Start",
        "03-Quick-Start",
    ],
    "Quick Start Unit 2": [
        "04-Quick-Start",
        "05-Quick-Start",
        "06-Quick-Start",
    ],
    "Quick Start Unit 3": [
        "07-Quick-Start",
        "08-Quick-Start",
        "09-Quick-Start",
        "10-Quick-Start",
    ]
}


baseTextEnglishForThai = """
Unit ini akan membantu Anda...

- mengingat kata-kata dan frasa-frasa yang terkait dengan topik ini
- belajar membaca dan menulis kata-kata dan frasa-frasa tersebut
- mengenal bunyi dan bisa mengucapkannya dengan benar

Mulailah dengan aktivitas seperti Language Comparison (Perbandingan Bahasa) dan Pronunciation Practice (Latihan Pengucapan) untuk membantu Anda menjadi terbiasa dengan materi ini.

Lanjutkan dengan aktivitas pilihan ganda dan menjodohkan yang berbasis wicara untuk meningkatkan pemahaman Anda atas kata-kata dan frasa-frasa yang diberikan.

Kemudian, lengkapi aktivitas menyimak dan mengetik untuk mempraktikkan produksi dan penulisan bahasa.

Akhirnya, lengkapi aktivitas penilaian pada akhir unit untuk menguji pengetahuan Anda atas kata-kata dan frasa-frasa yang diberikan."""

englishForThaiUnitObjectives = {"Quick Start Unit 1": """This unit teaches useful words and phrases related to common greetings, basic polite phrases, places around town, and renting a room at a hotel.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven multiple choice and matching activities to reinforce your recall of the words and phrases.

Then, complete the dictation and typing activities to practice producing and writing the language.

Finally, complete the assessment activities  at the end of the unit to test your knowledge of the words and phrases..""",
"Quick Start Unit 2": """This unit teaches useful words and phrases related to shopping at a store or market, ordering at a restaurant, the days of the week, weather, and time.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven multiple choice and matching activities to reinforce your recall of the words and phrases.

Then, complete the dictation and typing activities to practice producing and writing the language.

Finally, complete the assessment activities  at the end of the unit to test your knowledge of the words and phrases.""",
"Quick Start Unit 3": """This unit teaches useful words and phrases related to related to English language skills, giving basic directions to a location, and asking for help in an emergency situation.

This unit will help you...

- memorize words and phrases related to the topic
- learn to read and type the words and phrases
- recognize the sounds and be able to pronounce them correctly

Begin with activities like Language Comparison and Pronunciation Practice to help you become familiar with the material.

Continue on to the speech-driven multiple choice and matching activities to reinforce your recall of the words and phrases.

Then, complete the dictation and typing activities to practice producing and writing the language.

Finally, complete the assessment activities  at the end of the unit to test your knowledge of the words and phrases.
"""}

unitNumbersEnglishForThai = {"Quick Start Unit 1": 1,
               "Quick Start Unit 2": 2,
               "Quick Start Unit 3": 3}

lessonNameToListNameMapEnglishForThai = {
    "01-Quick-Start": "Lesson 1",
    "02-Quick-Start": "Lesson 2",
    "03-Quick-Start": "Lesson 3",
    "04-Quick-Start": "Lesson 4",
    "05-Quick-Start": "Lesson 5",
    "06-Quick-Start": "Lesson 6",
    "07-Quick-Start": "Lesson 7",
    "08-Quick-Start": "Lesson 8",
    "09-Quick-Start": "Lesson 9",
    "10-Quick-Start": "Lesson 10",
}
unitListEnglishForThai = ["Quick Start Unit 1", "Quick Start Unit 2", "Quick Start Unit 3"]

isESLTrueEnglishForThai = True
isTranslitEnglishForThai = False

#######################################################################################################################

englishForSwahiliProjectName = "QS_ESL_Courses"
englishForSwahiliLessonOrder = {
    "Mwanzo Kasi Sura 1": [
        "Somo 1",
        "Somo 2",
        "Somo 3"
    ],
    "Mwanzo Kasi Sura 2": [
        "Somo 4",
        "Somo 5",
        "Somo 6"
    ],
    "Mwanzo Kasi Sura 3": [
        "Somo 7",
        "Somo 8",
        "Somo 9",
        "Somo 10"
    ]
}

englishForSwahiliUnitNameList = englishForSwahiliLessonOrder.keys()
languageDictForSwahili = [
    ["x for Swahili Speakers", "English"],
]
unitMapEnglishForSwahili = {
    "Mwanzo Kasi Sura 1": [
        "01-Quick-Start",
        "02-Quick-Start",
        "03-Quick-Start",
    ],
    "Mwanzo Kasi Sura 2": [
        "04-Quick-Start",
        "05-Quick-Start",
        "06-Quick-Start",
    ],
    "Mwanzo Kasi Sura 3": [
        "07-Quick-Start",
        "08-Quick-Start",
        "09-Quick-Start",
        "10-Quick-Start",
    ]
}
baseSwahiliText = u"""

Sura hii itakusaidia...

- kukariri maneno na misemo inayohusika na mada
- kujifunze kusoma  na kupiga chapa maneno na misemo
- kubaini sauti na kuweza kuzitamka kwa ufasaha

Anza na majaribio kama vile Language Comparison na Pronunciation Practice ili  upate ufahamu wa somo.

Endelea na  majaribio yanayolenga mazungumzo ya chaguzi nyingi  pamoja na majaribio husika ili kutilia mkazo uwezo wa kukumbuka maneno na misemo.

Kisa, kamilisha majaribio ya imla na kupiga chapa ili kufanya mazoezi ya kutumia lugha na kuiandika.

Mwisho, kamilisha majaribio yaliyoko mwisho wa sura  ili kupima ujuzi wako wa maneno na misemo.
"""

englishForSwahiliUnitObjectives = {"Mwanzo Kasi Sura 1": "Sura hii inafundisha maneno muhimu na misemo kuhusu maamkio ya kawaida, misemo ya kimsingi yenye heshima,  sehemu mbali mbali katika mji, na kuhifadhi chumba kwenye hoteli." + "\n" + baseSwahiliText,
"Mwanzo Kasi Sura 2": "Sura hii inafundisha maneno muhimu na misemo kuhusu kununua madukani au sokoni, kuagiza kwenye mkahawa, siku za wiki, hali ya hewa, na saa." + "\n" + baseSwahiliText,
"Mwanzo Kasi Sura 3": "Sura hii inafundisha maneno muhimu na misemo kuhusu ustadi wa lugha ya kiingereza, maelekezo ya kimsingi ya kwenda mahali fulani, na kuomba msaada katika hali ya dharura." + "\n" + baseSwahiliText,
}

swahiliUnitNumbers = {"Mwanzo Kasi Sura 1": 1,
               "Mwanzo Kasi Sura 2": 2,
               "Mwanzo Kasi Sura 3": 3}

swahiliLessonNameToListNameMap = {
    "01-Quick-Start": "Somo 1",
    "02-Quick-Start": "Somo 2",
    "03-Quick-Start": "Somo 3",
    "04-Quick-Start": "Somo 4",
    "05-Quick-Start": "Somo 5",
    "06-Quick-Start": "Somo 6",
    "07-Quick-Start": "Somo 7",
    "08-Quick-Start": "Somo 8",
    "09-Quick-Start": "Somo 9",
    "10-Quick-Start": "Somo 10",
}
swahiliUnitList = ["Mwanzo Kasi Sura 1", "Mwanzo Kasi Sura 2", "Mwanzo Kasi Sura 3"]

isESLTrueForESLSwahili = True
isTranslitForESLSwahili = False

def createConfiguration():
    configObject = courseConfiguration()
    configObject.projectName = englishForIndonesianProjectName
    configObject.unitNameList = englishForIndonesianUnitNameList
    configObject.languageDict = languageDict
    configObject.lessonOrder = unitMapEnglishForIndonesian #englishForIndonesianLessonOrder
    configObject.unitMap = unitMapEnglishForIndonesian
    configObject.unitObjectives = englishForIndonesianUnitObjectives
    configObject.unitNumbers = unitNumbers
    configObject.lessonToList = lessonNameToListNameMap
    configObject.isESLTrue = isESLTrue
    configObject.unitNumberToNames = configObject.createUnitNumberToNames(unitList)
    configObject.isTranslit = isTranslit
    return configObject

def createConfigurationForEnglishForThai():
    configObject = courseConfiguration()
    configObject.projectName = englishForThaiProjectName
    configObject.unitNameList = englishForThaiUnitNameList
    configObject.languageDict = languageDictEnglishForThai
    configObject.lessonOrder = unitMapEnglishForThai #englishForIndonesianLessonOrder
    configObject.unitMap = unitMapEnglishForThai
    configObject.unitObjectives = englishForThaiUnitObjectives
    configObject.unitNumbers = unitNumbersEnglishForThai
    configObject.lessonToList = lessonNameToListNameMapEnglishForThai
    configObject.isESLTrue = isESLTrueEnglishForThai
    configObject.unitNumberToNames = configObject.createUnitNumberToNames(unitListEnglishForThai)
    configObject.isTranslit = isTranslitEnglishForThai
    return configObject

def createConfigurationForEnglishForSwahili():
    configObject = courseConfiguration()
    configObject.projectName = englishForSwahiliProjectName
    configObject.unitNameList = englishForSwahiliUnitNameList
    configObject.languageDict = languageDictForSwahili
    configObject.lessonOrder = unitMapEnglishForSwahili
    configObject.unitMap = unitMapEnglishForSwahili
    configObject.unitObjectives = englishForSwahiliUnitObjectives
    configObject.unitNumbers = swahiliUnitNumbers
    configObject.lessonToList = swahiliLessonNameToListNameMap
    configObject.isESLTrue = isESLTrueForESLSwahili
    configObject.unitNumberToNames = configObject.createUnitNumberToNames(swahiliUnitList)
    configObject.isTranslit = isTranslitForESLSwahili
    return configObject


