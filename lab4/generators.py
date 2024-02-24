#ex1
class MyNums:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a*self.a
        self.a += 1
        return x
    
mynums = MyNums()
N=int(input())
myiter = iter(mynums)

for i in range(N):
    print(next(myiter))
#ex2
def even_numbers_generator(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i
n = int(input( ))
even_nums = even_numbers_generator(n)
print(end='')
print(*even_nums, sep=', ')   
#ex3
class MyNums:
    def __iter__(self):
        self.a = 12
        return self

    def __next__(self):
        x = self.a
        self.a += 12
        return x
    
mynums = MyNums()
N=int(input())
myiter = iter(mynums)
nums=[]
for i in range(0,N//12):
    nums.append(str(next(myiter)))
print(", ".join(nums))
#ex4
def squares(a, b):
    for num in range(a, b+1):
        yield num**2

a = int(input())
b = int(input())
for square in squares(a, b):
    print(square)
#ex5
def myRange(start, stop):
    while start > stop:
        yield start
        start -= 1
n=int(input())
print(list(myRange(n,0)))