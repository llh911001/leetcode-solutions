#!/usr/bin/env python
# encoding: utf-8

"""
 Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

"""

def evalRPN(tokens):
    # better to map these opraters to a proper lambda function
    opr = ['+', '-', '*', '/']
    tmp = []
    for t in tokens:
        if t in opr:
            a, b = int(tmp[1]), int(tmp[0])
            if t == '+':
                res = a + b
            elif t == '-':
                res = a - b
            elif t == '/':
                res = int(float(a) / b)
            elif t == '*':
                res = a * b
            tmp = tmp[2:]
            tmp.insert(0, res)
        else:
            tmp.insert(0, int(t))
    return int(tmp[0])

