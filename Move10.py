"""
Move every letter in the provided string forward 10 letters through the alphabet.

If it goes past 'z', start again at 'a'.

Input will be a string with length > 0.
"""

def move_ten(st):
    string = [ord(x)+10 for x in st]
    for i in range(len(string)):
        if string[i] > 122:
            string[i] = 64+(string[i]-122)
    final = [chr(x).lower() for x in string]
    return ''.join(final)
