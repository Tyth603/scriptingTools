from organizeB4Us import organizeB4U
import createUnits
import createConfigYAML
import os
import shutil
import SupplementalVocabularyCourses as SVC
import QuickStartCourses as QS
import SupplementalVocabularyCourseESLSPAco as SVCSPAco
import time


def runCreateYAML(course):
    dir = course.proj1Dir
    for learnLanguage in os.listdir(dir):
        learnDir = os.path.join(dir, learnLanguage)
        for knownLanguage in os.listdir(learnDir):
            knownDir = os.path.join(learnDir, knownLanguage)
            for unit in os.listdir(knownDir):
                unitDir = os.path.join(knownDir, unit, "data")
                if os.path.isdir(unitDir):
                    course.unitDir = unitDir
                    createConfigYAML.createYAML(course)
                else:
                    pass


def cleanUp(course):
    dir = course.proj1Dir
    for language in os.listdir(dir):
        knownLangPath = os.path.join(dir, language)
        for learnLangDir in os.listdir(knownLangPath):
            #print learnLangDir
            if learnLangDir == "revision.txt":
                pass
            else:
                learnLangPath = os.path.join(knownLangPath, learnLangDir)
                for unit in os.listdir(learnLangPath):
                    unitDir = os.path.join(learnLangPath, unit)
                    if unit != "revision.txt":
                        finalUnitDir = os.path.join(learnLangPath, "unit" + str(course.unitNumbers[unit]))
                        os.rename(unitDir, finalUnitDir)
                    if unit == "revision.txt":
                        pass
                    else:
                        if unit == "config.yaml":
                            os.remove(finalUnitDir)
                        else:
                            for B4X in os.listdir(finalUnitDir):
                                print B4X
                                b4xDir = os.path.join(finalUnitDir, B4X)
                                if B4X == "OUTPUT_B4Xs_1":
                                    os.rmdir(b4xDir)
                                elif unit.endswith(".b4u"):
                                    os.remove(b4xDir)
                                elif unit.endswith(".yaml"):
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
                dst = os.path.join(dir, "not_enough_units", language)
                shutil.move(src, dst)

#dir = project level directory
def createRevision(dir):
    for lang in os.listdir(dir):
        langDir = os.path.join(dir, lang)
        for lang2 in os.listdir(langDir):
            if lang2 != "not_enough_units":
                lang2Dir = os.path.join(langDir, lang2)
                fileName = "revision.txt"
                filePath = os.path.join(lang2Dir, fileName)
                if os.path.exists(filePath):
                    pass
                else:
                    f = open(filePath, "w+")
                    f.write(str(time.time()))
                    f.close()


def runUnitGenerator(paths):
    for knownLanguage in os.listdir(paths):
        knownDir = os.path.join(paths, knownLanguage)
        for learnLanguage in os.listdir(knownDir):
            learnDir = os.path.join(knownDir, learnLanguage)
            for unit in os.listdir(learnDir):
                unitDir = os.path.join(learnDir, unit)
                cmd = 'python "D:\working\\forChuck\\unit_generator.py" -u -p "%s"' % unitDir
                os.system(cmd)


def createCourse(courseConfig):
    organize = organizeB4U(courseConfig.unitNameList, courseConfig.languageDict, courseConfig.unitMap,
                           courseConfig.projectName, courseConfig.unitObjectives,
                           courseConfig.lessonOrder, courseConfig.unitNumbers,
                           courseConfig.lessonToList, courseConfig.isESLTrue)
    createUnits.tmpOrganize(organize.finalPathNames)
    runCreateYAML(organize)
    runUnitGenerator(organize.proj1Dir)
    createRevision(organize.proj1Dir)
    cleanUp(organize)


if __name__ == "__main__":
    supplementalConfig = SVC.createSVCConfiguration()
    createCourse(supplementalConfig)

    qsConfig = QS.createConfiguration()
    createCourse(qsConfig)

    eslSPAcoConfig = SVCSPAco.createSVCConfiguration()
    createCourse(eslSPAcoConfig)