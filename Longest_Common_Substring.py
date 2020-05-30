#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 19:14:22 2020

@author: alun
"""
s1 = "abdca"
s2 = "cbda"
def Longest_Common_Substring_recursive(s1,s2):
    return Solve_Longest_Common_Substring_recursive(s1,s2,0,0,0)
def Solve_Longest_Common_Substring_recursive(s1,s2,i1,i2,count):
    if len(s1)==i1 or len(s2)==i2:
        return count
    if s1[i1]==s2[i2]:
        count=Solve_Longest_Common_Substring_recursive(s1,s2,i1+1,i2+1,count+1)
        
        
        
    c1 = Solve_Longest_Common_Substring_recursive(s1,s2,i1+1,i2,0)
    c2 = Solve_Longest_Common_Substring_recursive(s1,s2,i1,i2+1,0)
    
    return max(c1,c2,count)


#%% dp

def Longest_Common_Substring_dp(s1,s2):
    dp=[[0 for x in range(len(s1)+1)] for y in range(len(s2)+1)]

    temp=0 
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            if s1[j-1]==s2[i-1]:
                dp[i][j]=dp[i-1][j-1]+1
                temp=max(temp,dp[i][j])
    return dp