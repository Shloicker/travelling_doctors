# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:21:58 2019

@author: c1896292

Generating an initial solution 
"""

import random


#N = total num coords on map
#n1 = doctors home coordinates
#n2 = N-n1 = gives the number of patients


#numDoc = input("enter the number of Doctors:  ")
#numPatient = input("enter the number of patients:  ")









def createRoutes(n1, n2, m):
    
    sol = []
    S = [[] for i in range(n1)]
    patientList = []
    for i in range(n2): 
        patientList.append(i)
        
    while(len(patientList) > 0):
            rand1 = random.randint(0, len(patientList)-1)
            rand2 = random.randint(0, len(S)-1)
            if len(S[rand2]) == m:
                sol.append(S[rand2])
                S.pop(rand2)
                n1 = n1-1
            else:
                S[rand2].append(patientList[rand1])
                patientList.pop(rand1)
    
    for i in range (len(sol)):
        S.append(sol[i])
    return S                


def cost(S, D, n1):
    price = 0
    for i in range(n1):
        
        for j in range(0, len(S[i])+1):
            if j == 0:
                price += D[i][S[i][j]+n1]
                
            elif j>0 and j <= len(S[i])-1: 
                price+= D[n1+S[i][j]][n1+S[i][j-1]]
            else:
                price += D[n1+S[i][j-1]][i]
                
    return price
            


# Main Program: First ask the user to specify the input file.
filename = "p1.txt"

# Now read the input file line by line
with open(filename, "r") as f:
    
    # Read the first line of the file to get values for n1, n2, m (and N)
    line = f.readline().split()
    n1 = int(line[0])
    n2 = int(line[1])
    m = int(line[2])
    N = n1 + n2
    
    # Now define the arrays to hold the coordinates and the distances
    coords = [[0,0] for i in range(N)]
    D = [[0 for i in range(N)] for i in range(N)]
    
    # Now read in the coordinates
    for i in range(N):
        line = f.readline().split()
        coords[i][0] = float(line[0])
        coords[i][1] = float(line[1])
        
    # Finally read in the distance matrix
    for i in range(N):
        line = f.readline().split()
        for j in range(N):
            D[i][j] = float(line[j])

#print(filename + " has been read in correctly.")

# The next stage is to produce a solution S and evaluate it via a cost function
# creating routes


# test price .............................................................
            """
S = [ [3, 4, 9, 12],[5, 10, 6],[7, 11, 8] ]

for i in range (len(S)):
    for j in range (len(S[i])):
        S[i][j] = S [i][j]-3

ans= D[0][3] +  D[3][4] + D[4][9]+ D[9][12]+ D[12][0]+     D[1][5]+ D[5][10]+ D[10][6]+ D[6][1]+    D[2][7]+  D[7][11]+  D[11][8]+  D[8][2]

answer = cost(S, D, n1)
print(ans)
print(answer)

"""
   
"""
print("n1      = " + str(n1))
print("n2      = " + str(n2))
print("m       = " + str(m))

# The following lines are for testing purposes and can be deleted
print("n1      = " + str(n1))
print("n2      = " + str(n2))
print("m       = " + str(m))
#print("coords  = " + str(coords))
#print()

#for i in range(len(D)):
#    print(D[i])

#print("S       = " + str(S))
#print("cost(S) = " + str(cost(S, D)))
"""

