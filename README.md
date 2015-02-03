Roman.py
========

Roman Numeral Python Module

Adds Roman numeral functionality to Python.

Roman numerals can be instantiated by calling Roman(num) for some integer
    note: |num| must be less than 2,000,000

Roman numerals support the following operations:
    
    +, -, *, /, //, **, ==, <=, >=, <, >, !=


Integers may also be used as one of the operands.

Usage:

	>>> from roman import *
	>>> I
	Roman(1)
	>>> XXX
	Roman(30)
	>>> a = Roman(20)
	>>> a
	Roman(20)
	>>> print(a)
	XX
	>>> b = Roman(23)
	>>> print(a+b)
	XLIII
	>>> b + 45
	Roman(68)
	>>> a == b
	False




