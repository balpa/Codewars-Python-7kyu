"""
In this Kata, you will be given an array of integers whose elements have both a negative and a positive value, except for one integer that is either only negative or only positive. 
Your task will be to find that integer.
"""

def solve(arr):
    a = [x for x in arr if -x not in arr]
    return a[0]
