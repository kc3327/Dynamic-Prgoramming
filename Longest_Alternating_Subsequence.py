#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 13:46:55 2020

@author: alun
"""
# array=[1, 3, 2, 4]
array=[1, 2, 3, 4]
def Longest_Alternating_Subsequence_Recursive(array):
    return max(solve_Longest_Alternating_Subsequence_Recursive(array,-1,0,True),solve_Longest_Alternating_Subsequence_Recursive(array,-1,0,False))

def solve_Longest_Alternating_Subsequence_Recursive(array,previous_index,current_index,isAscend):
    if len(array)==current_index:
        return 0
    
    
    c1=0
    if isAscend:
        if array[current_index]>array[previous_index]:
            c1=1+solve_Longest_Alternating_Subsequence_Recursive(array,current_index,current_index+1, not isAscend)
    else:
        if array[current_index]<array[previous_index]:
            c1=1+solve_Longest_Alternating_Subsequence_Recursive(array,current_index,current_index+1, not isAscend)
    c2=solve_Longest_Alternating_Subsequence_Recursive(array,previous_index,current_index+1, isAscend)
    
    return max(c1,c2)



#%%
def Longest_Alternating_Subsequence_dp(nums):
  n = len(nums)
  if n == 0:
    return 0
  # dp[0][i] = stores the LAS ending at 'i' such that the last two elements are in ascending order
  # dp[1][i] = stores the LAS ending at 'i' such that the last two elements are in descending order
  dp = [[1 for _ in range(n)] for _ in range(2)]
  
  for i in range(1,n):
      for j in range(i):
          if nums[i]>nums[j]:
              dp[0][i]=max(dp[1][j]+1,dp[0][i])
          else:
              dp[1][i]=max(dp[0][j]+1,dp[1][i])
              
  return max(max(dp[0]),max(dp[1]))
              
  