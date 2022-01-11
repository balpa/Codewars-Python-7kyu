"""
Write a function cubeSum(n, m) that will calculate a sum of cubes of numbers in a given range, starting from the smaller (but not including it) to the larger (including). The first argument is not necessarily the larger number.

If both numbers are the same, then the range is empty and the result should be 0.
"""

def cube_sum(n, m):
    arr = []
    arr.append(n)
    arr.append(m)
    arr.sort()
    count = 0
    if arr[0] == arr[1]:
        return 0
    else:
        for x in range(arr[0]+1,arr[1]+1):
            count += x**3
    return count
