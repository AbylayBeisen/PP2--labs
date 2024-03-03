"""
#ex1
import math
x = [1, 2, 3]
print(math.prod(x))
#ex2
def count_upper_lower_builtin(string):
    z = sum(1 for c in string if c.isupper())
    t = sum(1 for c in string if c.islower())
    return z, t
string = input()
x, y = count_upper_lower_builtin(string)
print(x)
print(y)
#ex3
x = input()
y = list(x) == list(reversed(x))
if y:
    print("is palindrome")
else:
    print("not palindrome")
#ex4
import time
import math

def square_root(x, y):
    time.sleep(y/1000) 
    result = math.sqrt(x)
    return result

x = int(input())
y = int(input())

print(f"Square root of {x} after {y} milliseconds is {square_root(x, y)}")
"""
#ex5
x = (True, False, True)
y = (True, True, True)
print(all(x))
print(all(y))