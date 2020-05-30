#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:41:09 2020

@author: alun
"""

#%%
import math


def count_ribbon_pieces(ribbonLengths, total):
  maxPieces = count_ribbon_pieces_recursive(ribbonLengths, total, 0)
  return -1 if maxPieces == -math.inf else maxPieces


def count_ribbon_pieces_recursive(ribbonLengths, total, currentIndex):
  # base check
  if total == 0:
    return 0

  n = len(ribbonLengths)
  if n == 0 or currentIndex >= n:
    return -math.inf

  # recursive call after selecting the ribbon length at the currentIndex
  # if the ribbon length at the currentIndex exceeds the total, we shouldn't process this
  c1 = -math.inf
  if ribbonLengths[currentIndex] <= total:
    result = count_ribbon_pieces_recursive(
      ribbonLengths, total - ribbonLengths[currentIndex], currentIndex)
    if result != -math.inf:
      c1 = result + 1

  # recursive call after excluding the ribbon length at the currentIndex
  c2 = count_ribbon_pieces_recursive(ribbonLengths, total, currentIndex + 1)
  return max(c1, c2)


def main():
   print(count_ribbon_pieces([2, 3, 5], 5))
   print(count_ribbon_pieces([2, 3], 7))
   print(count_ribbon_pieces([3, 5, 7], 13))
   print(count_ribbon_pieces([3, 5], 7))


main()
#%% dp

total=7
denomination=[3,5]
def Max_Ribben_Cut_dp(denomination,total):
    dp=[[math.inf for x in range(total+1)] for y in range(len(denomination))]
    
    for i in range(len(denomination)):
        dp[i][0]=0
    for j in range(total+1):
        if j % denomination[0]==0:
            dp[0][j]=j//denomination[0]
    for i in range(1,len(denomination)):
        for j in range(1,total+1):
            if denomination[i]<=j and dp[i][j-denomination[i]] !=math.inf:
                dp[i][j]=max(dp[i-1][j],dp[i][j-denomination[i]]+1)
            else:
                dp[i][j]=dp[i-1][j]
    return -1 if dp[-1][-1]==math.inf else dp[-1][-1]
Max_Ribben_Cut_dp(denomination,total)  


