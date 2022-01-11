"""
Input :: [10,20,25,0]

Output :: ["+0", "+10", "+15", "-10"]
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
