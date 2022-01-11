"""
Given two arrays of strings, return the number of times each string of the second array appears in the first array.
"""

def solve(a,b):
    final = []
    for x in range(len(b)):
        final.append(a.count(b[x]))
    return final
