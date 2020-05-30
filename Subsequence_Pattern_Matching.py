#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:53:56 2020

@author: alun
"""



string,pattern="tomorrow", "tor"
def Subsequence_Pattern_Matching_recursieve(string,pattern):
    return solve_Subsequence_Pattern_Matching_recursieve(string,pattern,0,0)


def solve_Subsequence_Pattern_Matching_recursieve(string,pattern, string_index,pattern_index):
    if pattern_index==len(pattern):
        return 1
    if string_index==len(string):
        return 0
    c1=0
    if string[string_index]==pattern[pattern_index]:
        c1=solve_Subsequence_Pattern_Matching_recursieve(string,pattern,string_index+1,pattern_index+1)
    c2=solve_Subsequence_Pattern_Matching_recursieve(string,pattern,string_index+1,pattern_index)
    
    return c1+c2



    
#%%    
    
def Subsequence_Pattern_Matching_dp(string,pattern):
    dp=[[0 for x in range(len(string)+1)] for y in range(len(pattern)+1)]
    for i in range(len(string)+1):
        dp[0][i]=1
        
    for i in range(1,len(pattern)+1):
        for j in range(1,len(string)+1):
            if pattern[i-1]==string[j-1]:
                dp[i][j]=dp[i-1][j-1]+dp[i][j-1]
            else:
                dp[i][j]=dp[i][j-1]
                
    return dp[-1][-1]