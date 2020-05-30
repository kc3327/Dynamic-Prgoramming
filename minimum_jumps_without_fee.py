#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:12:04 2020

@author: alun
"""
inputs=[1,1,3,6,9,3,0,1,3]
import math
def Minimum_jumps_without_fee_recursive(inputs):
    return solve_Minimum_jumps_without_fee_recursive(inputs,0)

def solve_Minimum_jumps_without_fee_recursive(inputs,current_index):
    if current_index >=len(inputs):
        return math.inf
    if current_index==len(inputs)-1:
        return 0
    if inputs[current_index]==0:
        return math.inf
    count1=math.inf
    for i in range(1,inputs[current_index]+1):
        count1=min(solve_Minimum_jumps_without_fee_recursive(inputs,current_index+i)+1,count1)
        
    return count1
    



#%% dp
import math


inputs=[2, 1, 0, 1, 4]
def Minimum_jumps_without_fee_dp(inputs):
    dp=[math.inf for x in range(len(inputs))]
    dp[0]=0

    for i in range(len(inputs)-1):
        for j in range(1,inputs[i]+1):
            if i+j <=len(inputs)-1:
                dp[i+j]=min(dp[i]+1,dp[i+j])
         
    return dp[-1]
#%%
