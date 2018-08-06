'''
Created on Aug 4, 2018

@author: Rajesh Rathod
'''
from random import randint

#Initialize the list
listOfNumbers=[]

def generateRandomNumbers(totalNum, numRange, printNum):
    #Generate Random numbers within the range provided
    for i in range(totalNum):
        listOfNumbers.append(randint(0,numRange))
    #Sort the list of random numbers
    listOfNumbers.sort()
    #Print the sorted list of numbers
    for i in range(totalNum):
        print(i, listOfNumbers[i])
    #Print the nth smallest number from the list
    print("%dth smallest number is %d" %(printNum,listOfNumbers[printNum-1]))
    
#generateRandomNumbers(1000,20000000,9)
