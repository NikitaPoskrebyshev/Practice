import math
p = math.acos(-1)
s, r1 = map(float, input().split())
p = math.pi
r2 = (((r1**2 * p) - s)/p)**0.5
print(round(r2, 3))