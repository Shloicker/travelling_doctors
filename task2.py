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
    
 
def swapfunction(S):
    copysol = [[patient for patient in route] for route in S]
    i = random.sample(range(dr.n1), 2)
    firstdrpatient = random.randint(0, len(S[i[0]])-1)
    seconddrpatient = random.randint(0, len(S[i[1]])-1)


    swapPositions(copysol[i[0]], copysol[i[1]], firstdrpatient, seconddrpatient)

    return copysol
    

    


def movepatient(S):
    copysol = [[patient for patient in route] for route in S]
    copycopy = [[patient for patient in route] for route in S]
    
    doctorssubset = [[patient for patient in route] for route in S if len(route) < dr.m]
    doctor1 = random.choice(doctorssubset)  

    copycopy.remove(doctor1)
    doctor2 = random.choice(copycopy)

    patient = random.choice(doctor2)
    doctor2pos = S.index(doctor2)
    copysol[doctor2pos].remove(patient)

    position = random.choice(range(len(doctor1)))
    doctor1pos = S.index(doctor1)
    copysol[doctor1pos].insert(position, patient)
	
    return copysol


def solsearch(function, S, repetitions):
    copysol = [[patient for patient in route] for route in S]
    costs = [dr.cost(copysol, dr.D, dr.n1)]
    print("Original cost:\n", dr.cost(copysol, dr.D, dr.n1))
    for i in range(repetitions):
        newsol = function(copysol)
        ogcost = dr.cost(copysol, dr.D, dr.n1)
        newcost = dr.cost(newsol, dr.D, dr.n1)
        costs.append(newcost)
        if newcost < ogcost:
            copysol = newsol
    print("\n\nNew cost:\n", dr.cost(copysol, dr.D, dr.n1))
    return [copysol, costs]
