""" #16 string slicing

print(len('hello'))

print(len('I am'))

mystring = "abcdefghijk"


print(mystring[0])

print(mystring[8])

print(mystring[-3])


print(mystring[1:3])

# takes a gap  of one argument

print(mystring[2:7:2])

# reverse indexing

print(mystring[::-1]) """

""" 
## 17. String properties and methods

# strigs are immutable

name = "Sam"
# name[0] = 'P' # this can't be done

# can be done using string concat , +

last_letter = name[1:]

print(last_letter)

final_word = 'P' + last_letter

print(final_word)

final_word = 'P' + final_word

print(final_word)

# multiple string concatenation

letter = 'z'
letter * 10
print(letter)

# int concatenation

print(2+3)

# string concatenation

print('2' + '3')

x = 'Hello World'

# string methods  # not inplace methods

print(x.upper())

print(x.lower())

# split method - spllit and store it into list

x = 'Hi, This is a string'

print(x.split())


# split on i's
print(x.split('i'))



 # count function  - count number of occr of a substring

A = "This is a python tutorial"
print(A.count("is",0,len(A)))

# center , ljust, rjust - stuff a string to make it of desired length

str = "GeeksForGeeks"

print(str.center(20,'-'))

print(str.ljust(20,'-'))

print(str.rjust(20,'-'))


#is alpha , isalnum ,isspace

str1 = "abc"
str2 = "abc12"
str3= " "

print("For string 1 : isaplha () -->",str1.isalpha())

print("For string 2 : isaplha () -->",str2.isalnum())


print("For string 3 : isaplha () -->",str3.isspace())


# join -- join all ele in a list with a delimiter

l = ['Geeks','For','Geeks']
s = " "
print(s.join(l))

# reverse a string

gfg = "geeksforgeeks"

gfg = "".join(reversed(gfg))
print(gfg)

# string slicing

print(gfg[3:12])

# 3rd and 2nd last character
print(gfg[3:-2])

# python - update character of string

# since strings are immutable we need to convert into list do the manipulation and convert back to string

string = "Hello , I'm a Geek"
list1 = list(string)
list1[2] = 'p'
string2 = ''.join(list1)
print(string2)

# another way - string slicing

string3 = string[0:2] + 'p' + string[3:]
print(string3)


# deleting character from string - slicing

# deleting 2nd character
 
string2 = string[0:2] + string[3:]
print(string2)


# deleting entire string

del string2
#print(string2) # gives error - string2 not defined

#escape sequences

string1 = 'I\'m a geek'
print(string1)

string2 = 'Hi\tGeeks'
print(string2)

string3 = "I'm a \"Geek\""

print(string3)

string4 = "Python\nGeeks"

print(string4)

""" 

"""
# print formatting with strings

# .format() and f-string method

# .FORMAT

result = 100/777

print('This is a string {} '. format('INSERTED'))

# number of decimals after decimal points - defined , incuding whitespaces

print('The result was {r:10.6f}'.format(r = result))

name = 'Jose'

age = '3'

# new format - with f string

print(f'{name} is {age} years old.') """



""" 

 Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered

 """


