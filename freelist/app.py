import math
import os
import sys
import csv
#import pdftotext
from collections import defaultdict


def getpdf():
    pass
    #Still working on converting from PDF to text file. 
    #For now I convert manually using the pdftotext function any help would be appreciated. 

def scanwords():
    #fileDir = os.path.dirname(os.path.realpath('__file__'))

    global Ting
    Ting = defaultdict(int)
    
    with open('freelist/data/text/CAMUS-Letranger.txt', 'rb') as f:
        for line in f:
            for word in line.split():
                Ting[word.lower().decode('utf-8').strip('.,«»')] += 1
        return Ting

def tocsv(w):
    with open('freelist/data/text/cleanTing.csv', 'w', newline="") as csv_file:  
        writer = csv.writer(csv_file)
        for key, value in w.items():
            writer.writerow([key, value])


scanwords()
tocsv(Ting)



#print ("--- Start Point---")
#print ({k: v for k, v in sorted(Ting.items(), key=lambda item: item[1], reverse=True )})
