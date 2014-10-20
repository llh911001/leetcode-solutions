#!/usr/bin/env python
# encoding: utf-8

"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the". 
"""
def reverseWords(s):
    return ' '.join(s.strip().split()[::-1])

