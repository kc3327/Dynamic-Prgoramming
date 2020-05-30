#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:10:40 2020

@author: alun
"""


array="cddpd"
def Palindromic_Partitioning(array):
    l=len(array)
    
    dp=[[False for x in range(l)] for y in range(l)]
    
    for i in range(l):
        dp[i][i]=True
    
    for start in range(l-2,-1,-1):
        for end in range(start+1,l):
            if array[start]==array[end]:
                if end-start==1 or dp[start+1][end-1]:
                    dp[start][end]=True
    cuts = [0 for _ in range(l)]
    for startIndex in range(l-1, -1, -1):
      minCuts = l  # maximum cuts
      for endIndex in range(l-1, startIndex-1, -1):
        if dp[startIndex][endIndex]:
          # we can cut here as we got a palindrome
          # also we don't need any cut if the whole substring is a palindrome
          minCuts = 0 if endIndex == l-1 else min(minCuts, 1 + cuts[endIndex + 1])
    
      cuts[startIndex] = minCuts
    
    return cuts               
