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





'''
from the collections module defaultdict a subclass of dictionary take in int, list, or a function as an argument called default factory it is based on this default_factory that the defaultdict will be used 
'''


from collections import defaultdict
sentence = "The red fox jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')
d = defaultdict(int)
for word in words:
    d[word] +=1
print(d) # output: defaultdict(<class 'int'>, {'The': 1, 'red': 1, 'fox': 1, 'jumped': 1, 'over': 1, 'the': 2, 'fence': 1, 'and': 1, 'ran': 1, 'to': 1, 'zoo': 1, 'for': 1, 'food': 1})

# the default_factory as a list

my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
        (345, 222.66), (678, 300.25), (1234, 35.67)]

dl = defaultdict(list)

for acct, amount in my_list:
    dl[acct].append(amount)
    
print(dl) # output: defaultdict(<class 'list'>, {1234: [100.23, 75.0, 35.67], 345: [10.45, 222.66], 678: [300.25]})

# lambda as default_factory:

animal = defaultdict(lambda:'Monkey')
animal['slow']= 'Snail'
animal['fast']= 'Tiger'
print(animal['tricky']) # output: Monkey
print(animal['jumpy']) # output: Monkey




'''
Deque pronounced deck is another method from the collections module to create an instance of deque it takes in a list
with deque you can append to the left rotate the list by indicating the number of elements you want to rotate
'''

from collections import deque
juices = ["apple", "banana", "cherry", "apple", "cherry", "lemon", "mango", "pawpaw", "berries", ]
deck = deque(juices)

deck.append('smoothie')
print(deck) # output: deque(['apple', 'banana', 'cherry', 'apple', 'cherry', 'lemon', 'mango', 'pawpaw', 'berries', 'smoothie'])
    
deck.appendleft('pepper')

print(deck) # output: deque(['apple', 'banana', 'cherry', 'apple', 'cherry', 'lemon', 'mango', 'pawpaw', 'berries', 'smoothie'])

deck.rotate(-1)

print(deck) # output: deque(['apple', 'banana', 'cherry', 'apple', 'cherry', 'lemon', 'mango', 'pawpaw', 'berries', 'smoothie', 'pepper'])

'''
We can also use deque to instruct our programme to keep a certain no of value in it list.

'''

def get_text(filename, n=5):
    try:
        with open(filename, 'r') as f:
            return deque(f, n)
    except OSError:
        print('Error opening file {}'.format(filename))
        raise

result = get_text('text.txt')
print(result) 
'''
output: deque(["Which, but their children's end, nought could remove,\n", "Is now the two hours' traffic of our stage;\n", 'The which if you with patient ears attend,\n', 'What here shall miss, our toil shall strive to mend.\n', 'SCENE I. Verona. A public place.'], maxlen=5)
'''

