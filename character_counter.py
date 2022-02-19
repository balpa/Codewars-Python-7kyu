def validate_word(word):
    word = word.lower()
    arr = []
    use = list(set(word))
    
    for x in range(len(use)):
        arr.append(word.count(use[x]))
    
    for x in range(len(arr)-1):
        if arr[x] != arr[x+1]:
            return False
    return True
