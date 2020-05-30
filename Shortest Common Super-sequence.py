#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:46:31 2020

@author: alun
"""
# s1= "abcf"
# s2="bdcf"


s1,s2="dynamic", "programming"
import math
def Shortest_Common_Supersequence_dp(s1,s2):
    l1=len(s1)
    l2=len(s2)
    dp=[[math.inf for x in range(l1+1)] for y in range(l2+1)]
    
    
    for i in range(l1+1):
        dp[0][i]=i
    for j in range(l2+1):
        dp[j][0]=j
    for i in range(1,l2+1):
        for j in range(1,l1+1):
            if s1[j-1]==s2[i-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=1+min(dp[i-1][j],dp[i][j-1])
                
                
    return dp[-1][-1]
    