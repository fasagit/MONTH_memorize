#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:01:45 2021

@author: sangin
"""

import random

MONTHS = ['January', 'February', 'March',
          'April', 'May', 'June',
          'July', 'August', 'September', 
          'October', 'November', 'December']

def generate_month_number():
    return random.randint(1,12)

def generate_month_literal():
    return MONTHS[random.randint(0, 11)]

def get_month_literal(month_number):
    return MONTHS[month_number - 1]


which_type = random.randint(1, 2)
n = generate_month_number()
if which_type ==1:
    print('what month?')
    print(n) 
    input('press any key to reveal answer')
    print(get_month_literal(n))
else:
    print('what\'s month number?')
    print(get_month_literal(n))
    input('press any key to reveal answer')
    print(n) 

# print(generate_month_number()) if which_type ==1 else print(generate_month_literal())

# input()

# print() if which_type ==1 else print(generate_month_literal())