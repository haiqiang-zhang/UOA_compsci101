"""
Name: Haiqiang Zhang
Username: hzha556
ID number: 237994789
Description: Q1   A program that implements the above approximation of pi.
"""
import math
golden_ratio = (1 + math.sqrt(5))/2
pi = ((802*golden_ratio-801)/(602*golden_ratio-601))**4
print("Pi is equivalent to", round(pi, 7))
