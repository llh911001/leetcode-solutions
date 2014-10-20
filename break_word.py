#!/usr/bin/env python
# encoding: utf-8

"""
 Given a string s and a dictionary of words dict, determine if s can be
 segmented into a space-separated sequence of one or more dictionary words.

 For example, given
 s = "leetcode",
 dict = ["leet", "code"].

 Return true because "leetcode" can be segmented as "leet code".
"""

def break_word(s, d):
    n = len(s)
    a = [False for _ in range(n)]
    for i in range(n, -1, -1):
        if s[i:n] in d:
            a[i] = True
        else:
            for j in range(i+1, n):
                if s[i:j] in d and a[j]:
                    a[i] = True
                    break
    return a[0]