""" 


## Lists are objects of different data type

my_list = [1,2,3]

my_list = ['STRING',100,23.2]

print(my_list)


# indexing and slicing like strings

my_list = ['one','two','three']

print(my_list[0])

another_list = ['four','five']

# concatenate -- not inpace , need to assign to a new variable to save

print(my_list+ another_list)


new_list = my_list+ another_list

# indexing and slicing -just like strings

print(new_list[0])

print(new_list[1:])


# elements are mutable

new_list[0] = 'ONE ALL CAPS'

print(new_list)

## inserting items in list -- append,extend,insert

# appending at the end of list -- it is inplace

#append() function inserts a single element into an existing list.

new_list.append('six')

print(new_list)

new_list.append(['seven','eight'])

print(new_list)

## extend() can add multiple individual elements to the end of the list.

new_list.append('nine')

print(new_list)

new_list.extend(['ten','eleven'])

print(new_list)

# insert - insert any item in the particular index of the list and right shift the list items.

# insert(index,item)

new_list.insert(0,'zero')

print(new_list)




# delete an element from the list

# pop - removes last element from the list

popped_item = new_list.pop()

print(new_list,popped_item)

# reversse indexes while popping out element

new_popped_item = new_list.pop(-1)

print(new_list,new_popped_item)


# remove - remove the first occurence of the element specified in the list

list = ['Cake', 'Pizza', 'Juice', 'Pasta', 'Burger','Juice']

list.remove('Juice')

print(list)

# del - remove item based on indexes

del[list[0]] #remove 0th index ele from the list

print(list)

new_list = ['a','e','x','b','c']
num_list = [4,1,8,3]

# sort the list , inplace, return nothing 
# returns NoneType - indicate no value


new_list.sort()

print(type(new_list))


# to store the sorted result - first sort the values and then store

new_list.sort()

sorted_list = new_list

print(sorted_list)

print(num_list)

num_list.sort()

print(num_list)

# sorted - sort the list # not inplace

new_list = ['a','e','x','b','c']
num_list = [4,1,8,3]

print(sorted(new_list))

print(new_list)


# reverse method in list ,  - especially to reverse int type, inplace

new_list = ['a','e','x','b','c']
num_list = [4,1,8,3]

new_list.reverse()

print(new_list)

# creating multi dimesnsional list

List = [['geeks ', 'for'],['geeks','website']]

print(List[0][1])

print(List[1][1])

List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']

# negative indexing
print(List[-1])

# length of list
print(len(List))

# taking input in a list python

string = input("Enter elements (space - seperated):")

# split the string and stores in list
lst = string.split()
print('The list is : ',lst)


 


n = int(input("Enter the size of list : "))


# stores the element using map,split and strip function

lst = list(map(int,input("Enter the integer elements :").strip().split()))

# printing the list

print('The list is',lst)



# adding elements to list using iterator

L=[]
for i in range(1,4):
    L.append(i)

print(L)

#adding tuples to the list

L.append((5,6))
print(L)

# adding list to a list

L.append(['Geeky','Abhinav'])
print(L)

# insert an element on a specific position
L.insert(3,12)
print(L)

# extend - appending mutliple elements to the list at once

L.extend([8,'Abhi','Suman'])
print(L)

# reverse a list
mylist = [1,2,3,4,5,6,'Geeks','Python']
mylist.reverse()
print(mylist)

# Removal of elements in a List

mylist.remove(6)
print(mylist)

# removing elements based on iterator

for i in range(1,5):
    mylist.remove(i)

print(mylist)

# list comprehenssion

odd_square = []

for x in range(1,11):
    if x % 2 == 1:
        odd_square.append(x**2)

print(odd_square)

# same can be written using list comprehension

odd_square = [x**2 for x in range(1,11) if x%2==1]
print(odd_square)


"""


""" 
# dictionaries in python - unordered collection of items ,stored as key value pair
# keys and values can be of any data type but can't be null


my_dict = {'key1':'value1','key2':'value2'}

print(my_dict)

print(my_dict['key1'])

prices_lookup = {'apple':2.99,'oranges':1.99,'milk':5.80}\


# getting the value based on key


print(prices_lookup['apple'])

# complex dict

d = {'k1':123,'k2':[0,1,2],'k3':{'insideKey':100,'name':'abhinav'}}

# accessing the elements of dict

# for accessing the list of k2 key


print(d['k2'])

#  for accessing the key 'insideKey' inside the dict of key 'k3'

print(d['k3']['insideKey'])

#  for accessing the  2nd index element of list of k2 key


print(d['k2'][2])


di = {'key1':['a','b','c']}

# fetching the list and storing the values and doing uppercase

my_list = di['key1']

letter = my_list[2]

print(letter.upper())

# alternative way 

print(di['key1'][2].upper())

# assign new value to key 

d['k3'] = 300

print(d)


# overwrite existing value to the dict

d['k1'] = 'NEW VALUE'
print(d)

# to get all the keys

print(d.keys())

# to get all the values

print(d.values())

# to get both keys and values in dict as a seperate key

print(d.items())

d = {0.1:'a',1:'b'}

print(d[0.1])

# len of dict

print(len(d))

# type of dict

print(type(d))

# dict constructor to make a dict

d = dict(name='Abhinav',age=36,country='Norway')

print(d)

# empty dict

dic = {}

print(dic)

# accessing a element from a Dictionary


Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
  
# accessing a element using key
print(Dict['name'])
  
# accessing a element using key
print(Dict[1])

#Accessing an element of a nested dictionary

Dict  = {'Dict1':{1:'Geeks'},'Dict2':{'Name':'For'}}

print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])


# demo for all dictionary methods
dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
  
# copy method -  Returns a copy of the dictionary

dict2 = dict1.copy()
print(dict2)

# clear() method -  Returns a copy of the dictionary
dict1.clear()
print(dict1)

#get method - Returns the value of specified key
print(dict2.get(1))

#items method
print(dict2.items())

#keys method

print(dict2.keys())

# remove element from dict - pop()

dict2.pop(4)
print(dict2)

# popitem() method -  Removes the last inserted key-value pair

dict2.popitem()
print(dict2)

#update() method
dict2.update({3:'Scala'})
print(dict2)

#values() method
print(dict2.values())
 """
