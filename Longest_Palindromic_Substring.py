#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 00:50:08 2020

@author: alun
"""
array="abdbca"
# array="cddpd"
def Longest_Palindromic_Substring_recursive(array):
    return solve_Longest_Palindromic_Substring_recursive(array,0,len(array)-1)

def solve_Longest_Palindromic_Substring_recursive(array,start_index,end_index):
    if start_index==end_index:
        return 1
    
    if start_index> end_index:
        return 0
    
    if array[start_index]==array[end_index]:
        if end_index-start_index-1==solve_Longest_Palindromic_Substring_recursive(array,start_index+1,end_index-1):
            return end_index-start_index+1
    case2=solve_Longest_Palindromic_Substring_recursive(array,start_index+1,end_index)
    case3=solve_Longest_Palindromic_Substring_recursive(array,start_index,end_index-1)
    
    return max(case2,case3)



#%% DP
def Longest_Palindromic_Substring_dp(array):
    l=len(array)
    dp=[[0 for x in range(l)] for y in range(l)]
    for i in range(l):
        dp[i][i]=1
    for start in range(l-2,-1,-1):
        for end in range(start+1,l):
            if array[start]==array[end] and dp[start+1][end-1]==(end-start-1):
                dp[start][end]=dp[start+1][end-1]+2
            else:
                dp[start][end]=max(dp[start+1][end],dp[start][end-1])
    return dp[0][-1]
    