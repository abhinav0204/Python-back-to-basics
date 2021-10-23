#single word
print("hello")

# entire phrase

print("this is a double quoted string")

#we can use single quotes

print('this is a  single quoted string')

# multi line comment

"""
this is a multi line comment
"""


# print the length of the letters in the string

print(len('Hello World'))


#assign as a string

s = 'Hello World'
print(s)


#string slicing

#strings are immutable collection of objects

print(s[::-1])

#lists are mutable collection of objects

l = [2,3,4,5,6,7,8,"abhinav"]

l[0] = "abhi"

print(l)


# + operator for concatenation

s+'abhinav \n'

#we can't assign s completely though

s =s +"concatenate me !"

print(s)


#built in methods in string

string = "         abHInav       "

#lower method
print(string.lower())

#upper mthod
print(string.upper())


#split methodd
print(s.split(' '))




# python print formatting

string = "python"
version =2.0

print("this is {} 2.0 format".format(string))

print("this is also {} 2.0 format".format("python"))



## any number of arguments is acceptable but not any number of brackets are acceptable

print("this is also {} {} format".format(string,version,string))


## location and counting

s = "this is a very big event !!"


#count method

print(s.count('i'))


#find method

print(s.find('v'))

#center method

print(s.center(40,'*'))

# alpha method
print(s.isalpha())

# alnum method
print(s.isalnum())

#endswith method
print(s.endswith('!'))



# bulit in regular expression

print(s.split('e'))  #return list #split the data set on the occurence of all the delimiter

print(s.partition('e')) #return tuple #split the data set only on the occurence of first delimiter


# lists  -- mutable collection of objects

my_list = [1,2,3]

my_list = ['A string',23,100.234,'o']

print(len(my_list))


# indexing and slicing

my_list = ['one','two','three',4,5]

#indexing

print(my_list[0])


#slicing
print(my_list[:3])

#concatenation

my_list = my_list + ["abhinav"]

print(my_list)


# double fold the list

print(my_list*2)


#list operations

# push an elememt to the list operations

l.append('append me')

l.insert(1,"abhinav")

print(1,"s")

l1 = ["apple","banana","mango"]
l2 = ["potato","brinjal","lady finger"]




l1.extend(l2)  # extend unwrap the list2 and append to list 1
print(l1)


l1.append(l2)  # append add the list2 to list 1
print(l1)

print(l1+l2) #same as append -- unwrap the list2 and add to list1


l1.insert(2,"guava")   # insert element at specific position
print(l1)


# expandtabs -- expand along the tabs

print("abhinav\tsuman".expandtabs())




l1 = ["apple","banana","mango"]
l2 = ["potato","brinjal","lady finger"]


#  pop an elememt to the list operations

print(l1.pop())  #default removes the last element

print(l1.pop(-1))  #pop takes integeral position as argumnet



#remove method

my_list = [12, 'Siya', 'Tiya', 14, 'Riya', 12, 'Riya']

my_list.remove(12) # it will remove the element 12 at the start.

print(my_list)


# del method

del my_list[3]

print(my_list)

#Using clear() method


element = my_list.clear()  #The clear() method will empty the given list
print(element)
print(my_list)



# 1. reverse a list

# Python List reverse()

prime_numbers = [2, 3, 5, 7]

# reverse the order of list elements  -- it is peramanent
prime_numbers.reverse()


print('Reversed List:', prime_numbers)

# 2. everse a List Using Slicing Operator

systems = ['Windows', 'macOS', 'Linux']

print(systems[::-1])  # need to assign to new variable for permanent change



#  3. Accessing Elements in Reversed Order  -- reversed is temporary
# If you need to access individual elements of a list in the reverse order, it's better to use the reversed() function.

# Operating System List
systems = ['Windows', 'macOS', 'Linux']

# Printing Elements in Reversed Order
for o in reversed(systems):
    print(o)




# sort method

#Sort the list alphabetically:

cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)


# Sort the list descending:

cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)

print(cars)



# nesting of lists


# creating a nested list

l1 = [1,2,3]

l2 = [4,5,6]

l3 =[7,8,9]

matrix=[l1,l2,l3]

print(matrix)



L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']


#  accessing nested list


print(L[2])
# Prints ['cc', 'dd', ['eee', 'fff']]

print(L[2][2])
# Prints ['eee', 'fff']

print(L[2][2][0])
# Prints eee


# accessing nested list using negative indexes

print(L[-3])
# Prints ['cc', 'dd', ['eee', 'fff']]

print(L[-3][-1])
# Prints ['eee', 'fff']

print(L[-3][-1][-2])
# Prints eee



# Change Nested List Item Value

L = ['a', ['bb', 'cc'], 'd']
L[1][1] = 0
print(L)


#list comprehension

# Empty list
List = []

# Traditional approach of iterating
for character in 'Geeks 4 Geeks!':
    List.append(character)

# Display list
print(List)


# Using list comprehension to iterate through loop
List1 = [character for character in 'Geeks 4 Geeks!']

# Displaying list
print(List1)




#list comprehension vs normal method -- which is faster

# Import required module
import time

# define function to implement for loop


def for_loop(n):
    res=[]
    for i in range(n):
        res.append(i**2)


# define function to implement list comprehension

def list_comprehension(n):
    return [i**2 for i in range(n)]



# Calculate time takens by for_loop()

begin = time.time()
for_loop(10**6)
end = time.time()

# Display time taken by for_loop()

print('Time taken for_loop:',round(end-begin,2))


# Calculate time takens by list_comprehension()

begin = time.time()
list_comprehension(10**6)
end = time.time()



# Display time taken by list_comprehension()

print('Time taken for list_comprehension:',round(end-begin,2))



# if using list comprehension

squares = [n**2 for n in range(1,11) if n%2==0]

print(squares)


#Display even elements from a list of random numbers.

# Assign matrix
twoDMatrix = [[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]]


l1=[]
for j in range(len(twoDMatrix)):
    l2=[]
    for i in twoDMatrix:
        l2.append(i[j])
    l1.append(l2)


print(l1)

# Generate transpose

trans =[[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix)) ]
print(trans)



#if...else With List Comprehension

obj = ["Even" if i%2==0 else "Odd" for i in range(10)]

print(obj)

l1 = [1,2,3]

l2 = [4,5,6]

l3 =[7,8,9]

matrix=[l1,l2,l3]


print([(i[0],i[1]) for i  in matrix])


# list other opeations

l=[1,2,3,4,2,3,2,3,2]

#count method -- count of elements

print(l.count(2))


x = [1,2,3]

x.append([4,5])  # append as list inside list
print(x)


x.extend([6,7])  # unwrap the list and then append -- like + (concat operator)

print(x)


#index operation -- index of first occurence of data

l=[1,2,3,4,2,3,2,3,2]

print(l.index(2))


#remove -- pop element from list -- remove first occurence of element (index element as argument)

print(l.remove(3))

# pop operation -- (index index as argument)

print(l.pop(0))
