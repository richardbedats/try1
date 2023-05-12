#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 18:50:49 2023

@author: richardbedats
"""

# =========================
# Printing using f-strings
# =========================
# Video lecture: https://youtu.be/W3aIcrQX3Zo 
    
# F-strings provide a way to embed expressions inside string literals, using 
# a minimal syntax. It should be noted that an f-string is really an expression 
# evaluated at run time, not a constant value. In Python source code, an f-string 
# is a literal string, prefixed with 'f', which contains expressions inside 
# braces. The expressions are replaced with their values.
# Source: https://www.python.org/dev/peps/pep-0498/

print('hello!')
a = f'{1+2}'
a

type(a)

print(a)

print(f'{1+2}')
type(f'{1+2}')

print(f'1+2 is {1+2}.')


fname  = 'steve'
f'My first name is {fname}.'

type(f'My name is {fname}.')
print(f'My name is {fname}.')

fname = 'mary'


a = 1/3
a
print(a)

print(f'{a: .4f}')      # 4 digits float

print(f'{7.37654:.2f}')


lname = 'johnson'
annual_salary = 111_133         # underscore can be used instead of comma, easier to read
print(f'My name is {fname} {lname} and my monthly salary is ${annual_salary/12:.2f}.')
