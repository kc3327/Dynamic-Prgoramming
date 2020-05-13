#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 12:15:05 2020

@author: alun
"""

weights=[1, 3, 4, 5]
capacity=8
profits=[15, 50, 60, 90]



#%% Recursive
def unbounded_knapsak_recursive(weights,capacity,profits):
    return unbounded_knapsak_recur(weights,capacity,profits,0,)
## The difference between Unbounded Knapsack and 0/1 is unlimitted use of one item.

def unbounded_knapsak_recur(weights,capacity,profits,current_index):

    if capacity <0 or current_index>=len(profits):
        return 0
    profit1=0
    if weights[current_index]<=capacity:
        profit1=profits[current_index]+\
            unbounded_knapsak_recur(weights,\
                                    capacity-weights[current_index],profits,current_index)
    ## The only difference is current index does not increase by 1
    profit2=unbounded_knapsak_recur(weights,capacity,profits,current_index+1)
    return max(profit1,profit2)


unbounded_knapsak_recursive(weights,capacity,profits)



#%% 
def unbounded_knapsak_dp(weights,capacity,profits):
    dp=[[-1 for x in range(capacity+1)] for y in range(len(profits))]
    return unbounded_knapsak_dp_solve(weights,capacity,profits,dp)



def unbounded_knapsak_dp_solve(weights,capacity,profits,dp):
    for i in range(len(profits)):
        for j in range(capacity):
            if j==0:
                dp[i][j]=0
                
    
    for j in range(1,capacity+1):
        if j<weights[0]:
            dp[0][j]=0
        elif j % weights[0]==0:
            dp[0][j]= j//weights[0]*profits[0]
        else:
            dp[0][j]=dp[0][j-1]
    ## the first row setups
    for i in range(1,len(profits)):
        for j in range(1,capacity+1):
            if j<weights[i]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i][j-weights[i]]+profits[i],dp[i-1][j])
## only difference is dp[i-1][j-weights[i]], 无限使用不在乎用了几次，dp[i-1][j-weights[i]]肯定比dp[i][j-weights[i]]小
    return dp[-1][-1]



            
            
                
                
                
                
                
                
                
                
                