#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:28:15 2020

@author: alun
"""
# array="abdbca"
array="cddpd"
def Longest_Palindromic_Subsequence_Recursive(array):
    return Solve_Longest_Palindromic_Subsequence_Recursive(array,0,len(array)-1)

def Solve_Longest_Palindromic_Subsequence_Recursive(array,start_index,end_index):
    if start_index >end_index:
        return 0
    
    if start_index ==end_index:
        return 1
    
    if array[start_index]==array[end_index]:
        return 2+Solve_Longest_Palindromic_Subsequence_Recursive(array,start_index+1,end_index-1)
    else:
        case1=Solve_Longest_Palindromic_Subsequence_Recursive(array,start_index+1,end_index)
        case2=Solve_Longest_Palindromic_Subsequence_Recursive(array,start_index,end_index-1)
        return max(case1,case2)
    
    

#%% dp
array='abdbca'
def Longest_Palindromic_Subsequence_dp(array):
    dp=[[0 for x in range(len(array))] for y in range(len(array))]
    
    for i in range(len(array)):
        dp[i][i]=1
    # print(len(array)-1)
    for start in range(len(array)-2,-1,-1):
        # print(start)
        for end in range(start+1,len(array)):
            # print([start,end])
            if array[start]!= array[end]:
                dp[start][end]=max(dp[start+1][end],dp[start][end-1])
            else:
                dp[start][end]=2+dp[start+1][end-1]
    return dp[0][-1]
                
        
#%%%
for x in range(5,-1,-1):
    print(x)