#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 15:44:31 2020

@author: alun
"""
# s1="abdca"
# s2="cbda"

s1="passport"
s2="ppsspt"

def Longest_Common_Subsequence_recursive(s1,s2):
    return solve_Longest_Common_Subsequence_recursive(s1,s2,0,0)


def solve_Longest_Common_Subsequence_recursive(s1,s2,i1,i2):
    if i1>=len(s1) or i2 >=len(s2):
        return 0
    if s1[i1]==s2[i2]:
        return 1+solve_Longest_Common_Subsequence_recursive(s1,s2,i1+1,i2+1)
    case1=solve_Longest_Common_Subsequence_recursive(s1,s2,i1+1,i2)
    case2=solve_Longest_Common_Subsequence_recursive(s1,s2,i1,i2+1)
    
    return max(case1,case2)




#%% DP

def Longest_Common_Subsequence_dp(s1,s2):
    l1=len(s1)
    l2=len(s2)
    dp=[[0 for x in range(l1+1)] for y in range(l2+1)]
    temp=0
    for i in range(1,l2+1):
        for j in range(1,l1+1):
            if s1[j-1]==s2[i-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
            temp=max(temp,dp[i][j])
    return dp