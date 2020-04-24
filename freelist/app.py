import math
import os
import sys
import csv
#import pdftotext
from collections import defaultdict


def convertpdftotext():
    pass
    # Still working on converting from PDF to text file. 
    # For now I convert manually using the pdftotext function any help would be appreciated. 

def scanwords():
    # fileDir = os.path.dirname(os.path.realpath('__file__'))

    global allwords
    allwords = defaultdict(int)
    
    with open('freelist/data/text/CAMUS-Letranger.txt', 'rb') as f:
        for line in f:
            for word in line.split():
                allwords[word.lower().decode('utf-8').strip('[].,«»:’’)(1234567890"').rstrip()] += 1
        #return allwords
    

def tocsv(w):

    lan = 'FR'
    with open('freelist/data/text/cleanTing.csv', 'w', newline="") as csv_file:  
        writer = csv.writer(csv_file)
        for key, value in w.items():
            writer.writerow([key, value, lan])




def toMongoDb():
    # This will be the function to send the date to Mongo DB. 
    # I have never used Mongo DB before this so im using this as a chance to practice. 
    # if word id does not exist insert into DB or else increment counter for later use. 
    # The question is should I use the word as the id? or should I have a seperate ID number?
    # Is it possible to see if a value already exists in a column before entering into DB? 
    # Im sure there must be a way. 
    pass

scanwords()
tocsv(allwords)



print ("--- Start Point---")
print ({k: v for k, v in sorted(allwords.items(), key=lambda item: item[0], reverse=True )})
