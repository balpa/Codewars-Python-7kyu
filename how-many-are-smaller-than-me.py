"""
that given an array arr, you have to return the amount of numbers that are smaller than arr[i] to the right.
"""

def smaller(arr):
    final = []
    for i in range(len(arr)):
        count = 0
        for x in range(i+1,len(arr)):
            if arr[x]< arr[i]:
                count += 1
        final.append(count)   
    return final
