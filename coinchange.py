#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 15:36:40 2020

@author: alun
"""






denomination=[1,2,3]
total=11
#%% recursive
def coin_change_recursive(denomination,total):
    return coin_change_recursive_solve(denomination,total,0)


def coin_change_recursive_solve(denomination,total,current_index):
    if total==0:
        return 1
    if current_index>=len(denomination):
        return 0
    
    sum1,sum2=0,0
    if total>=denomination[current_index]:
        sum1=coin_change_recursive_solve(denomination,total-denomination[current_index],current_index)
    sum2=coin_change_recursive_solve(denomination,total,current_index+1)
    return sum1+sum2
    
coin_change_recursive(denomination,total)

#%% dp

def coin_change_dp(denomination,total):
    dp=[[0 for x in range(total+1)] for y in range(len(denomination))]
    
    for i in range(len(denomination)):
        dp[i][0]=0
    for j in range(total+1):
        if j % denomination[0]==0:
            dp[0][j]=1
    for i in range(1,len(denomination)):
        for j in range(1,total+1):
            if denomination[i]<j:
                dp[i][j]=dp[i-1][j]+dp[i][j-denomination[i]]+1
            else:
                dp[i][j]=dp[i-1][j]
    return dp[-1][-1]
coin_change_dp(denomination,total)               
        
        
        
