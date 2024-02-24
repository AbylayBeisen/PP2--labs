#ex1
from math import radians
a=int(input())
print(radians(a))
#ex2
a=int(input())
b=int(input())
c=int(input())
print(((b+c)/2)*a)
#ex3
import math 
numOfSides=int(input())
len=int(input())
pi=math.pi
area=(1/2)*(len*numOfSides)*(len/(2*math.tan(pi/numOfSides)))
print(int(area))
#ex4
import math 
len=int(input())
h=int(input())
area=h*len
print(float(area))