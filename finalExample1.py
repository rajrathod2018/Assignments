'''
Created on Aug 4, 2018

@author: Rajesh Rathod
'''
from pip._vendor.pyparsing import line

def doesFileExist(fileName):
    try:
        fin= open(fileName)
        print("\n")
        for rawLine in fin:
            line=rawLine.rstrip('\r\n')
            twoParts=line.split('-')
            description=twoParts[1]
            print(twoParts[0])
            dscrInfo=description.split(',')
            for rawInfo in dscrInfo:
                info=rawInfo.lstrip()
                print(info)
        fin.close()
    except:
        print("Something went wrong. File", fileName, "does not exist.")
        
#doesFileExist('testFile.txt')
#doesFileExist('newTestFile.txt')