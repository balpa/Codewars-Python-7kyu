"""
that given an array arr, you have to return the amount of numbers that are smaller than arr[i] to the right.
"""

def equalize(arr):
    if arr == []:
        return []
    else:
        a = arr[0]
        final = list(map(lambda x : x-arr[0],arr))
        res = []
        for x in range(len(final)):
            if final[x] < 0:
                res.append(f"{final[x]}")
            else:
                res.append(f"+{final[x]}")
        return res
