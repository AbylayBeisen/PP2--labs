#ex1
import re
x = str(input())
y = re.search('^a(b*)$', x)
if y:
    print(x)
else:
    print("")
#ex2
import re
x = str(input())
y = re.search('^a(bb|bbb)$', x)
if y:
    print(x)
else:
    print("")
#ex3
import re
x = str(input())
y = re.findall('[a-z]+_[a-z]+', x)
if y:
    print(x)
else:
    print("")
#ex4
import re
x = str(input())
y = re.findall('[A-Z][a-z]+', x)
if y:
    print(x)
else:
    print("")
#ex5
import re
y = str(input())
x = re.search("a.*b$", y)
if x:
    print(y)
else:
    print("")
#ex6
import re
x = str(input())
y = re.sub('[ ,.]', ':', x)
print(y)
#ex7
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    camel_str = components[0] + ''.join(x.title() for x in components[1:])
    return camel_str
x = str(input())
y = snake_to_camel(x)
print(y)
#ex8
def split_up(x):
    y = [x[0]]
    for char in x[1:]:
        if char.isupper():
            y.append(char)
        else:
            y[-1] += char
    return y
x = str(input())
y = split_up(x)
print(y)
#ex9
def insert_spaces(x):
    y = ' '
    for char in x:
        if char.isupper() and y and not y.endswith(' '):
            y += ' '
        y += char
    return y
x = str(input())
y = insert_spaces(x)
print(y)
#ex10
def camel_to_snake(x):
    y = ' '
    for char in x:
        if char.isupper():
            y += '_' + char.lower()
        else:
            y += char
    return y.lstrip('_')
x = str(input())
y = camel_to_snake(x)
print(y)