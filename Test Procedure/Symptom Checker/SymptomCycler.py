''' 

Test Script to Work Out Cycling Through Symptoms
Author: Mason Edgar 


'''



import numpy as np 
import itertools as iter

TestArray = np.ones(shape=10, dtype=int, order='C')
IndexArray = np.zeros(shape=10, dtype=int, order='C')

count = 0 
var = 9


# TestArray.shape[0] gets the size of the 1-D array 

for x in TestArray:
    IndexArray[count] = count 
    count = count + 1

    
    

NewTestArray = np.copy(TestArray)


'''
#------------------ STAGE 1 -------------------#

count = 0 

for x in NewTestArray:
    
    NewTestArray[IndexArray[count]] = 0  
    
    #------ IMPLEMENT ALGORITHM RIGHT HERE----#
    
    print(NewTestArray)
    
    #-----------------------------------------#
    
    
    
    #------- RESET FOR NEXT ITERATION --------# 
    
    NewTestArray[IndexArray[count]] = 1 
    count = count + 1
    
    #-----------------------------------------#
'''    

'''  
NewList = list(iter.combinations(IndexArray, 1))
    
    
count = 0 

for x in NewList:
    print(NewList[count][0])
    count = count + 1
'''    



stage = 1
count = 0 

NewList = list(iter.combinations(IndexArray, stage))   

'''
for x in NewList:
    NewTestArray[IndexArray[NewList[count][stage-1]]] = 0 
    print(NewTestArray)
    NewTestArray[IndexArray[NewList[count][stage-1]]] = 1
    count = count + 1
'''



'''
count = 0 
stage = 3

NewList = list(iter.combinations(IndexArray, stage)) 

for x in NewList:
    i = 0    
    while(i < stage):
        NewTestArray[IndexArray[NewList[count][i]]] = 0
        i = i + 1
    print(NewTestArray)
    i = 0    
    while(i < stage):
        NewTestArray[IndexArray[NewList[count][i]]] = 1
        i = i + 1
    count = count + 1
    
'''


 
stage = 1

while(stage <= TestArray.shape[0]):
    
    count = 0
    
    NewList = list(iter.combinations(IndexArray, stage)) 
    
    for x in NewList:
        i = 0    
        while(i < stage):
            NewTestArray[IndexArray[NewList[count][i]]] = 0
            i = i + 1
        print(NewTestArray)
        i = 0    
        while(i < stage):
            NewTestArray[IndexArray[NewList[count][i]]] = 1
            i = i + 1
        count = count + 1       
        
    stage = stage + 1
    print("")
    print("")