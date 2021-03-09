#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 03:42:55 2021

@author: wangyue
"""

def square(x):
    """Returns the square of x"""
    return x * x

def test_square():
    assert square(0) == 0
    assert square(2) == 4
    assert square(-2) == 4