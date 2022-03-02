def get_larger_numbers(a, b):
    final = []
    
    for x in range(len(a)):
        if a[x] > b[x]:
            final.append(a[x])
        else:
            final.append(b[x])
    return final
