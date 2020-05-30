#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 13:00:56 2020

@author: alun
"""

#%% recursive
money=[2, 5, 1, 3, 6, 2, 4]
def max_thief_recursive(money):
    return max_thief_recursive_solve(money,0)

def max_thief_recursive_solve(money,current_index):
    if current_index >= len(money):
        return 0
    
    
    stealth1=max_thief_recursive_solve(money,current_index+2)+money[current_index]
    stealth2=max_thief_recursive_solve(money,current_index+1)
    
    
    return max(stealth1,stealth2)


    
#%% dp
def max_thief_dp(money):
    dp=[0 for x in range(len(money))]
    
    dp[0]=money[0]
    dp[1]=money[1]
    dp[2]=money[0]+money[2]
    
    for i in range(3,len(money)):
        dp[i]=max(dp[i-2],dp[i-3])+money[i]
    return max(dp)