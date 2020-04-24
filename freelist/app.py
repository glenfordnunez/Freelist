import math
import os
import sys
#import pdftotext
from collections import defaultdict


Ting = defaultdict(int)


def getpdf():
    pass

def scanwords():
    #fileDir = os.path.dirname(os.path.realpath('__file__'))


    with open('freelist/data/text/CAMUS-Letranger.txt', 'rb') as f:
        for line in f:
            for word in line.split():
                Ting[word.lower().decode('utf-8').strip('.,')] += 1



def todb():
    pass

scanwords()


print ("--- Start Point---")

print ({k: v for k, v in sorted(Ting.items(), key=lambda item: item[1], reverse=True )})