""" 
 # tuples are immutable (one key diff from lists) .similar to lists
#tuples (1,2,3)

t = (1,2,3)

mylist = [1,2,3]

print(type(t))

# len of tuple

print(len(t))

# mix of data type

print('one',2)

# slicing and indexing

print(t[0])

print(t[-1])

t = ('a','a','b')
t1= (1,1,2)

#count
print(t.count('a'))

#index
print(t.index('a',1))

#concat
print(t + t1)

#tuples are immutable while strings are mutable

# tuples are faster than list 
# passing as an objects that does not often get changed
# data integrity is maintained

mylist[0] = 'NEW'  # works fine as list are mutable
#t[0] = 'NEW' # type error : does not support assignment

# nesting of tuple

tuple3 = (t1,t)
print(tuple3)

# repitition

tup3 = ('python')*3
print(tup3)

# slicing 
tuple1 = (0,1,2,3)
print(tuple1[1:])
print(tuple1[::-1])

# deleting a tuple
tuple3 = (0,1)
del tuple3

# printing len of tuple
tup2 = ('python','geek')
print(len(tup2))

# converting list to tup
lis = [0,1,2]
print(lis)

# tuples in loop
tup = ('geek',)
n=5
for i in range(int(n)):
    tup = (tup,)
    print(tup)
 """
""" 
 # sets in python -- unordered collection of unqiue elements
# no duplicates

#However, there are two major pitfalls in Python sets: 

#The set doesn’t maintain elements in any particular order.
#Only instances of immutable types can be added to a Python set.

# used for removing duplicates in a list

myset = set()
print(myset)

# adding the element to the set
myset.add('d')
print(myset)

myset.add(2)
print(myset)

# adding the same value does nothing to set

myset.add(2)
print(myset)

mylist = [1,1,1,2,2,2,3,3,4,4,5]

new_list = list(set(mylist))
print(new_list)

# frozen sets
#While elements of a set can be modified at any time, elements of the frozen set remain the same after creation. 

#If no parameters are passed, it returns an empty frozenset.

normal_set = set(["a","b","c"])

print(normal_set)

# forzen set
frozen_set = frozenset(['e','f','g'])
print(frozen_set)

# adding element to set
people = {"Jay", "Idrish", "Archi"}

people.add("Abhinav")

print(people)


# adding element to set using iterator keyword
for i in range(1,6):
    people.add(i)
print(people)

# union on sets - union or '|'

people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}

population = people.union(vampires)
print(population)

population = people|dracula
print(population)

# intersection on sets - intersection or  '&' keyword

set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)

for i in range(3,9):
    set2.add(i)


set3 = set1.intersection(set2)
print(set3)

set3 = set1 & set2
print(set3)

# set difference - persent in a not in b - difference keyword

set1 = set()

set2 = set()

for i in range(5):
    set1.add(i)

for i in range(3,9):
    set2.add(i)

set3 = set1.difference(set2)
print(set3)

set3 = set1 - set2
print(set3)

# clear - empties the set

set1 = {1,2,3,4,5,6}
set1.clear()
print(set1)

# disjoint sets -- sets having nothing in common -isdisjoint keyword
set1 = {1,2,3,4}
set2 = {6}

print(set1.isdisjoint(set2)) """

