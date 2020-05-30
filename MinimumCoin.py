#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:05:45 2020

@author: alun
"""
denomination=[1,2,3]
total=7
#%%
def Minimum_Coin_Change_dp(denomination,total):
    dp=[[0 for x in range(total+1)] for y in range(len(denomination))]
    
    for i in range(len(denomination)):
        dp[i][0]=0
    for j in range(total+1):
        if j % denomination[0]==0:
            dp[0][j]=j//denomination[0]
    for i in range(1,len(denomination)):
        for j in range(1,total+1):
            if denomination[i]<=j:
                dp[i][j]=min(dp[i-1][j],dp[i][j-denomination[i]]+1)
            else:
                dp[i][j]=dp[i-1][j]
    return dp[-1][-1]
Minimum_Coin_Change_dp(denomination,total)  

    