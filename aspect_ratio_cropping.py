from typing import Tuple
import math

def aspect_ratio(x: int, y: int) -> Tuple[int, int]:
    val = math.ceil((y*16)/9)
    return (val,y)
