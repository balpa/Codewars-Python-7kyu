"""
There are some stones on Bob's table in a row, and each of them can be red, green or blue, indicated by the characters R, G, and B.

Help Bob find the minimum number of stones he needs to remove from the table so that the stones in each pair of adjacent stones have different colours.
"""

def solution(stones):
    arr = [x for x in stones]
    count = 0
    for x in range(len(arr)-1):
        if x+1 > len(arr):
            pass
        else:
            if arr[x] == arr[x+1]:
                count+=1
    return count
