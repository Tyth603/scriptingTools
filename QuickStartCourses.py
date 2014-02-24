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

englishForThaiUnitObjectives = {"Quick Start Unit 1": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan sapaan umum, frasa dasar yang sopan, tempat-tempat sekitar, dan menyewa kamar di hotel." + "\n" + baseText,
"Quick Start Unit 2": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan berbelanja di toko atau pasar, memesan di restoran, hari-hari dalam seminggu, cuaca, dan waktu." + "\n" + baseText,
"Quick Start Unit 3": "Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan keterampilan bahasa Inggris, memberikan arah ke suatu lokasi, dan meminta bantuan dalam situasi darurat." + "\n" + baseText,
}

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


