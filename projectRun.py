import os
import shutil
import time
import re
import fileinput
import sys

from courseConfigurations import SupplementalVocabularyCourseESLCMNcn as SVCCMNcn
from organizeB4Us import organizeB4U
import createUnits
import createConfigYAML
import courseConfigurations.SupplementalVocabularyCourses as SVC
import QuickStartCourses as QS
import courseConfigurations.SupplementalVocabularyCourseESLSPAco as SVCSPAco
import courseConfigurations.SupplementalVocabularyCourseESLINDid as SVCINDid
import courseConfigurations.SupplementalVocabularyCoursesJPNjpT as SVCJPNjpT
import courseConfigurations.SupplementalVocabularyCourseESLFRAfr as SVCFRAfr
import courseConfigurations.SupplementalVocabularyCoursesESLSWHke as SVCSWHke
import courseConfigurations.SupplementalVocabularyCoursesESLPORbr as SVCPRObr
from QuickStartCourses import createConfigurationForEnglishForSwahili as QSSHHkes


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


def stripTagging(projectDir):
    for folder in os.listdir(projectDir):
        folder = os.path.join(projectDir, folder)
        for subFolder in os.listdir(folder):
            subFolder = os.path.join(folder, subFolder)
            for langFolder in os.listdir(subFolder):
                if not langFolder.endswith(".txt"):
                    langFolder = os.path.join(subFolder, langFolder)
                    for unitFolder in os.listdir(langFolder):
                        unitFolder = os.path.join(langFolder, unitFolder)
                        for b4xFolder in os.listdir(unitFolder):
                            if b4xFolder.endswith(".xml") or b4xFolder.endswith(".yaml"):
                                pass
                            else:
                                b4xFolder = os.path.join(unitFolder, b4xFolder)
                                for file in os.listdir(b4xFolder):
                                    if file.endswith(".xml"):
                                        file = os.path.join(b4xFolder, file)
                                        #f = open(file, "w+")
                                        for line in fileinput.input(file, inplace=True):
                                            line = re.sub(r"&lt;.*&gt;", "", line)
                                            sys.stdout.write(line)


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
    stripTagging(organize.proj1Dir)


if __name__ == "__main__":
    QSSHHkesConfig = QSSHHkes()
    createCourse(QSSHHkesConfig)

    # eslPRObrConfig = SVCPRObr.createSVCConfiguration()
    # createCourse(eslPRObrConfig)

    # eslSWHkefrConfig = SVCSWHke.createSVCConfiguration()
    # createCourse(eslSWHkefrConfig)

    # eslFRAfrConfig = SVCFRAfr.createSVCConfiguration()
    # createCourse(eslFRAfrConfig)

    # qsConfig = QS.createConfiguration()
    # createCourse(qsConfig)
    #
    # EtoThaiConfig = QS.createConfigurationForEnglishForThai()
    # createCourse(EtoThaiConfig)
    #
    # eslSPAcoConfig = SVCSPAco.createSVCConfiguration()
    # createCourse(eslSPAcoConfig)
    #
    # eslCMNcnConfig = SVCCMNcn.createSVCConfiguration()
    # createCourse(eslCMNcnConfig)
    #
    # SVCJPNjpTConfig = SVCJPNjpT.createSVCConfiguration()
    # createCourse(SVCJPNjpTConfig)
    #
    # supplementalConfig = SVC.createSVCConfiguration()
    # createCourse(supplementalConfig)
    #
    # eslINDidConfig = SVCINDid.createSVCConfiguration()
    # createCourse(eslINDidConfig)
