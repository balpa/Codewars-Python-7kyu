"""
Complete the function that returns a christmas tree of the given height. 
The height is passed through to the function and the function should return a list containing each line of the tree.
"""
def xMasTree(n):
    s,a = "#","_"
    k,c = n,1
    final = []
    for x in range(n):
        final.append(f"{(k-1)*a}{s*c}{(k-1)*a}")
        c += 2
        k -= 1
    final.append(f"{a*(int(n)-1)}{s}{a*(int(n)-1)}")
    final.append(f"{a*(int(n)-1)}{s}{a*(int(n)-1)}")
    return final
