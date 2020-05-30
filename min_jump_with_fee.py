#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 20:44:03 2020

@author: alun
"""
#%% dp
import math
fee=[2,3,4,5]
# fee=[1,2,5,2,1,2]
def min_jump_with_fee(n,fee):
    dp=[[math.inf for x in range(n+1)] for y in range(3)]
    for i in range(3):
        dp[i][0]=0
        dp[i][1]=fee[0]
    for j in range(2,n+1):
        dp[0][j]=dp[0][j-1]+fee[j-1]
    for i in range(1,3):
        for j in range(2,n+1):
            if j<i+1:
                dp[i][j]=dp[i-1][j]
            else:
                for z in range(1,i+2):
                    dp[i][j]=min(dp[i][j],dp[i][j-z]+fee[j-z])
    return dp[-1][-1]


#%% recursive

def min_jump_with_fee_recursive(fee,n):
    return solve_min_jump_with_fee_recursive(fee,n,0)


def solve_min_jump_with_fee_recursive(fee,n,current_index):
    if current_index >= n:
        return 0
    
    fee1=solve_min_jump_with_fee_recursive(fee,n,current_index+1)
    fee2=solve_min_jump_with_fee_recursive(fee,n,current_index+2)
    fee3=solve_min_jump_with_fee_recursive(fee,n,current_index+3)
    
    return min(fee1,fee2,fee3)+fee[current_index]
    
#%% 1d dp


def min_jump_with_fee_dp(n,fee):
    dp=[math.inf for x in range(n+1)]
    dp[0]=0
    dp[1]=fee[0]
    dp[2]=fee[0]
    for i in range(3,n+1):
        dp[i]=min(dp[i-1]+fee[i-1],dp[i-2]+fee[i-2],dp[i-3]+fee[i-3])
        
        

    return dp[-1]

  