#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 03:44:18 2021

@author: wangyue
"""

def cube(x):
    """Returns the cube of x"""
    return 0  # <--- This obviously doesn't work correctly

def test_square():
    assert cube(0) == 0
    assert cube(2) == 8
    assert cube(-2) == -8