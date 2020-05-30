#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 16:43:39 2020

@author: alun
"""
numbers="tomorrow"
def Longest_Repeating_Subsequence(numbers):
  n = len(numbers)
  dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
  maxLength = 0
  # dp[i1][i2] will be storing the LRS up to numbers[0..i1-1][0..i2-1]
  # this also means that subsequences of length zero(first row and column of
  # dp[][]), will always have LRS of size zero.
  for i1 in range(1, n+1):
    for i2 in range(1, n+1):
      if i1 != i2 and numbers[i1 - 1] == numbers[i2 - 1]:
        dp[i1][i2] = 1 + dp[i1 - 1][i2 - 1]
      else:
        dp[i1][i2] = max(dp[i1 - 1][i2], dp[i1][i2 - 1])

      maxLength = max(maxLength, dp[i1][i2])

  return maxLength