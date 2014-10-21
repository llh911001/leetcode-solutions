#!/usr/bin/env python
# encoding: utf-8

def maxProduct(A):
    max_so_far = A[0]
    max_here = A[0]
    min_here = A[0]
    if len(A) == 0:
        return 0
    for i in range(1, len(A)):
        n = A[i]
        if n >= 0:
            max_here, min_here = max(max_here * n, n), min(min_here * n, 1)
        else:
            tmp = max_here
            max_here = max(min_here * n, n)
            min_here = min(tmp * n, n)

        if max_so_far < max_here:
            max_so_far = max_here

    return max_so_far

if __name__ == '__main__':
    print maxProduct([-2, 0, -1])