""" 

# booleans - operators to convey True or False

print(type(True))

print(type(False))

b = None
print(b)

x = 5
y = 10
print(bool(x==y))

x = ()
print(bool(x))

x = {}
print(bool(x))

x = 'A'
print(bool(x))

var1 = 0
print(bool(var1))

var1 = 2
print(bool(var1))

# is operator -- two var references to same object - if both are same

x = 10
y = 10

if x is y:
    print(True,'is operator')
else:
    print(False ,'is operator')

x = ["a", "b", "c", "d"]
x1 = ["a", "b", "c", "d"]

print(x is y)

# Python Boolean == (equivalent) and != (not equivalent) Operator
# check if the values in two variables are equal or not
a=0
b=1
if a == 0:
    print(True,'equivalence check')

if a == b:
    print(True)
if a!=b:
    print(True ,'equivalence check')

# membership operator -in

animals = ["dog", "lion", "cat"]
if "lion" in animals:
    print(True) """

""" ## 28 . IO with Basic Files In Python

import os

myfile = open('credentials.txt')

print(myfile.read())
print(os.getcwd())
print(myfile.read())

print(myfile.seek(0))

print(myfile.readlines())

myfile.close()

print(myfile)

# to enable auto closing of file we use with keyword


with open('credentials.txt') as new_file:
    cotents = new_file.read()

# assigning mode while file handling
with open('credentials.txt',mode='r') as new_file:
    cotents = new_file.read()

#mode = 'r' is read only
#mode = 'w' is write only ( will overwerite files or create new)
#mode = 'a' is append only (will add on to files)
#mode = 'r+' is writing and reading 
#mode = 'w+' is writing and reading (overwrites existing file and create new file)

with open('credentials.txt',mode='a') as f:
    f.write('\n ak@gmail.com ak')

with open('new_file.txt',mode='w') as f:
     f.write('I CREATED THIS FILE !')

with open('new_file.txt',mode='r') as f:
     print(f.read()) """

""" 
d = {'k1': [{'nest_key' : ['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

 """

""" 
# comparison operator

print(2==1)

print('hello'=='Bye')

print(1 != 1)

print(not(100==1 and 2 == 200))

 """


""" 
# if elif and else statements

hungry = True

if hungry == True:
    print('Feed Me !!')
else:
    print('I\'m not hungry') """

""" 
loc = 'Auto Shop'

if loc == 'Auto Shop':
    print("Cars are cool !")

elif loc == "Bank":
    print("Money is cool !")

else:
    print('I do not know much !') """


""" 
# for loop in python

my_list = list(range(1,11))

for num in my_list:
    if num%2==0:
        print(f'Even number : {num}')
    else:
        print(f'Odd number  : {num}')



my_list = list(range(1,11))


list_sum = 0

for num in my_list:
    list_sum += num

    print(list_sum)



mystring = 'Hello World'

for _ in mystring:
    print(_)

tup = (1,2,3)

for item in tup:
    print(item)
 


mylist = [(1,2),(3,4),(5,6),(7,8)]

mylist1 = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]

len(mylist)

for item in mylist:
    print(item)

# tuple unpacking

for a,b,c in mylist1:
    print(a)
    print(b)
    print(c)

"""
""" 
d = {'k1':1,'k2':2,'k3':3}

# iterate thorugh dict



# tuple unapacking in dict

for key,value in d.items():
    print(value)

d = {'k1':1, 'k2':2,'k3':3}

for item in d:
    print(item) """

""" 
# while loop with else
# only when while is executed the


x = 0
while x < 5:
    print(f"The current value of x is {x}")
    x+=1

else:
    print("X is not less than 5") """

""" 
# pass 

x= [1,2,3]
for item in x:
    pass
print('End Of My Script')

#continue

mystring  = 'abhinav'
for letter in mystring:
    if letter == 'a':
        print('This is letter A !')
        continue
    print(letter)

# break
x=0
while x<5:
    if x == 2:
        break
    print(x)
    x+=1  """
