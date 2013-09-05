__author__ = 'vagrant'
from CourseConfiguration import courseConfiguration


englishForIndonesianProjectName = "QS_ESL_Courses"
englishForIndonesianLessonOrder = {
    "Start Cepat Unit 1":[
        "Pelajaran 1",
        "Pelajaran 2",
        "Pelajaran 3"
    ],
    "Start Cepat Unit 2" : [
        "Pelajaran 4",
        "Pelajaran 5",
        "Pelajaran 6"
    ],
    "Start Cepat Unit 3" : [
        "Pelajaran 7",
        "Pelajaran 8",
        "Pelajaran 9",
        "Pelajaran 10"
    ]
}
englishForIndonesianUnitNameList = englishForIndonesianLessonOrder.keys()


def createConfiguration():
    configObject = courseConfiguration()
    configObject.projectName = englishForIndonesianProjectName
    configObject.unitNameList = englishForIndonesianUnitNameList

    configObject.lessonOrder = englishForIndonesianLessonOrder

    return configObject


    # configObject.unitNameList = unitNameList
    # configObject.languageDict = languageDict
    # configObject.unitMap = unitMap
    # configObject.unitObjectives = unitObjectives
    # configObject.lessonOrder = lessonOrder