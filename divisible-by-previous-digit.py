"""
Take a number and check each digit if it is divisible by the digit on its left checked and return an array of booleans.

The booleans should always start with false becase there is no digit before the first one.


"""

def divisible_by_last(n):
    arr = []
    digits = [int(x) for x in str(n)]
    for x in range(0,len(digits)-1):
        if digits[x] == 0:
            arr.append(False)
        elif digits[x+1] % digits[x] == 0:
            arr.append(True)  
        else:
            arr.append(False)
    arr.insert(0,False)
    return arr
