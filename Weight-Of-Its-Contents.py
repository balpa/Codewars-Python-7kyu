"""
Let's make a contentWeight function that takes in two parameters: bottleWeight and scale. This function will return the weight of the contents inside the bottle.

bottleWeight will be an integer representing the weight of the entire bottle (contents included).

scale will be a string that you will need to parse. It will tell you how the content weight compares to the weight of the bottle by itself. 
2 times larger, 6 times larger, and 15 times smaller would all be valid strings (smaller and larger are the only comparison words).
"""

def content_weight(bottle_weight, scale): 
    value = scale.split(" ")
    num = int(value[0])
    
    if value[2] == "larger":
        final = bottle_weight - (bottle_weight/(num+1))
        return final
    elif value[2] == "smaller":
        return bottle_weight/(num+1)
