'''

Author: Mason Edgar
Symptom Checking Algorithm for the PMDK
University of Houston 
Senior Captson 2017


'''

import numpy as np
import pandas as pd
df = pd.read_excel('/Users/Mason/Documents/Senior-Design-2-Electric-Boogaloo/Test Procedure/Symptom Checker/Illness Matrix Barebones .xlsx')
illness_matrix = df.as_matrix()

np.set_printoptions(threshold=np.nan)

Anemia = illness_matrix[0]
Bronchitis = illness_matrix[1]
ColdSore = illness_matrix[2]
Conjunctivitis = illness_matrix[3]
Diabetes = illness_matrix[4]
Chickenpox = illness_matrix[5]
KidneyStones = illness_matrix[6]
Migraines = illness_matrix[7]
PollenAllergy = illness_matrix[8]
Tuberculosis = illness_matrix[9]

AnemiaSymptoms = np.zeros(shape=10, dtype=int, order='C')

count = 0
index = 0

for x in Anemia:
    
    if x == 1:
        AnemiaSymptoms[index] = count
        index = index + 1
        count = count + 1
    elif x == 0:
        count = count+1
        
        



