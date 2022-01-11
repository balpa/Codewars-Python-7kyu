"""
The function must return the truncated version of the given string up to the given limit followed by "..." if the result is shorter than the original. 
Return the same string if nothing was truncated.
"""

def solution(st, limit): 
    return f"{st[0:limit]}..." if limit<len(st) else st
