#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 13:48:34 2020

@author: alun
"""
nums=[4, 1, 2, 6, 10, 1, 12]
def Maximum_Sum_Increasing_Subsequence(nums):
  n = len(nums)
  dp = nums.copy()
  dp[0] = nums[0]

  maxSum = nums[0]
  for i in range(1, n):
    for j in range(i):
      if nums[i] > nums[j] and dp[i] < dp[j] + nums[i]:
        dp[i] = dp[j] + nums[i]

    maxSum = max(maxSum, dp[i])

  return maxSum