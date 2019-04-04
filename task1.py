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
