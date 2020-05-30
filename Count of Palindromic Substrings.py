#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 00:50:05 2020

@author: alun
"""

#%% DP
import numpy

array="cddpd"
def Count_Palindromic_Substring_dp(array):
    l=len(array)
    dp=[[0 for x in range(l)] for y in range(l)]
    for i in range(l):
        dp[i][i]=1
    for start in range(l-2,-1,-1):
        for end in range(start+1,l):
            if array[start]==array[end] and dp[start+1][end-1]==(end-start-1):
                dp[start][end]=dp[start+1][end-1]+2
            else:
                dp[start][end]=max(dp[start+1][end],dp[start][end-1])
    dp_TF=[[False for x in range(l)] for y in range(l)]
    for i in range(l):
        dp_TF[i][i]=True
    
    for start in range(l-1,-1,-1):
        for end in range(start+1,l):
            if dp[start][end]==end-start+1:
                dp_TF[start][end]=True
                
    return numpy.count_nonzero(dp_TF)