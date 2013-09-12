__author__ = 'vagrant'


class courseConfiguration:
    def __init__(self):
        pass

    def createUnitNumbers(self, unitNameList):
        unitNumbers = {}
        for item in unitNameList:
            unitNumbers.update({item: unitNameList.index(item) + 1})
        return unitNumbers


    def createUnitNumberToNames(self, unitNameList):
        unitNumberToName = {}
        for item in unitNameList:
            unitNumberToName.update({"unit" + unicode(unitNameList.index(item) + 1): unicode(item)})
        return unitNumberToName