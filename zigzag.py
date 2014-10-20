#!/usr/bin/env python
# encoding: utf-8

"""
 The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

def convert(s, nRows):
    if nRows < 2:
        return s
    s = list(s)
    n = nRows
    res = []

    for i in range(n):
        li = s[i::2*n-2]
        #lii = []
        #for c in li:
        #    lii.append(c)
        #    lii.extend(list(' '*(n-2)))
        if 0 < i < n-1:
            tmp = s[2*n-2-i::2*n-2]

            for j in range(len(tmp)):
                li.insert(2*j+1, tmp[j])

            #for j, x in enumerate(tmp):
            #    lii[(n-1-i)+j*(n-1)] = x
        #res.append(''.join(lii).strip())
        res.append(''.join(li))
    #return '\n'.join(res)
    return ''.join(res)

