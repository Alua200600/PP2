#Task1
import math
degree = float(input())
radian = degree * (math.pi/180)
print(radian)

#Task2
height = int(input())
f1 = int(input())
f2 = int(input())
print(f"area : {(f1+f2)/2 * height}")

#Task3
n = int(input())
length = float(input())
area = (n*(length**2))/(4*math.tan(math.pi/n))
print(f"area of regular polygon:{area:.1f}")

#Task4
a = float(input())
b = float(input())
area = a*b
print(f"area of a parallelogram: {area:.1f}")