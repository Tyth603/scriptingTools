import os
import time
from batch_b4u_converter import B4U_Convert

class convert():
    def __init__(self, dir):
        for language in os.listdir(dir):
            langDir = os.path.join(dir, language)
            if language != "not_enough_units":
                for unit in os.listdir(langDir):
                    unitDir = os.path.join(langDir, unit)
                    for file in os.listdir(unitDir):
                        print file
                        if file.endswith(".b4u") == True:
                            self.convertB4U(os.path.join(unitDir, file))
        time.sleep(1)
        for language in os.listdir(dir):
            langDir = os.path.join(dir, language)
            for unit in os.listdir(langDir):
                unitDir = os.path.join(langDir, unit)
                if unit != "not_enough_units":
                    for file in os.listdir(unitDir):
                        if file.endswith(".b4u") == True: 
                            self.deleteB4U(os.path.join(unitDir, file))

    def convertB4U(self, file):
        convert = B4U_Convert()
        outputDir = os.path.join(os.path.split(file)[0], "B4X_OUTPUT")
        finalDir = os.path.join(outputDir, os.path.split(file)[1][:-4])
        if not os.path.exists(finalDir):
            try:
                
                time.sleep(1)
                convert.processMessage(file, outputDir)
            except TypeError, e:
                print "CONVERSION FAILED %s" (file)
                raise
        else:
            print "FIX ME"
        pass
        #currently I am going to just use the old B4U_Util.jar but this will not work for all languages so at some point I need to point it at the AMQP B4U converter service

    def deleteB4U(self, file):
        outputDir = os.path.join(os.path.split(file)[0], "B4X_OUTPUT")
        finalDir = os.path.join(outputDir, os.path.split(file)[1][:-4])
        if os.path.exists(finalDir):
            try:
                os.remove(file)
            except (OSError) as e:
                print "Path is a Directory: Can not be Deleted"
    
if __name__=="__main__":
    conv = convert("C:\Users\Delelopment\Desktop\\forChuck\project1")
    #convertB4U("C:\Users\Delelopment\Desktop\\forChuck\project1\Afrikaans\AFRza-ENGus-Asking-for-Directions-1.b4u")
    #deleteB4U("C:\Users\Delelopment\Desktop\\forChuck\project1\Afrikaans\AFRza-ENGus-Asking-for-Directions-1.b4u")