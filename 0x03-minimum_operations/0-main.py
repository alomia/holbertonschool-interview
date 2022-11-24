#!/usr/bin/python3
"""
Main file for testing
"""

from sqlalchemy import false, true


minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 'Hola'
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = -20
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))


