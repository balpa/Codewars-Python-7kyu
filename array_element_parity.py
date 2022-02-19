def solve(arr):
    for x in range(len(arr)):
        if arr[x]*-1 in arr:
            pass
        else:
            return arr[x]
