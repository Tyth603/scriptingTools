import os, shutil

def translitCheck(dir, organize):
    proj = os.path.split(dir)[1]

    for language in os.listdir(dir):
        langDir = os.path.join(dir, language)
        if (language[0]+language[1]) == "T_":
            pass
        else:
            translitLanguage = "T_" + language
            finalTranslitDir = os.path.join(os.path.split(langDir)[0], translitLanguage)
            for file in os.listdir(langDir):
                if "-T-" in file:
                    src = os.path.join(langDir, file)
                    dst = os.path.join(finalTranslitDir, file)
                    if os.path.exists(finalTranslitDir) == True:
                        shutil.move(src, dst)
                    else:
                        os.mkdir(finalTranslitDir)
                        shutil.move(src, dst)
    
        
    
if __name__ == "__main__":
    dir = "C:\Users\Delelopment\Desktop\\forChuck\project1"
    translitCheck(dir)


