import pdb

print('Reading in of Data...')

# read in data
import csv
import numpy as np
from random import randint

symptoms = []
illnessMatrix = [] # matrix for illnesses and symptoms
illnessList = [] # list of illnesses
dataMatrix = [] # logical matrix
responseVector = []

print('Converting response vector -> numpy vector')    

with open('SymptomList.csv', 'r') as file:
    read = csv.reader(file)
    for line in read:
        symptoms.append(line) # convert to list

# read in symptoms into vector

# creation of test responseVector
for number in range(len(symptoms)):
    responseVector.append(randint(0,1))

with open('IllnessesMatrix.csv','r') as file:
    read = csv.reader(file)
    count = 0
    for line in read:  
        illnessMatrix.append(line)
    for illness in illnessMatrix:
        count = count + 1
        
    
    #dataMatrix = np.asarray(dataMatrix)
        
#print(illnessMatrix)
#print(illnessMatrix[1][1:69])
