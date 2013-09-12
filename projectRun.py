from organizeB4Us import organizeB4U
import createUnits
import createConfigYAML
import os
import shutil
import SupplementalVocabularyCourses as SVC
import QuickStartCourses as QS
import SupplementalVocabularyCourseESLSPAco as SVCSPAco
import SupplementalVocabularyCourseESLCMNcn as SVCCMNcn
import SupplementalVocabularyCourseESLINDid as SVCINDid
import SupplementalVocabularyCoursesJPNjpT as SVCJPNjpT
import time


def runCreateYAML(course):
    projectDir = course.proj1Dir
    for learnLanguage in os.listdir(projectDir):
        learnDir = os.path.join(projectDir, learnLanguage)
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
    projectDir = course.proj1Dir
    for language in os.listdir(projectDir):
        knownLangPath = os.path.join(projectDir, language)
        for learnLangDir in os.listdir(knownLangPath):
            #print learnLangDir
            if learnLangDir == "revision.txt":
                pass
            else:
                learnLangPath = os.path.join(knownLangPath, learnLangDir)
                for unit in os.listdir(learnLangPath):
                    finalUnitDir = os.path.join(learnLangPath, unit)
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
def checkNumberOfUnits(projectDir, projUnitNameList):
    nameList = projUnitNameList
    for language in os.listdir(projectDir):
        langDir = os.path.join(projectDir, language)
        if language != "not_enough_units":
            if len(nameList) == len(os.listdir(langDir)):
                pass
            else:
                src = langDir
                dst = os.path.join(projectDir, "not_enough_units", language)
                shutil.move(src, dst)


#dir = project level directory
def createRevision(projectDir):
    for lang in os.listdir(projectDir):
        langDir = os.path.join(projectDir, lang)
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
                           courseConfig.lessonToList, courseConfig.isESLTrue, courseConfig.unitNumberToNames,
                           courseConfig.isTranslit)
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

    eslCMNcnConfig = SVCCMNcn.createSVCConfiguration()
    createCourse(eslCMNcnConfig)

    eslINDidConfig = SVCINDid.createSVCConfiguration()
    createCourse(eslINDidConfig)

    SVCJPNjpTConfig = SVCJPNjpT.createSVCConfiguration()
    createCourse(SVCJPNjpTConfig)