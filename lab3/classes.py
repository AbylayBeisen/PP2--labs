#ex1
class Stringinput():
    def Get_string(self):
        return input("")
    def string_to_upper(self, s):
        print(s.upper())
string_get = Stringinput()
s = string_get.Get_string()
string_get.string_to_upper(s)
#ex2
class Shape():
    def __init__(self):
        self.area = 0

    def a(self):
        print("Area of the shape is {}".format(self.area))
class Square():
    def __init__(self, length):
        self.length = length

    def area(self):
        self.area = self.length ** 2
        print("Area of the square is {}".format(self.area))

square = Square(5)
square.area()
s = Shape()
s.a()
#ex3
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = self.length * self.width

    def a(self):
        print("Area of the rectangle is {}".format(self.area))
rectangle = Rectangle(5, 10)
rectangle.a()
#ex4
import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Point coordinates: ({}, {})".format(self.x, self.y))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx ** 2 + dy ** 2)
p1 = Point(3, 4)
p2 = Point(6, 8)
p1.show()
p1.move(1, 1)
p1.show()
print("Distance between p1 and p2 is {}".format(p1.dist(p2)))
#ex5
class Account():
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} has been deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} has been withdrawn. New balance: {self.balance}")
            else:
                print("Withdrawal amount exceeds available balance.")
        else:
            print("Withdrawal amount must be greater than 0.")

    def show_balance(self):
        print(f"Account owner: {self.owner}")
        print(f"Account balance: {self.balance}")
#ex6
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
prime_numbers = list(filter(lambda n: is_prime(n), numbers))
print(prime_numbers)