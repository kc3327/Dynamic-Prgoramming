#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:40:09 2020

@author: alun
"""
numbers=[4,2,3,6,10,1,12]
def Longest_Increasing_Subsequence_Recursive(numbers):
    return Solve_Longest_Increasing_Subsequence_Recursive(numbers,0,-1)


def Solve_Longest_Increasing_Subsequence_Recursive(numbers,current_index,previous_index):
    if current_index>=len(numbers):
        return 0
    c1 = 0
    if previous_index == -1 or numbers[current_index] > numbers[previous_index]:
        c1 = 1 + Solve_Longest_Increasing_Subsequence_Recursive(numbers, current_index + 1, current_index)

    # excluding the number at currentIndex
    c2 = Solve_Longest_Increasing_Subsequence_Recursive(numbers, current_index + 1, previous_index)

    return max(c1, c2)



#%%
numbers=[-4, 10, 3, 7, 15]
def Longest_Increasing_Subsequence_dp(numbers):
    dp=[1 for x in range(len(numbers))]
    for i in range(1,len(numbers)):
        for j in range(i):
            
            if numbers[i]>numbers[j] and dp[i]<=dp[j]:
                dp[i]=dp[j]+1

    return dp[-1]
    

    
    