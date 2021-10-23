
# tuples -- immutable ororderd collection of objects
t = ()
print(type(t))

t = (1,2,3,4,"abhinav",True,)

print(t)


# converting  tuple to list list to tuple

l = list(t)

l[2] = "abhinav"

print(l)


#convert tuple to list

l =[1,2,3,4,5,6]

print(tuple(l))


# looping in tuples

for i in t:
    print(i)


#tuples operations -- only 2 methods index of 1st occurence of element




#index method
print(t.index(2))

#count method

print(t.count(2))



 # index -- gives index of first val -- considers false - 0 and true-1

t = (1,2,3,4,"abhinav",True,2,1,2,)

for i in t:
    print(t.index(i))



# sets - curly braces -- unordered collection of unique elements constructed using set function

x=[1,2,3,4,5,6,7,8,9]

x = set()
print(type(x))


#split each character of the word

print(list("abhinav"))


# program to find unique elements from a list -- set is used

l = [1,2,2,3,4,5,3,4,1.1,2.2,3.3,"abhinav"]

print(list(set(l)))


# list to set conversion

# you cannot convert nested list to set

print(set([1,2,3,1,1,1.2,1.2,1.2,"abhinav"]))


#  tuple to set conversion


print(set((2,3,4,55,33,22,)))


# set operations


#add function

x = {1,2,5,6,7,1}

print(x.add(3))

print(x)


# looping on set


for i in x:
    print(i)





### dictionaries --  collection consisting of key value pairs
# keys should be unique and duplicate keys gets updated
#values can bee duplicate


d = {}  # curly braces with no element - dict    and with element - set
print(type(d))


# make  a dictionary

my_dict = {True:'value1','key2':'value2','key3':'value3','key1':'abc'}

print(my_dict)


# keys should be unique and duplicate keys gets updated
#values can be duplicate
#boolean values can be used as keys
# collection -- list or tuple cannot be used as keys  -- # can be used as a key
#some special characters cannot be used as keys



# dict formation methods

#using dict keyword

d = {True:'abhinav'}
print(d)

# calling an index on the value

print(my_dict['key1'])

#adding new key to key

my_dict['key5'] ="abhinav"
print(my_dict)


# looping in dict

for i in my_dict:  #by default i takes keys
    print(i)


# looping on dict using dict.items

for i,j in my_dict.items():
    print(i,j)

print(my_dict.keys())  # lists all the keys in the dictionary

print(type(my_dict.keys()))


print(my_dict.values())  # lists all the va.lues in the dictionary

print(type(my_dict.values()))


# To delete an entry, use the del statement, specifying the key to delete:

del my_dict['key1']
print(my_dict)


# Built-in Dictionary Methods


# d.clear() -- empties dictionary d of all key-value pairs:

d = {'a': 10, 'b': 20, 'c': 30}

d.clear()

print(d)


# d.get(<key>[, <default>]) -- eturns the value for a key if it exists in the dictionary.

print(my_dict.get('key2'))

print(my_dict.get('key55'))  # return none if not present


# d.items() -- Returns a list of key-value pairs in a dictionary.

d = {'a': 10, 'b': 20, 'c': 30}

print(list(d.items()))


print(list(d.items())[1][0])

print(list(d.items())[1][1])


#d.values() --Returns a list of values in a dictionary

d = {'a': 10, 'b': 20, 'c': 30}

print(list(d.values()))


# d.pop(<key>[, <default>]) -- Removes a key from a dictionary, if it is present, and returns its value.

d = {'a': 10, 'b': 20, 'c': 30}
d.pop('b')
print(d)


#d.pop(<key>) raises a KeyError exception if <key> is not in d:



#d.popitem()   --Removes a key-value pair from a dictionary.

d = {'a': 10, 'b': 20, 'c': 30}

d.popitem()

print(d)

# d.update(<obj>)  --  Merges a dictionary with another dictionary or with an iterable of key-value pairs.

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}

d1.update(d2)  # merging of two dicts

print(d1)

d1.update([('b',200),('d',400)]) # adding key val to existing dict

print(d1)

d1.update(b=600, d=700)  # adding key val to existing dict -- 2nd type
print(d1)



# create a dict of numbers and squares

squares = {i:i**2 for i in range(10)}

print(squares)


# cannot convert dict into list -- gives only list of keys

#progeam to get mean of all values in key2  of the dict


import statistics

d = {'key1':[1,2,3,4,5],'key2':[6,7,8,9,10]}

d['key2'] = [i*10 for i in d['key2']]

res = statistics.mean(d['key2'])

print(res)





# map  == it is a function which takes two arguments == a function and a sequential iterable

# map(function,sequence)




def fahrenheit(f):
    return(float(9/5)*f+32)

def celsius(f):
    return(float(5/8)*(f-32))


print(fahrenheit(-40))

print(celsius(40))


temp = [0,22.5,40,100]

l=[]
for i in temp:
    l.append(fahrenheit(i))

print(l)



#  same function to convert into fahrenheit using map function

f_temps = list(map(fahrenheit,temp))

print(f_temps)


f_celsius = list(map(celsius,temp))

print(f_celsius)



## lambda function or anonymous function -- adhoc func

print(list(map(lambda x:(5.0/9)*(x-320),f_temps)))

a = [1,2,3,4,6]
b=[5,6,7,5,6,7]
c=[9,10,11,12]

print(list(map(lambda x,y:x*y,a,b)))

print(list(map(lambda x,y,z:x+y+z,a,b,c)))

c = list(map(lambda x,y:x*y,a,b))

for i in c:
    print(i,end=" ")



## reduce function -- aggregation operation while map -- return iterable object
# reduce always takes two arguments


from functools import reduce
lst = [46,11,34,656,87]
print("\n the reduce result is",reduce(lambda x,y:x+y,lst))


max_find = lambda x,y:x if(x>y) else y

print("the max of the list is",reduce(max_find,lst))



# filter func -- filter(function,list) -- filter out the elements for iterable for which func returns true

# return the value for which the func return true

def even_check(num):
    if num%2 == 0:
        return True


lis= range(20)

print(list(filter(even_check,lis)))
