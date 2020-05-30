#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:55:03 2020

@author: alun
"""

s1 = "abdca"
s2 = "cbda"
def Edit_Distance_recursive(s1,s2):
    return Solve_Edit_Distance_recursive(s1,s2,0,0)

def Solve_Edit_Distance_recursive(s1,s2,i1,i2):
    n1=len(s1)
    n2=len(s2)
    if i1==n1:
        return n2-i2
    
    if i2==n2:
        return n1-i1
    
    if s1[i1]==s2[i2]:
        return Solve_Edit_Distance_recursive(s1,s2,i1+1,i2+1)
    
    c1=1+Solve_Edit_Distance_recursive(s1, s2, i1+1, i2)#deletion, skip the deleted one in s1
    c2=1+Solve_Edit_Distance_recursive(s1, s2, i1, i2+1)#insertion, s1 does not have this one, check the next in s2
    c3=1+Solve_Edit_Distance_recursive(s1, s2, i1+1, i2+1)#substitute
    
    return min(c1,c2,c3)



#%% 

def Edit_Distance_dp(s1,s2):
    
    l1,l2=len(s1),len(s2)
    dp=[[0 for x in range(l1+1)] for y in range(l2+1)]
    
    for i in range(l1):
        dp[0][i]=i #s2是empty，s1 转到s2,需要一直delete
    for j in range(l2):
        dp[j][0]=j
    
    for i in range(1,l2+1):
        for j in range(1,l1+1):
            if s1[j-1]==s2[i-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
    return dp[-1][-1]


    
    
    
    
    
    
    
    
    
    