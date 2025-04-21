

name = 'Nina'
age = 12

print(name)
print(age)
print(f'Hello {name}, you are {age} years old.')

print(type(name))
print(type(name) == str)
print(isinstance(name, str))
print(isinstance(age, float))


# if condition else value
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

# ternary operator is basically a if-else statement in a single line  
def is_adult2(age):
    return "Adult" if age >= 18 else "Minor"

is_adult(18)
is_adult2(1)

# concatenating strings w/ plus operator
name = "Nina"
phrase = "Hello " + name
print(phrase)

# concatenating w/ plus equal (+=) operator
name += " Banana"
print(name)

# string methods
# is_alpha() # checks if a string contains only characters and is not empty
# is_digit() # checks if a string contains only numbers and is not empty
# is_alnum() # checks if a string contains only characters and numbers and is not empty
# is__decimal() # checks if a string contains only digits and is not empty
# is_space() # checks if a string contains only spaces and is not empty
# is_title() # checks if a string is in title case
# is_lower() # checks if a string is in lower case
# is_upper() # checks if a string is in upper case
# is_numeric() # checks if a string contains only numbers and is not empty
# lower() # converts a string to lower case
# upper() # converts a string to upper case
# title() # converts a string to title case
# split() # splits a string into a list of strings on a specified separator
# join() # joins a list of strings into a single string
# strip() # removes leading and trailing spaces from a string, to trim a string
# startswith() # checks if a string starts with a given string
# endswith() # checks if a string ends with a given string
# find() # finds the first occurrence of a given string in a string
# replace() # replaces a given string with another string
# count() # counts the number of occurrences of a given string in a string

name = "Ni\'na" # Ni\na
print(name)

name = "Ni\na" # Ni
print(name)     # a

name = "Ni\\'na" # Ni\'na
print(name)

name = "Ni\'na" # Ni'na
print(name)

# String characters & slicing
name = "Nina"
print(name[0]) # N
print(name[1]) # i
print(name[2]) # n
print(name[3]) # a
print(name[-1]) # a

print(name[0:2]) # Ni
print(name[1:4]) # ina

# bolean
book1 = True
book2 = False
read_any = any([book1, book2])
print(read_any) # True
read_all = all([book1, book2])
print(read_all) # False

# update a object in a list
books = ["book1", "book2", "book3"]
books[0] = "book4"
print(books) # ['book4', 'book2', 'book3']
# add a object to a list
books.append("book5")
print(books) # ['book4', 'book2', 'book3', 'book5']
# remove a object from a list
books.remove("book2")
print(books) # ['book4', 'book3', 'book5']
# add a object to a list
books.insert(1, "book6")
print(books) # ['book4', 'book6', 'book3', 'book5']
# remove a object from a list
books.pop(1) # remove the object at index 1, if not specified, it will remove the last object
print(books) # ['book4', 'book3', 'book5']
# add a object to a list
books.extend(["book6", "book7"]) # need to be a list
print(books) # ['book4', 'book3', 'book5', 'book6', 'book7']
# remove a object from a list
books.clear()
print(books) # []

# dictionary
dog = {'name': ['Tapioca', 'Black', 'Nina'], 'age': [18, 16, 12]}
print(dog['name']) # ['Tapioca', 'Black', 'Nina']

print(dog.get('name')) # ['Tapioca', 'Black', 'Nina']
print(dog.get('name')[0]) # Tapioca
print(dog.get('color')) # None
print(dog.get('color', 'No color')) # No color

dog['color'] = ['Black and White', 'Black', 'Yellow']
print(dog) # {'name': ['Tapioca', 'Black', 'Nina'], 'age': [18, 16, 12], 'color': ['Black and White', 'Black', 'Yellow']}

# iterate over a dictionary
for key, value in dog.items():
    print(f'{key}[0]: {value[0]}') 
    
# iterate over a dictionary
for key, value in dog.items():
    print(f'{key}: {value}') 
    
print(dog.pop('color')) # ['Black and White', 'Black', 'Yellow']
print(dog) # {'name': ['Tapioca', 'Black', 'Nina'], 'age': [18, 16, 12]}

dog['color'] = ['Black and White', 'Black', 'Yellow']
print(dog) # {'name': ['Tapioca', 'Black', 'Nina'], 'age': [18, 16, 12], 'color': ['Black and White', 'Black', 'Yellow']}
print(list(dog.values())) # ('color', ['Black and White', 'Black', 'Yellow'])
print(list(dog.keys())) # ['name', 'age', 'color']
print(list(dog.items())) # [('name', ['Tapioca', 'Black', 'Nina']), ('age', [18, 16, 12]), ('color', ['Black and White', 'Black', 'Yellow'])]
print(dog.keys()) # dict_keys(['name', 'age', 'color'])
print(len(dog)) # 3 


# while loop # should be use if precaution to not interaction forever
i = 0
while i <= 10:
    #print(i)
    print(f'Hello {i}')
    i += 2
print("End of while loop")

# for loop
items = [1, 2, 3, 4, 5]
for i in items:
    print(i)

# for loop with range
items = range(1, 10)
for i in items:
    if i % 2 == 0:
        print(i)
        
items = [1, 2, 3, 4, 5]
for i in items:
    print(i * 2)
    
# for loop with enumerate
items = ['a', 'b', 'c', 'd']
for i, item in enumerate(items):
    print(i, item)
    
# for loop with continue
items = ['a', 'b', 'c', 'd']
for i in items:
    if i == 'b':
        continue
    print(i)
    
# for loop with break
items = ['a', 'b', 'c', 'd']
for i in items:
    if i == 'c':
        break
    print(i)

# for loop with else
items = ['a', 'b', 'c', 'd']
for i in items:
    print(i)
else:
    print("End of for loop")

# lambda function
add = lambda x, y: x + y
print(add(2, 3)) # 5

mul = lambda x, y: x ** y
print(mul(2, 5)) # 32

# map(), filter(), reduce()
#1. map # applies a function to all items in an input list
def square(x):
    return x ** 2

#2. the same as the above function using lambda
square = lambda x: x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers)) # we need to convert the map object to a list to see the result
print(squared_numbers) # [1, 4, 9, 16, 25]

#3. here is where the lambda function shynes and simplifies the code
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers)) # we need to convert the map object to a list to see the result
print(squared_numbers) # [1, 4, 9, 16, 25]


#1. filter # creates a list of elements for which a function returns true, or a filter object 
def is_even(x):
    return x % 2 == 0

#2 the same as the above function using lambda
is_even = lambda x: x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(is_even, numbers)) # we need to convert the filter object to a list to see the result
print(even_numbers) # [2, 4]

#3. here is where the lambda function shynes and simplifies the code
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0))
print(even_numbers) # [2, 4]
#

# reduce # applies a rolling computation to sequential pairs of values in a list
from functools import reduce
expense = [('Dinner', 80), ('Car Rental', 200), ('Hotel', 300)]
sum = 0

for item in expense:
    sum += item[1]
print(sum) # 580

# the same as the above function using lambda
sum = reduce(lambda x, y: x + y[1], expense, 0)
print(sum) # 580

#1. list comprehension
numbers = [1, 2, 3, 4, 5]
# the complicated way instead of list comprehension, with if statement, loop
def sq_n(x):
    a = []
    if isinstance(x, list):
        for item in x:
            a.append(item ** 2)
    else:
        a.append(x * 2)
    return a

print(sq_n(numbers))

# list comprehension: the easiaest way to create a list and more readable than loops
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers) # [1, 4, 9, 16, 25]

# list comprehension with if statement
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers if x % 2 == 0]
print(squared_numbers) # [4, 16]


