def Method1(symptomVector):
    
    import csv
    import numpy as np
    
    symptoms = []  # list that contains the symptoms
    illnessMatrix = []  # matrix for symptoms and illnesses
#    dataMatrix = []  # logical matrix for symptoms and illnesses
    responseVector = symptomVector  # response vector from the GUI...as well as testing
    illnessDict = {}  # dictionary for totalling of matches for each illness
#    differentialDiag = []  # end differential diagnosis

    # read in symptoms into vector
    with open('SymptomList.csv', 'r') as file:
        read = csv.reader(file)
        for line in read:
            symptoms.append(line)

    # set the ERROR term to 0
    responseVector[17] = 0

    with open('IllnessesMatrix.csv', 'r') as file:
        read = csv.reader(file)
        for line in read:
            illnessMatrix.append(line)

    # parse the illness and the symptom into separate variables
    illnessList = [item[0] for item in illnessMatrix]  # list for illnesses
    symptomMatrix = [item[1:] for item in illnessMatrix]

    symptomMatrix = np.asarray(symptomMatrix).astype('float')

    # transpose responseVector for matrix multiplication...
    responseVector = np.transpose(responseVector)

    # matrix multiplication...
    for illness in range(len(illnessList)):
        illnessDict[illnessList[illness]] = symptomMatrix[illness].dot(responseVector)

    #print(illnessDict)

    sortedIllnessList = sorted(illnessDict, key=illnessDict.get, reverse=True)
    
    
#    for illness in sortedIllnessList:
#        print(illness, illnessDict[illness])
#        
#
#    print("\n")
#    print(sortedIllnessList)
#    print("\n")    
    
    return sortedIllnessList[0:3]
   

## TESTING PURPOSES
#from random import randint
#
#vector = []
#
#for num in range(69):
#    vector.append(randint(0,1))
#
#illness = Method1(vector)
#print("Diagnosis:", illness)