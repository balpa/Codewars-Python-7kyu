
"""
In this Kata, we are going to reverse a string while maintaining the spaces (if any) in their original place.
"""

def solve(s):
    string = [x for x in s]
    count = []
    for x in range(len(string)):
        if string[x] == " ":
            count.append(x)        
    reversed = [x for x in string if x != " "]
    reversed.reverse() 
    for x in range(len(count)):
        reversed.insert(count[x]," ")
    return ''.join(reversed)
