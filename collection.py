from collections import ChainMap

car_parts = {"hood": 500, "engine": 5000, "front_door": 750}
car_options = {"A/C": 1000, "Turbo": 2500, "rollbar": 300}
car_accessories = {"cover": 100, "hood_ornament": 150, "seat_cover": 99}
car_pricing = ChainMap(car_accessories, car_parts,car_options)

car_pricing['Turbo']=3500
car_pricing.pop('Turbo')
print(car_pricing) #output = ChainMap({'cover': 100, 'hood_ornament': 150, 'seat_cover': 99}, {'hood': 500, 'engine': 5000, 'front_door': 750}, {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300})


# The vars() function returns the __dict__ attribute of an object.
#The __dict__ attribute is a dictionary containing the object's changeable attributes.

age = 21
age = age.__str__
print(type(age)) #output = <class 'method-wrapper'>
num = age()
print(type(num)) # output = <class 'str'>

class Man:
    chest = 'Large'
    head = 'square'
    waist = 'small'
    
result = vars(Man)
print(result)

#The count() method returns the number of times a specified value appears in the string.
# Syntax: string.count(value, start, end)

text = 'The quick brown fox jumps over the lazy dog'
print(text.lower().count('the')) # output 2



# The collections module also provides us with a neat little tool that supports convenient and fast tallies. This tool is called Counter.

from collections import Counter

fruits = ["apple", "banana", "cherry", "apple", "cherry", "lemon", "mango", "pawpaw", "berries", ]
counter = Counter(fruits)

counter2 = Counter(["apple", "banana", "cherry", "berries", ])

print(Counter(fruits))  # output Counter({'apple': 2, 'cherry': 2, 'banana': 1, 'lemon': 1, 'mango': 1, 'pawpaw': 1, 'berries': 1})

print(counter['cherry'])  # output 2

print(list(counter.elements()))  # output ['apple', 'apple', 'banana', 'cherry', 'cherry', 'lemon', 'mango', 'pawpaw', 'berries

print(counter.most_common(3))  # output [('apple', 2), ('cherry', 2), ('banana', 1)]

print(counter.subtract(counter2)) # output: None

print(counter)# output: Counter({'apple': 1, 'cherry': 1, 'lemon': 1, 'mango': 1, 'pawpaw': 1, 'banana': 0, 'berries': 0})

