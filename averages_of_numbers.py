def averages(arr):
    final = []
    j = 1
    if arr is None:
        return[]
    elif len(arr)<2:
        return[]
    else:
        for x in range(len(arr)-1):
            final.append((arr[x]+arr[j])/2)
            j += 1
    return final
