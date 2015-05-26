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
def incomeTrans(tup):
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
    return tup
    
    
def appUseTrans(tup):
    regex = '\"'

    for row in tup:
        count = 0
        templist = []
        index = 0
        length = len(row)
        for i in range(0,length):
            if (row[i].startswith(regex) and not(row[i].endswith(regex))):
                count += 1
                templist.append(row[i])
                index = i
            elif (row[i].endswith(regex) and not(row[i].startswith(regex))):
                templist.append(row[i])
                row[index] = ','.join(templist)
                #delete useless data
                #print(count, index)                    
                #print(row)
                #reset
                count = 0
                templist =[]
                #print (row[index])
                
            elif (not(count == 0)):
                count += 1
                templist.append(row[i])
                #print(templist)
    for row in tup:
        for z in range(0,len(row)):
            if (row[0] == '3882027944'):
                row.pop(8)
                row.pop(8)
                #print(row)
                break
            if (row[0] == '3878526543'):
                row.pop(4)
                row.pop(4)
                row.pop(4)
                #print(row)
                break
            if (row[0] == '3878262512'):
                row.pop(8)
                row.pop(8)
                #print(row)
                break

    return tup
                                


# app category
def createAppCategory(tup):    
    appCategory = {'App':'ID'}
    counter = 0                   
    for row in tup:
        for i in range(0,len(row)):
            if (row[2] == 'A specific website or app (please provide the answer)'):
                if len(appCategory) == 0 :
                    counter += 1
                    appCategory.update({row[3]:str(counter)})
                    #print("ID: %d, %s" %(counter,row[3]))                                  
                    break
                else:
                    for j in range(0,len(appCategory)):
                        if (not(row[3] in appCategory.keys())):
                            counter += 1
                            #print("ID: %d, %s" %(counter,row[3]))
                            appCategory.update({row[3]:str(counter)})
                            #print(row[3])   
                            break            
    return appCategory
    
def appCategoryTrans(tup):
    newT = incomeTrans(tup)
    dict = createAppCategory(tup)
    for row in tup:
        for i in range(3,4):
            if(row[3] in dict.keys()):
                row[3] = dict[row[3]]
    return tup
   
def createIncomeCategory(tup): 
    incomeTrans(tup)   
    incomeCategory = {'incomeRange':'ID'}
    counter = 0                   
    for row in tup:
        for i in range(0,len(row)):
           if len(incomeCategory) == 0 :
               counter += 1
               print("ID: %d, %s" %(counter,row[7]))
               appCategory.update({row[7]:str(counter)})
               break
           else:
               for j in range(0,len(incomeCategory)):
                    if (not(row[7] in incomeCategory.keys())):
                        counter += 1
                        print("ID: %d, %s" %(counter,row[7]))
                        print(row)
                        incomeCategory.update({row[7]:str(counter)})
                        #print(row[3])   
                        break            
    return incomeCategory 
 



tup = incomeTrans(tup)
# the last data table
final_data_table = appUseTrans(tup)



