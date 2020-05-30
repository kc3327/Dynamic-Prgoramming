#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 15:11:19 2020

@author: alun
"""
lengths=[1, 2, 3, 4, 5]  
prices=[2, 6, 7, 10, 13]  
rod_length= 5 


#%% recursive
def rodcut_recursive(weights,capacity,profits):
    return rodcut_recur(weights,capacity,profits,0,)
## The difference between Unbounded Knapsack and 0/1 is unlimitted use of one item.

def rodcut_recur(weights,capacity,profits,current_index):

    if capacity <0 or current_index>=len(profits):
        return 0
    profit1=0
    if weights[current_index]<=capacity:
        profit1=profits[current_index]+\
            rodcut_recur(weights,\
                                    capacity-weights[current_index],profits,current_index)
    ## The only difference is current index does not increase by 1
    profit2=rodcut_recur(weights,capacity,profits,current_index+1)
    return max(profit1,profit2)


rodcut_recursive(lengths,rod_length,prices)


#%%
##The same as Unbounded Kanpsack