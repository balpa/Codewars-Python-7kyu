"""
In this Kata your task will be to return the count of pairs that have consecutive numbers as follows:
"""

def pairs(ar):
    count = 0
    for x in range(0,len(ar)-1,2):
        if x > len(ar):
            break
        if abs(ar[x]-ar[x+1]) == 1:
            count += 1
    return count
