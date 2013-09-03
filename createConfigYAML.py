import os
from UnitObjectives import unitObjectives


def createYAML(unitDir):
    configLocation = os.path.join(unitDir, "config.yaml")
    unit = os.path.split(os.path.split(unitDir)[0])[1]
    activities = ["Reading", "Preview", "SelfReportingRecognize", "Pronunciation", "AudioMultiChoice",
                  "MultipleChoice2", "Matching", "SelfReportingProduce", "Dictation2", "ProduceWritten"]

    maxItems = 10
    minScore = 65
    showHints = 'true'
    description = unitObjectives[unit]
    modules = ["ListeningRecognitionA", "WrittenProduceA"]
    Line1 = "activities: %s \n" % activities
    Line2 = "tlx_activities: []\n"
    Line3 = "name: '%s' \n" % unit
    Line4 = "assessment: \n"
    Line5 = "  maxitems: %d \n" % maxItems
    Line6 = "  minscore: %d \n" % minScore
    Line7 = "  modules: %s \n" % modules
    Line8 = "  showhints: %s \n" % showHints
    Line9 = "description: '%s' \n" % description
    lines = [Line1, Line2, Line3, Line4, Line5, Line6, Line7, Line8, Line9]
    f = open(configLocation, "w+")
    for line in lines:
        f.write(line)
    f.close()
    pass
    

if __name__ == "__main__":
    unitDir = "C:\Users\Delelopment\Desktop\\forChuck\project1\Afrikaans\Asking-for-Direction"
    createYAML(unitDir)

'''
activities: []
tlx_activities: []
name: a unit name
assessment:
  maxitems: 10
  minscore: 90
  modules: []
  showhints: 'true'
description: my unit
'''