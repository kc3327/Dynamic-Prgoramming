#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 07:32:03 2020

@author: alun
"""

def Fib(n):
    if n==1:
        return 1
    if n==0:
        return 0
    return Fib(n-1)+Fib(n-2)

#%% Top-down with Memorization

def Fib_with_memo(n):
    dp=[-1 for x in range(n+1)]
    dp[0]=0
    dp[1]=1
    return Fib_with_memo_solve(dp,n)

def Fib_with_memo_solve(dp,n):
    if n==1:
        return dp[1]
    if n==0:
        return dp[0]
    if dp[n]!=-1:
        return dp[n]
    
    dp[n]=Fib_with_memo_solve(dp,n-1)+Fib_with_memo_solve(dp,n-2)
    return dp[n]
    



#%% DP

def Fib_dp(n):
    dp=[-1 for x in range(n+1)]
    dp[0]=0
    dp[1]=1
    for i in range(2,len(dp)):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[-1]
    
    
