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
unitMap = {
    "Start Cepat Unit 1" : [
        "01-Quick-Start",
        "02-Quick-Start",
        "03-Quick-Start",
    ],
    "Start Cepat Unit 2" : [
        "04-Quick-Start",
        "05-Quick-Start",
        "06-Quick-Start",
    ],
    "Start Cepat Unit 3" : [
        "07-Quick-Start",
        "08-Quick-Start",
        "09-Quick-Start",
        "10-Quick-Start",
    ]
}
englishForIndonesianUnitObjectives = {"Start Cepat Unit 1":"""Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan sapaan umum, frasa dasar yang sopan, tempat-tempat sekitar, dan menyewa kamar di hotel.

Unit ini akan membantu Anda...

- mengingat kata-kata dan frasa-frasa yang terkait dengan topik ini
- belajar membaca dan menulis kata-kata dan frasa-frasa tersebut
- mengenal bunyi dan bisa mengucapkannya dengan benar

Mulailah dengan aktivitas seperti Perbandingan Bahasa dan Latihan Pengucapan untuk membantu Anda menjadi terbiasa dengan materi ini.

Lanjutkan dengan aktivitas pilihan ganda dan menjodohkan yang berbasis wicara untuk meningkatkan pemahaman Anda atas kata-kata dan frasa-frasa yang diberikan.

Kemudian, lengkapi aktivitas menyimak dan mengetik untuk mempraktikkan produksi dan penulisan bahasa.

Akhirnya, lengkapi aktivitas penilaian pada akhir unit untuk menguji pengetahuan Anda atas kata-kata dan frasa-frasa yang diberikan.""",
                                      "Start Cepat Unit 2":"""Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan berbelanja di toko atau pasar, memesan di restoran, hari-hari dalam seminggu, cuaca, dan waktu.

Unit ini akan membantu Anda...

- mengingat kata-kata dan frasa-frasa yang terkait dengan topik ini
- belajar membaca dan menulis kata-kata dan frasa-frasa tersebut
- mengenal bunyi dan bisa mengucapkannya dengan benar

Mulailah dengan aktivitas seperti Perbandingan Bahasa dan Latihan Pengucapan untuk membantu Anda menjadi terbiasa dengan materi ini.

Lanjutkan dengan aktivitas pilihan ganda dan menjodohkan yang berbasis wicara untuk meningkatkan pemahaman Anda atas kata-kata dan frasa-frasa yang diberikan.

Kemudian, lengkapi aktivitas menyimak dan mengetik untuk mempraktikkan produksi dan penulisan bahasa.

Akhirnya, lengkapi aktivitas penilaian pada akhir unit untuk menguji pengetahuan Anda atas kata-kata dan frasa-frasa yang diberikan.""",
                                      "Start Cepat Unit 3":"""Unit ini mengajarkan kata-kata dan frasa-frasa penting yang terkait dengan keterampilan bahasa Inggris, memberikan arah ke suatu lokasi, dan meminta bantuan dalam situasi darurat.

Unit ini akan membantu Anda...

- mengingat kata-kata dan frasa-frasa yang terkait dengan topik ini
- belajar membaca dan menulis kata-kata dan frasa-frasa tersebut
- mengenal bunyi dan bisa mengucapkannya dengan benar

Mulailah dengan aktivitas seperti Perbandingan Bahasa dan Latihan Pengucapan untuk membantu Anda menjadi terbiasa dengan materi ini.

Lanjutkan dengan aktivitas pilihan ganda dan menjodohkan yang berbasis wicara untuk meningkatkan pemahaman Anda atas kata-kata dan frasa-frasa yang diberikan.

Kemudian, lengkapi aktivitas menyimak dan mengetik untuk mempraktikkan produksi dan penulisan bahasa.

Akhirnya, lengkapi aktivitas penilaian pada akhir unit untuk menguji pengetahuan Anda atas kata-kata dan frasa-frasa yang diberikan.""",}

unitNumbers = {"Start Cepat Unit 1": 1,
               "Start Cepat Unit 2": 2,
               "Start Cepat Unit 3": 3}

lessonNameToListNameMap = {
    "Pelajaran 1":"01-Quick-Start",
    "Pelajaran 2":"02-Quick-Start",
    "Pelajaran 3":"03-Quick-Start",
    "Pelajaran 4":"04-Quick-Start",
    "Pelajaran 5":"05-Quick-Start",
    "Pelajaran 6":"06-Quick-Start",
    "Pelajaran 7":"07-Quick-Start",
    "Pelajaran 8":"08-Quick-Start",
    "Pelajaran 9":"09-Quick-Start",
    "Pelajaran 10":"10-Quick-Start",
}
unitList = ["Start Cepat Unit 1","Start Cepat Unit 2","Start Cepat Unit 3"]

isESLTrue = True

def createConfiguration():
    configObject = courseConfiguration()
    configObject.projectName = englishForIndonesianProjectName
    configObject.unitNameList = englishForIndonesianUnitNameList
    configObject.languageDict = languageDict
    configObject.lessonOrder = englishForIndonesianLessonOrder
    configObject.unitMap = unitMap
    configObject.unitObjectives = englishForIndonesianUnitObjectives
    configObject.unitNumbers = unitNumbers
    configObject.lessonToList = lessonNameToListNameMap
    configObject.isESLTrue = isESLTrue
    configObject.unitNumberToNames = configObject.createUnitNumberToNames(unitList)
    return configObject


