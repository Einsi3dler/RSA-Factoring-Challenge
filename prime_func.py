#!/usr/bin/python3
"""
This file contains RSA factorization
"""
def prime_factor(value):
    for num in range(2, value):
        res = value % num
        if res == 0:
            return(value/num, num)
        else:
            continue
