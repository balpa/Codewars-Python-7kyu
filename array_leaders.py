def array_leaders(numbers):
    arr = [x for x in numbers]
    ans = []
    c = 0
    for x in range(len(numbers)):
        sumarr = sum(arr) - arr[0]
        if arr[c] > sumarr:
            ans.append(arr[c])
        del arr[0]
    return ans
