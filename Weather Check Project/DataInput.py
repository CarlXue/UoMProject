#from sklearn import *
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import csv
import numpy as np
import re
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_extraction import DictVectorizer


def fixText(text):
    row = []
    z = text.find(',')
    if z == 0:
        row.append('')
    else:
        row.append(text[:z])
    for x in range(len(text)):
        if text[x] != ',':
            pass
        else:
            if x == (len(text) - 1):
                row.append('')
            else:
                if ',' in text[(x + 1):]:
                    y = text.find(',', (x + 1))
                    c = text[(x + 1):y]
                else:
                    c = text[(x + 1):]
                row.append(c)
    return row


def createTuple(oldFile):
# oldFile is filename (e.g. 'sheet.csv')
    f1 = open(oldFile, "r")
    tup = []
    while 1:
        text = f1.readline()
        if text == "":
            break
        else:
            pass
        if text[-1] == '\n':
            text = text[:-1]
        else:
            pass
        row = fixText(text)
        tup.append(row)
    return tup


def incomeTrans(tup):
    for row in tup:
        for i in range(0, len(row) - 2):
            if(bool(re.search(regex, row[i])) == True):
                if(bool(re.search(regex, row[i + 1])) == True):
                    # join the strings
                    seq = (row[i], row[i + 1])
                    row[i] = ','.join(seq)
                    # pop out useless string
                    row.pop(i + 1)
                    break
                elif(bool(re.search(regex, row[i + 2])) == True):
                    seq = (row[i], row[i + 1], row[i + 2])
                    row[i] = ','.join(seq)
                    # pop out useless string
                    row.pop(i + 1)
                    row.pop(i + 1)
                    break
    return tup


def appUseTrans(tup):
    regex = '\"'

    for row in tup:
        count = 0
        templist = []
        index = 0
        length = len(row)
        for i in range(0, length):
            if (row[i].startswith(regex) and not(row[i].endswith(regex))):
                count += 1
                templist.append(row[i])
                index = i
            elif (row[i].endswith(regex) and not(row[i].startswith(regex))):
                templist.append(row[i])
                row[index] = ','.join(templist)
                # delete useless data
                #print(count, index)
                # print(row)
                # reset
                count = 0
                templist = []
                #print (row[index])

            elif (not(count == 0)):
                count += 1
                templist.append(row[i])
                # print(templist)
    for row in tup:
        for z in range(0, len(row)):
            if (row[0] == '3882027944'):
                row.pop(8)
                row.pop(8)
                # print(row)
                break
            if (row[0] == '3878526543'):
                row.pop(4)
                row.pop(4)
                row.pop(4)
                # print(row)
                break
            if (row[0] == '3878262512'):
                row.pop(8)
                row.pop(8)
                # print(row)
                break

    return tup


# app category
def createAppCategory(tup):
    appCategory = {}  # 'App': 'ID'
    counter = 0
    appCategory.update(
        {'A specific website or app (please provide the answer)': str(counter)})
    counter += 1
    appCategory.update({'-': str(counter)})
    for row in tup:
        for i in range(0, len(row)):
            if (row[2] == 'A specific website or app (please provide the answer)'):
                if len(appCategory) == 0:
                    counter += 1
                    appCategory[row[3]] = str(counter)
                    # print("ID: %d, %s" %(counter,row[3]))
                    break
                else:
                    for j in range(0, len(appCategory)):
                        if (not(row[3] in appCategory.keys())):
                            counter += 1
                            # print("ID: %d, %s" %(counter,row[3]))
                            appCategory[row[3]] = str(counter)
                            # print(row[3])
                            break

    return appCategory


def createIncomeCategory(tup):
    incomeCategory = {}  # 'incomeRange': 'ID'
    counter = -1
    for row in tup:
        for i in range(0, len(row)):
            if len(incomeCategory) == 0:
                counter += 1
                # print("ID: %d, %s" % (counter, row[7]))
                incomeCategory.update({row[7]: str(counter)})
                break
            else:
                for j in range(0, len(incomeCategory)):
                    if (not(row[7] in incomeCategory.keys())):
                        counter += 1
                        # print("ID: %d, %s" % (counter, row[7]))
                        # print(row)
                        incomeCategory.update({row[7]: str(counter)})
                        # print(row[3])
                        break
    return incomeCategory


def createCheckOrNotCategory(tup):
    checkOrNotCategory = {}  # 'CheckOrNot': 'ID'
    counter = -1
    for row in tup:
        for i in range(0, len(row)):
            if len(checkOrNotCategory) == 0:
                counter += 1
                # print("ID: %d, %s" % (counter, row[1]))
                checkOrNotCategory.update({row[1]: str(counter)})
                break
            else:
                for j in range(0, len(checkOrNotCategory)):
                    if (not(row[1] in checkOrNotCategory.keys())):
                        counter += 1
                        # print("ID: %d, %s" % (counter, row[1]))
                        checkOrNotCategory.update({row[1]: str(counter)})
                        break
    return checkOrNotCategory


