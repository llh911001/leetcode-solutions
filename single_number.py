#!/usr/bin/env python
# encoding: utf-8

"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

def singleNumber(A):
    n = 0
    for i in A:
        n ^= i
    return n
