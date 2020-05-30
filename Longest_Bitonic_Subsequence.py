#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:57:39 2020

@author: alun
"""
# array=[4,2,3,6,10,1,12]
array=[4, 2, 5, 9, 7, 6, 10, 3, 1]
def Longest_Bitonic_Subsequence_dp(array):
    dp_increase=[1 for x in range(len(array))]
    dp_decrease=[1 for x in range(len(array))]
    
    for i in range(len(array)):
        for j in range(i):
            if array[i]>array[j]:
                dp_increase[i]=max(dp_increase[j]+1,dp_increase[i])
                     
                
    for i in range(len(array)-1,-1,-1):
        for j in range(len(array)-1,i,-1):
            if array[i]>array[j]:
                dp_decrease[i]=max(dp_decrease[j]+1,dp_decrease[i])
                
                
    temp_max=0            
    for i in range(len(array)):
        temp_max=max(temp_max,dp_decrease[i]+dp_increase[i]-1)
                
    return temp_max
    