""" 
# range - specifies the range for the loops

mylist = [1,2,3]

for num in range(0,11,2):
    print(num)

# can be done also as

print(list(range(0,11,2)))

# enumerate function -- to get the specified counter for each value

index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count+=1

# or

index_count=0
word = 'abcde'

for letter in word:
    print(word[index_count])
    index_count+=1

word = 'abcde'
for index,item in enumerate(word):
    print(index)
    print(letter)
    print('\n')

# zip - generator - concatenate two lists
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3=[100,200,300]

for item in zip(mylist1,mylist2):
    print(item)

print(list(zip(mylist1,mylist2)))

# in , membership operator - check something in present in list or not

print('x' in [1,2,3])

print('mykey' in {'mykey':365})

d = {'mykey':365}

print(365 in d.values()) """


""" 
# min and max values

mylist = [10,20,30,40,50,60]

print(min(mylist))

print(max(mylist))

# random libraries python

# shuffle - shuffle the list - does not return anything - inplace
from random import shuffle

mylist = [3,4,5,6,7,8,9,10]

shuffle(mylist)

print(mylist)

# randint - getting a randomn number


from random import randint

print(randint(0,100))

# accept user input

result = input("favouriate number : ")
print(type(result))

print(float(result))

print(int(result)) """

""" 

# list comprehension -- quickly creating a list

mystring = 'Hello'
mylist = []

for letter in mystring:
    mylist.append(letter)

print(mylist)

mylist = [letter for letter in mystring]
print(mylist)

mylist = [x for x in 'word']
print(mylist)

mylist = [num**2 for num in range(1,11)]
print(mylist)

mylist = [x**2 for x in range(0,11) if x%2==0]

celsius = [0,10,20,34.5]

fahreheit = [((9/5)* temp + 32) for temp in celsius]

print(fahreheit)

fahreheit = []
for temp in celsius:
    fahreheit.append((9/5)*temp +32)

print(fahreheit)

results = [x if x%2==0 else 'ODD' for x in range(0,11)]

print(results)

mylist = []

for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)

print(mylist)

mylist = [x* y for x in [2,4,6] for y in [1,10,1000]]
print(mylist)


 """

""" 
# python statements exercise

#1

st = 'Print only the word that start with s in the sentence'

word_list = st.split()

statement =[]

for i in word_list:
    if i[0].lower() == 's':
        print(i)


#2 
for i in range(0,11):
    if i%2==0:
        print(i,end=' ')

#3  
div_by_3 = [x for x in range(1,51) if x%3==0]

print(div_by_3)


#4

st = 'Print every word in the sentence that has even numbers of letters'

words = st.split()
for i in words:
    if len(i)==2:
        print('Even')

#5 

for i in range(1,101):

    if (i%3==0 and i%5==0):
        print('FizzBuzz',i)
    if(i%3==0):
        print('Fizz',i)
    elif (i% 5==0):
        print('Buzz',i)
    else:
        print(i)


#6

# create a list of the first letters of every word in the string below

st = 'Print every word in the sentence that has even numbers of letters'

lis_comp = [i[0] for i in st.split()]

print(lis_comp) """

""" #41. methods 

mylist = [1,2,3]
mylist.append(4)
print(mylist)
mylist.pop()
print(mylist)

help(mylist.insert)
 """


# functions

# block of code that can be executed many times

# increase readablilty


# def keyword

# snake casing - all lowercase with underscores between words

# doc string - multi line string explaining the working of the function


# def name_of_function(name):
#     # """ Docstring explains function"""
#     print("Hello " + name)

# name_of_function("Abhinav")


# return keyword = send the result of the function instead of printing
# allows to assign the value returned to a variable

# func with return 

# def add_function(num1,num2):
#     return num1+num2

# result = add_function(1,2)
# print(result)


""" 
def say_hello():
    print("hello")
    print("how")
    print("are")
    print("you")

print(say_hello) # without parenthesis - return the func name

print(say_hello()) """


# default - if val not provided it will be passed

# return vs print - value can be saved in a variable in return

""" 
def say_hello(name='Default'):
    print(f'Hello {name} !!')

say_hello() """

""" def add_num(num1,num2):
    return num1+num2

result = add_num(10,20)

print(result)

 """

 ## functions with logic
""" 
def check_even_list(num_list):
    for number in num_list:
        if number %2==0:
            return True
        else:
            pass

print(check_even_list([1,3,5]))

print(check_even_list([2,4,5]))

print(check_even_list([1,1,1,2])) """