def createHowCheckCategory(tup):
    howCheckCategory = {}  # 'HowCheck': 'ID'
    counter = -1
    for row in tup:
        for i in range(0, len(row)):
            if len(howCheckCategory) == 0:
                counter += 1
                # print("ID: %d, %s" % (counter, row[2]))
                howCheckCategory.update({row[2]: str(counter)})
                break
            else:
                for j in range(0, len(howCheckCategory)):
                    if (not(row[2] in howCheckCategory.keys())):
                        counter += 1
                        # print("ID: %d, %s" % (counter, row[2]))
                        howCheckCategory.update({row[2]: str(counter)})
                        break
    return howCheckCategory


def createWatchCheckCategory(tup):
    watchCheck = {}  # 'WatchCheck': 'ID'
    counter = -1
    for row in tup:
        for i in range(0, len(row)):
            if len(watchCheck) == 0:
                counter += 1
                # print("ID: %d, %s" % (counter, row[4]))
                watchCheck.update({row[4]: str(counter)})
                break
            else:
                for j in range(0, len(watchCheck)):
                    if (not(row[4] in watchCheck.keys())):
                        counter += 1
                        # print("ID: %d, %s" % (counter, row[4]))
                        watchCheck.update({row[4]: str(counter)})
                        break
    return watchCheck


def createAgeCategory(tup):
    age = {}  # 'Age': 'ID'
    counter = -1
    for row in tup:
        for i in range(0, len(row)):
            if len(age) == 0:
                counter += 1
                # print("ID: %d, %s" % (counter, row[5]))
                age.update({row[5]: str(counter)})
                break
            else:
                for j in range(0, len(age)):
                    if (not(row[5] in age.keys())):
                        counter += 1
                        # print("ID: %d, %s" % (counter, row[5]))
                        age.update({row[5]: str(counter)})
                        break
    return age


def createGenderCategory(tup):
    gender = {'Gender': 'ID'}
    counter = -1
    for row in tup:
        for i in range(0, len(row)):
            if len(gender) == 0:
                counter += 1
                # print("ID: %d, %s" % (counter, row[6]))
                gender.update({row[6]: str(counter)})
                break
            else:
                for j in range(0, len(gender)):
                    if (not(row[6] in gender.keys())):
                        counter += 1
                        # print("ID: %d, %s" % (counter, row[6]))
                        gender.update({row[6]: str(counter)})
                        break
    return gender


def createRegionCategory(tup):
    region = {'Region': 'ID'}
    counter = -1
    for row in tup:
        for i in range(0, len(row)):
            if len(region) == 0:
                counter += 1
                # print("ID: %d, %s" % (counter, row[8]))
                region.update({row[8]: str(counter)})
                break
            else:
                for j in range(0, len(region)):
                    if (not(row[8] in region.keys())):
                        counter += 1
                        # print("ID: %d, %s" % (counter, row[8]))
                        region.update({row[8]: str(counter)})
                        break
    return region


def categoryTrans(tup):
    appCategory = createAppCategory(tup)
    incomeCategory = createIncomeCategory(tup)
    checkOrNotCategory = createCheckOrNotCategory(tup)
    howCheckCategory = createHowCheckCategory(tup)
    watchCheckCategory = createWatchCheckCategory(tup)
    ageCategory = createAgeCategory(tup)
    genderCategory = createGenderCategory(tup)
    regionCategory = createRegionCategory(tup)

    for row in tup:
        for i in range(0, len(row)):
            if(row[0] == 'RespondentID'):
                row[0] = '0'
            if(row[1] in checkOrNotCategory.keys()):
                row[1] = checkOrNotCategory[row[1]]
            elif(row[2] in howCheckCategory.keys()):
                row[2] = howCheckCategory[row[2]]
            elif(row[3] in appCategory.keys()):
                row[3] = appCategory[row[3]]
            elif(row[4] in watchCheckCategory.keys()):
                row[4] = watchCheckCategory[row[4]]
            elif(row[5] in ageCategory.keys()):
                row[5] = ageCategory[row[5]]
            elif(row[6] in genderCategory.keys()):
                row[6] = genderCategory[row[6]]
            elif(row[7] in incomeCategory.keys()):
                row[7] = incomeCategory[row[7]]
            elif(row[8] in regionCategory.keys()):
                row[8] = regionCategory[row[8]]
    return tup


regex = '\"'
tup = createTuple('weather-check.csv')
tup = incomeTrans(tup)
# the last data table
final_data_table = appUseTrans(tup)
numericTable = categoryTrans(final_data_table)
for row in numericTable:
    for i in range(0, len(row)):
        row[i] = int(row[i])


attributeRange = [4, 5, 6, 7, 8]
attr = np.array([[l[i] for i in attributeRange] for l in numericTable])
classRange = [2]
classAttr = np.array([[l[i] for i in classRange] for l in numericTable])
# print(np.asarray(attr))
# print out the numeric table
#for rows in categoryTrans(final_data_table):
#    for i in range(0, len(rows)):
#        print(rows[i],"\t")
#    print("\n")

#print('\n'.join(['\t'.join(['{:}'.format(item) for item in row]) 
#for row in categoryTrans(final_data_table)]))


gnb = GaussianNB()
clf = gnb.fit(attr, classAttr)
for row in attr:
    print(clf.predict(row))
# print("Number of mislabeled points out of a total %d points : %d"
#    % (numericTable.shape[0],(classAttr != y_pred).sum()))
