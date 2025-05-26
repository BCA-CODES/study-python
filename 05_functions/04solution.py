import math

def circle(radius):
    area = math.pi * radius ** 2
    circum = 2 * math.pi * radius
    return area, circum

a, b = circle(5)
print("Area:" ,round(a,2), "Circumference:" ,round(b,2))