""" 
def check_even_numbers(num_list):
    even_numbers=[]
    for numbers in num_list:
        if numbers % 2 == 0:
            even_numbers.append(numbers)
        
        else:
            pass
    return even_numbers

print(check_even_numbers([2,4,5,6,7,8]))
 """


""" 
# tuple unpacking

stock_prices = [('APRIL',200),('GOOG',4000),('MSFT',100)]

for item in stock_prices:
    print(item)

for ticker,price in stock_prices:
    print(price + (0.1*price))


work_hours = [('Abby',100),('Billy',400),('Cassie',800)]

def employee_check(work_hours):
    current_max = 0
    employee_of_the_month =''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_the_month = employee
        
        else:
            pass
    return (employee_of_the_month,current_max)


result = employee_check(work_hours)
print(result)

##tuple unpacking

name,hours = employee_check(work_hours)
print(name,hours)

#name,hours,locations = employee_check(work_hours)  ## two many tuples to unpack
#print(name,locations,hours)

# interation b/w functions
 """

""" 
 # interaction b/w python function

example = [1,2,3,4,5,6,7]

from random import shuffle

shuffle(example) # shuffles the list

print(example)


 """

""" example = [1,2,3,4,5,6,7]

from random import shuffle

shuffle(example) # shuffles the list

"""

""" 
from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number 0,1 or 2 : ")

    return int(guess)



def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct !!')
    else:
        print('Wrong guess !')
        print(mylist)


# initial list

mylist = [' ','O',' ']

# shuffle list

mixed_up_list = shuffle_list(mylist)

# user guess

guess = player_guess()

# check guess

check_guess(mixed_up_list,guess)
 """


# kwargs and args -- unlimited number of args can be passed

""" def myfunc(a,b,c=0,d=0):
    #  return 5 % of a and b

    return (sum(a,b,c,d)) * 0.05

print(myfunc(50,60,70,80)) """


""" 
def myfunc(*args):      # args -- retuns  a tuple
    return sum(args)*0.05

print(myfunc(2,5,66,77,32))

 """

""" def myfunc(**kwargs):  
    print(kwargs) # kwargs returns a dict
    if 'fruit' in kwargs:
        print('My fruit of choice is {} .'.format(kwargs['fruit']))

    else:
        print('I did not find any fruit here.')

myfunc(fruit="apple",vegie='lettuce')

 """

""" 
# args should be always before kwargs

def myfunc(*args,**kwargs):
    print("I would like {} {} ".format(args[0],kwargs['food']))
    
myfunc(10,20,30,40,50,fruits='orange',food='eggs',animal='dog')

 """

 # func practice problem

#1. 
""" 
def lesser_of_two_events(a,b):
    if a%2==0 and b%2==0:
        if a < b:
            result=a
        else:
            result=b
    else:
        # one or both of the num are odd
        if a>b:
            result = a
        else:
            result=b

    return result


print(lesser_of_two_events(23,6)) """

""" 
def lesser_of_two_events(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        # one or both of the num are odd
        return max(a,b)

    return result

print(lesser_of_two_events(23,6)) """

#2.
""" 
def animal_crackers(text):
    wordlist = text.split()
    if len(wordlist)<2:
        return 'Invalid String Length !!'

    elif wordlist[0][0].lower() == wordlist[1][0].lower():
        return True

    else:
        return False

print(animal_crackers(' Llama'))
 """
    

""" 
## 3.

def makes_twenty(n1,n2):
    return  n1+n2 == 20 or (n1==20 or n2==20)


print(makes_twenty(10,10))  """


## Functions -Practice - Level 1

""" 
def old_word(name):
    first_letter = name[0]
    in_between = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]

    return first_letter.upper() + in_between + fourth_letter.upper() + rest

print(old_word('macdonald')) """

""" 
def old_word(name):
    first_half = name[:3]
    second_half = name[3:]

    return first_half.capitalize() + second_half.capitalize()

print(old_word('macdonald'))

 """

""" 
def reverse_word(text):
    wordlist = text.split()
    reverse_word_list = wordlist[::-1]
    return ' '.join(reverse_word_list)

print(reverse_word('I am home'))

 """


