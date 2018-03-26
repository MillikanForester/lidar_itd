#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
******************************************************************************                                   *
*Laboratorio de Manejo Florestal                                             *
*Faculdade de Engenharia Florestal                                           *
*Universidade Federal de Mato Grosso                                         *
*Tree Match algorithm  based on Eysn et al. (2015)                           *
*Author: Pedro H. K. Millikan                                                *
******************************************************************************
"""

import pandas as pd
#to install pandas on windows run command 'py -3.6 -m pip install pandas',
#for python version 3.6
from math import sqrt
import os

#set result directory
os.chdir('C:/../itd_folder')

#field data sheet in .csv format
fld = pd.read_csv('reference_trees.csv', sep = ',' )

def distance(Xa,Ya,Xb,Yb): 
    '''calculates the euclidean distance'''
    d = sqrt((Xa-Xb)**2 + (Ya - Yb)**2)
    return d


def candidate_trees(reference_tree,test, search_radius):
    '''finds trees in a given search radius'''
    Xa = reference_tree['X']
    Ya = reference_tree['Y']
    Xa = list(Xa.values.flatten())
    Ya = list(Ya.values.flatten())
    r = search_radius    
    Xb = test['X']
    Yb = test['Y']
    Xb = list(Xb.values.flatten())
    Yb= list(Yb.values.flatten())
    matches = []
    for i in range(1,len(Xb)):
        d = (distance(Xa, Ya, Xb[i], Yb[i]))
        if d  <= r:
            matches.append(d)
        else:
            pass
    ''' work from here'''
    if len(matches) >= 0:   
        return matches
    else: 
        pass

def calculate(df_reference_trees, df_test_trees, search_radius):
    '''calculates all cadidate trees in a dataframe'''
    trees = []
    for i in range(1,len(df_reference_trees)):
        trees.append(candidate_trees(df_reference_trees.iloc[i:i + 1,:], df_test_trees,
        search_radius))
    TP = 0 #Match
    FP = 0 #Commission
    FN = 0 #Ommission
    for i in trees:
        if len(i) == 1:
            TP += 1
        elif len(i) >= 2 :
            FP += len(i) - 1 #Number of trees inside the search radius - 1 
        elif len(i) == 0:
            FN += 1
    #TP = TP + FP
    '''test statistics'''
    r = TP / (TP + FN) #Recall
    p = TP / (TP + FP) # precision
    F = 2 * (r * p )/(r + p) # F score
    print( ' Recall(r) : {}, Precision(p) :  {}, F score : {}'.format(r, p, F))
    return TP, FP, FN


'''Example:

calculate(field, trees_detected, 3)

- inputs:
1. field = .csv table of X and Y coordinates of field referenced trees
2. trees_detected = .csv table of trees predicted by ITD algorithms,
X and Y coordinates.
3. Search radius = radius search around reference trees. Try to use values similar
or smaller than spacing.

read this file in R:
install.package('reticulate') # allows python code to run in R
require('reticulate')

reticulate::py_run_file('C:/.../TreeMatching.py')

comments and contributions very welcome!

'''






 






