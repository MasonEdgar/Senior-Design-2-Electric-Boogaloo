import pdb

# read in data
import csv
import numpy as np
import operator
from random import randint

symptoms = [] # list that contains the symptoms
illnessMatrix = [] # matrix for symptoms and illnesses
dataMatrix = [] # logical matrix for symptoms and illnesses
responseVector = [] # response vector from the GUI...as well as testing
illnessDict = {} # dictionary for totalling of matches for each illness
differentialDiag = [] # end differential diagnosis

# read in symptoms into vector
with open('SymptomList.csv', 'r') as file:
    read = csv.reader(file)
    for line in read:
        symptoms.append(line)

# creation of test responseVector
for number in range(len(symptoms)):
    responseVector.append(randint(0,1))

# set the ERROR term to 0
responseVector[17] = 0

# conversion to numpy array/vector
responseVector = np.asarray(responseVector).astype('int')

with open('IllnessesMatrix.csv','r') as file:
    read = csv.reader(file)
    for line in read:
        illnessMatrix.append(line)

# parse the illness and the symptom into separate variables
illnessList = [item[0] for item in illnessMatrix] # list for illnesses
symptomMatrix = [item[1:] for item in illnessMatrix]

symptomMatrix = np.asarray(symptomMatrix).astype('int')

# transpose responseVector for matrix multiplication...
responseVector = np.transpose(responseVector)

# matrix multiplication...
for illness in range(len(illnessList)):
    illnessDict[illnessList[illness]] = symptomMatrix[illness].dot(responseVector)

#print(responseVector)
#print(symptomMatrix)
print(illnessDict)

# for number in range(3):
#     maxIllness = max(illnessDict.iteritems(), key = operator.itemgetter(1))[0]
#     differentialDiag.append(maxIllness)
#     illnessDict.pop(maxIllness, None)

# sorting of dictionary from greatest to least
sortedIllnessList = sorted(illnessDict, key=illnessDict.get, reverse=True)
for illness in sortedIllnessList:
    print(illness, illnessDict[illness])

