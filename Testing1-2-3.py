"""
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.
"""

def number(lines):
    final = []
    print(lines)
    if len(lines)<1:
        return []
    else:
        for x in range(0,len(lines)):
            a = lines[x].replace(lines[x], f"{x+1}: {lines[x]}")
            final.append(a)
    return final
