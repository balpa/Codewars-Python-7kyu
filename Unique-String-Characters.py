"""
In this Kata, you will be given two strings a and b and your task will be to return the characters that are not common in the two strings.
"""

def solve(a,b):
    arra = [ x for x in a if x not in b]
    arrb = [ x for x in b if x not in a]
    final = arra+arrb
    return ''.join(final)
