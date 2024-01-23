#ex1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#in
#ex2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
# print(fruits) will output {'cherry', 'orange', 'banana', 'apple'}
#ex3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
# print(fruits) will output {'banana', 'cherry', 'orange', 'apple', 'grapes', 'mango'}
#ex4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
# print(fruits) will output {'apple', 'cherry'}
#ex5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
# print(fruits) will output {'apple', 'cherry'}