import math
def Mean(a, b):
    q = (a * b) / 2
    w = math.sqrt(a * b)
    return(q, w)
a, b = Mean(1, 2)
print(a, b)