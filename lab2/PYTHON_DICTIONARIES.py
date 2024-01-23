#ex1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
#ex2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"]=2020
#print(car) will output {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
#ex3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
#print(car) will output {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
#ex4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
#print(car) will output {'brand': 'Ford', 'year': 1964}
#ex5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
#print(car) will output {}