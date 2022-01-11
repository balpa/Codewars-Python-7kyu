"""
I'm creating a scoreboard on my game website, but I want the score to be displayed as tally marks instead of Roman numerals. Write a function that translates the numeric score into tally marks.

My tally mark font uses the letters a, b, c, d, e to represent tally marks for 1, 2, 3, 4, 5, respectively. I want a space and line break ( ) after each completed tally (5).

Assume that the score you receive will be an integer. This function should return an HTML string that I can insert into my website that represents the correct score.
"""

def score_to_tally(score):
    dic = {"a":1,"b":2,"c":3,"d":4,"e":5}
    revdic = {0:"",1:"a",2:"b",3:"c",4:"d",5:"e"}
    list = []
    if score >= 5:
        return (f"{revdic[5]}"+" <br>")*(score//5)+ f"{revdic[score % 5]}"
    else:
        list.append(revdic[score])
    return list[0]
