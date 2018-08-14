# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 21:16:01 2018

Problem: https://www.hackerrank.com/challenges/collections-counter/problem



@author: Shanshan
"""

import collections

num_of_shoes = int(input())  #1st line of input

sizes_in_stock = collections.Counter(map(int,input().split()))  #2rd line of input

total_revenue = 0

for _ in range(int(input())): 
    #3th line of input: customer num
    size, price = map(int,input().split())
    if sizes_in_stock[size]:
        total_revenue += price
        sizes_in_stock[size] -=1
print(total_revenue)