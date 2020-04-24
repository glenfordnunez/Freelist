import os
import sys
import csv
from collections import defaultdict
import PyPDF2 
import textract
#from nltk.tokenize import word_tokenize

#import pdftotext



def convertpdftotext():
    FILE_PATH = './freelist/data/pdf/HP_Deutch.pdf'

    with open(FILE_PATH, mode='rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        maxpages = reader.numPages
        
        newf = open('freelist/data/text/HP_Deutch.txt', 'w')

        for i in range(0, maxpages):
            page = reader.getPage(i)
            newf.write(page.extractText())
        newf.close()



def scanwords():
    # fileDir = os.path.dirname(os.path.realpath('__file__'))

    global allwords
    allwords = defaultdict(int)
    
    with open('freelist/data/text/HP_Deutch.txt', 'rb') as f:
        for line in f:
            for word in line.split():
                # This is stripping all of the sympbols and numbers from each word in file. 
                # Not sure if there is a more efficient way to do this. It seems fairly fast. 
                allwords[word.lower().decode('utf-8').strip(' .!?[],«»:’’)(1234567890"ÇÐ').rstrip()] += 1
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

def printTest():
# This is a test that prints all of the words and word count from the text file. 
    print ("--- Starting Point---")
    print ({k: v for k, v in sorted(allwords.items(), key=lambda item: item[0], reverse=True )})

convertpdftotext()
scanwords()
tocsv(allwords)
#printTest()