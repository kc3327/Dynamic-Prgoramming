#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 08:33:04 2020

@author: alun
"""
#%% bruto

def staircase_recursive(n):
    if n<0:
        return 0
    if n==1 or n==0:
        return 1
    return staircase_recursive(n-1)+staircase_recursive(n-2)+staircase_recursive(n-3)





#%% dp
steps=[1,2,3]
def staircase_dp(n,steps):
    dp=[[0 for x in range(n+1)] for y in range(3)]
    for j in range(n+1):
        dp[0][j]=1
    for i in range(3):
        dp[i][0]=1
    for i in range(1,3):
        for j in range(1,n+1):
            if steps[i]<=j:
                dp[i][j]=sum(dp[i][j-steps[i]:j])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[-1][-1]
    