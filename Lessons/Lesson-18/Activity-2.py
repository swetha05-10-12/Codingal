import random
import time

def getRandomDate(startDate,endDate):
    print("Printing a random date in between",startDate,"and",endDate)
    randomGenerator=random.random()
    dateformat= '%m/%d/%y'
    startTime= time.mktime(time.strptime(startDate,dateformat))
    endTime=time.mktime(time.strptime(endDate,dateformat))

    randomTime= startTime+randomGenerator*(endTime-startTime)
    randomDate= time.strptime(dateformat, time.localtime(randomTime))
    return randomDate
print("Random date=",getRandomDate("1/1/2016","12/12/2018"))