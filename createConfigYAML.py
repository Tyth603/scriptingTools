import os
import codecs


def createYAML(course):
    unitDir = course.unitDir
    unitObjectives = course.unitObjectives
    lessonOrder = course.lessonOrder
    configLocation = os.path.join(unitDir, "config.yaml")
    unit = unicode(course.unitNumberToName[os.path.split(os.path.split(unitDir)[0])[1]])
    activities = ["Reading", "Preview", "SelfReportingRecognize", "Pronunciation", "AudioMultiChoice",
                  "MultipleChoice2", "Matching", "SelfReportingProduce", "Dictation2", "ProduceWritten"]
    if course.isESLTrue:
        lessonMap = {}
        for lesson in lessonOrder[unit]:
            print lesson
            lessonMap.update({lesson: course.lessonMap[lesson]})
        lessonMapString = ""
        for item in lessonMap:
            lessonMapString = unicode(lessonMapString) + "\n" + " " + unicode(item) + ": " + unicode(course.lessonMap[item])
    else:
        lessonMapString = ""

    maxItems = 10
    minScore = 65
    showHints = 'true'
    description = unitObjectives[unit]
    modules = ["ListeningRecognitionA", "WrittenProduceA"]
    Line1 = "activities: %s \n" % activities
    Line2 = "tlx_activities: []\n"
    Line3 = u"name: '%s' \n" % unicode(unit)
    Line4 = "assessment: \n"
    Line5 = "  maxitems: %d \n" % maxItems
    Line6 = "  minscore: %d \n" % minScore
    Line7 = "  modules: %s \n" % modules
    Line8 = "  showhints: %s \n" % showHints
    Line9 = "description: '%s' \n" % description
    Line10 = u"lessonOrder: %s \n" % unicode(lessonOrder[unit])
    Line11 = u"lessonListMap: %s \n" % unicode(lessonMapString)
    Line12 = "isESLTrue: %s \n" % str(course.isESLTrue)
    lines = [Line1, Line2, Line3, Line4, Line5, Line6, Line7, Line8, Line9, Line10, Line11, Line12]
    f = codecs.open(configLocation, "w+", "utf-8")
    for line in lines:
        print line
        f.write(unicode(line))
    f.close()
    pass