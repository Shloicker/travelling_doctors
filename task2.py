# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 13:57:02 2019

@author: c1511993
"""
import doctor as dr

import random


def swapPositions(list1, list2, pos1, pos2):
    first_ele = list1.pop(pos1)
    second_ele = list2.pop(pos2)
    
    list1.insert(pos1, second_ele)
    list2.insert(pos2, first_ele)
    
 
def swapfunction():
    copysol = [[patient for patient in route] for route in dr.solution]
    i = random.sample(range(dr.n1), 2)
    firstdrpatient = random.randint(0, len(dr.solution[i[0]])-1)
    seconddrpatient = random.randint(0, len(dr.solution[i[1]])-1)


    swapPositions(copysol[i[0]], copysol[i[1]], firstdrpatient, seconddrpatient)

    return copysol
    

    


def movepatient():
    copysol = [[patient for patient in route] for route in dr.solution]
    copycopy = [[patient for patient in route] for route in dr.solution]
    
    doctorssubset = [route for route in dr.solution if len(route) < dr.m]
    doctor1 = random.choice(doctorssubset)  

    copycopy.remove(doctor1)
    doctor2 = random.choice(copycopy)

    patient = random.choice(doctor2)
    doctor2pos = dr.solution.index(doctor2)
    copysol[doctor2pos].remove(patient)

    position = random.choice(range(len(doctor1)))
    doctor1pos = dr.solution.index(doctor1)
    copysol[doctor1pos].insert(position, patient)
    return copysol


def solsearch(function, S):
    print(dr.cost(S, dr.D, dr.n1))
    for i in range(1000):
       # print("New step")
        #print(S)
        newsol = function()
        #print(S)
        #print(newsol)
        ogcost = dr.cost(S, dr.D, dr.n1)
        #print(ogcost)
        newcost = dr.cost(newsol, dr.D, dr.n1)
        #print(newcost)
        if newcost < ogcost:
            S = newsol
    print(dr.cost(S, dr.D, dr.n1))
    return S
    
print(solsearch(swapfunction, dr.solution))
        

    
    
    
    
    
    
    
    
    