""" 
def master_yoda(text):
    return text.lower() == text[::-1].lower()

print(master_yoda('Madam')) """

""" def almost_there(n):
    return (abs(100-n) <= 10) or  (abs(200-n)<=10)

print(almost_there(500)) """


""" 
# level 2 problems

#1 given a list of ints, return True if the array contains a 3 next to 3 somewhere

def has_33(nums):
    for i in range(0,len(nums-1)):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False """

#2

""" def paper_doll(text):
    for i in text:
        print(i*3,end='')

paper_doll('Mississippi') """
""" 
def paper_doll(text):
    result=''
    for i in text:
        result+= i*3
    print(result)

paper_doll('Mississippi') """


""" 
def sum_op(a,b,c):
    return a+b+c



def blackjack(a,b,c):
    if sum_op(a,b,c) <= 21:
        return sum_op(a,b,c)
    elif 11 in [a,b,c] and sum_op([a,b,c])-10 <=31:
        return sum_op([a,b,c])-10

    else:
        return "BUST"
print(blackjack(9,9,9))

 """
""" 
def summer_69(arr):
    total=0
    add = True

    for num in arr:
        while add:
            if num!=6:
                total += num
                break
            else:
                add = False

        while not add: # while add!=True
            if num!=9:
                break
            else:
                add=True
                break
    
    return total


print(summer_69([1,3,5]))

print(summer_69([4,5,6,7,8,9]))

print(summer_69([2,1,6,9,11])) """

""" 
#spy game

def spy_game(nums):
    
    code = [0,0,7,'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)
        
    return len(code)==1

print(spy_game([1,2,4,0,0,7,5])) """

""" def count_primes(num):
    # check for 0 or 1 input

    if num < 2:
        return 0

    # 2 or greater

    #store our prime numbers
    primes = [2]

    #counter going up to the input num
    x = 3

    # for -else - if for runs successfully else runs


    while x<= num:
        for y in primes:
            if x%y == 0:
                x+=2
                break
        else:
            primes.append(x)
            x+=2
    print(primes)

count_primes(50) """


""" 
# lambda expression : map and filters
#lambda functions = anonymous function

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

map(square,my_nums)  ##  gives generator -- needs to be iterated

for item in map(square,my_nums):
    print(item)

print(list(map(square,my_nums)))


def splicer(mystring):
    if len(mystring)%2==0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy','Eve','Sally']

print(list(map(splicer,names)))
 """

""" def check_even(num):
    return num%2==0

my_nums = [1,2,3,4,5,6]

# filter(check_even,my_nums)  ##  gives generator -- needs to be iterated


print(list(filter(check_even,my_nums)))


for n in filter(check_even,my_nums):
    print(n,end=',') """


""" def square(num):
    return num**2

print(square(3)) """

""" # lambda function - anonymous function - smaller way of writing funcs

square = lambda x:x**2 

print(square(3))

mynums = range(10)

# map - apply a function  to a list

print(list(map(lambda num:num**2,mynums)))

# filter - filters the value based on the list

print(list(filter(lambda num:num%2==0,mynums)))


names = ['Andy','Eve','Sally']

print(list(map(lambda x:x[0],names)))

 """

# nested statements and scope

#LEGB rule
#L:local , E: enclosing function locals
#G:Global , B: built in (python)

""" 
x = 25

def printer():
    x = 50
    return x

print(x)

print(printer()) """

""" name = 'THIS IS A GLOBAL STRING'

def greet():
    name = 'Sammy'
    def hello():
        print('hello ' +name)
    hello()

greet()

x = 50

def func(x):
    

    print(f'X is {x}')

    # local reassignment
    x='NEW VALUE'
    print(f'I\'m just locally changed global x to {x}')
    return x

print(x)

x = func(x)

print(x) """

## methods and functions - homework  overview


#1. 
def vol(rad):
    return (4/3) * (3.14) * pow(rad,3)

print(vol(2))

#2. check whether thee number is in a given range

def ran_check(num,low,high):
    if num>= low and num<=high:
        print(f'{num} is in the range between {low} and {high}')

    else:
        print(f'{num} is outside the range between {low} and {high}')

ran_check(15,2,7)


#3. # string that calculates upper case and lower case
