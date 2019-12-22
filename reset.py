
import os

DistDir = "I:\\Python"

def CheckDirIsExist(dir,expectations):
    d = os.listdir(dir)
    for dirName in d :
        if dirName == expectations:
             return True
    return False  

def mkOneDir(dir):
    if(os.makedirs(dir)  == None):
        return  dir

def checkDir():
    curDir = os.getcwd()
    print(curDir)
    print(os.chdir(curDir))
    print("I:\\Python\\zwftest exist??: ",CheckDirIsExist(DistDir,"zwftest"))
    if(os.path.exists(DistDir+"\\zwftest") == False):
        print(mkOneDir(DistDir+"\\zwftest"))
    #os.system("calc.exe")
    print(os.path.abspath("."))
    print(os.listdir("."))


def main():
    print("starting main()")
    checkDir()

if __name__ == "__main__":
    main()
