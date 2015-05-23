#from sklearn import *
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import csv
import numpy as np
import re

def fixText(text):
    row = []
    z = text.find(',')
    if z == 0:  row.append('')
    else:   row.append(text[:z])
    for x in range(len(text)):
        if text[x] != ',':  pass
        else:
            if x == (len(text)-1):  row.append('')
            else:
                if ',' in text[(x+1):]:
                    y = text.find(',', (x+1))
                    c = text[(x+1):y]
                else:   
                    c = text[(x+1):]
                row.append(c)
    return row
    
def createTuple(oldFile):
## oldFile is filename (e.g. 'sheet.csv')
    f1 = open(oldFile, "r")
    tup = []
    while 1:
        text = f1.readline()
        if text == "":  break
        else:   pass
        if text[-1] == '\n':
            text = text[:-1]
        else:   pass
        row = fixText(text)
        tup.append(row)
    return tup
tup = createTuple('weather-check.csv')

regex = '\"'

for row in tup:
    for i in range(0,len(row)-2):
        if(bool(re.search(regex, row[i])) == True):
            if(bool(re.search(regex,row[i+1])) == True):
                #join the strings
                seq = (row[i], row[i+1])
                row[i] = ','.join(seq)
                #pop out useless string
                row.pop(i+1)
                break
            elif(bool(re.search(regex,row[i+2])) == True):
                seq = (row[i], row[i+1], row[i+2])
                row[i] = ','.join(seq)
                #pop out useless string
                row.pop(i+1)
                row.pop(i+1)
                break
for row in tup:
     print(row)               


