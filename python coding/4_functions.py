################################################################################

### FUNCTIOMS


#func without definition

def test():
    pass


# you can either return ro print the func

def test1():
    print("this is my first function")

test1()

def test2():
    return "this is my 2nd function"

print(test2())


## we use return in place of print for better practise


# if returning more than one value the output type is tuple


#print stateement return none type


def double_perf(x):
    return x*3,x+x

print(double_perf(3))  # return tuple

a,b = double_perf(3)  #tuple unpacking

print(a,b)


#basic func

def print_func(x):
    for i in x:
        if i=='a':
            print(i)

print_func("abhinav")




def name_of_func(arg1,arg2):
    '''
    This is where doc string goes
    '''

    # do rest of the stuff here

# default args

def addition(a=90,b=10):
    return a+b

print(addition())



# greeting func

def greeting(name):
    print('Hello %s  !!!'%name)

greeting("Abhinav")


# prime or not func

def is_prime(num):
    '''
    Naive method for checking primes
    '''

    for n in range(2,num):
        if num%n ==0:
            print("not prime")
            break
    else:
        #if never mod zero,then prime
        print('prime')

is_prime(23)




################################################################################

#ITERATORS AND GENERATORS


#YOU CAN'T ITERATE OVER INTEGER UNLIKE STRING

#INT OS NOT ITERABLE

#STRING IS NOT ITERATOR

#FOR LOOP CONVERT STRING TO ITERATOR AND THEN WE CAN LOOP OVER INT

a = iter("abhinav")
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


print(range(5))

for i in range(5):
    print(i)


a = iter(range(6))
print(next(a))

#range is iterable object


#list ,tuple,dict and string are iterable -- means you can run for loop over it

#but int is not iterable --

# if something is not iterable you cannot convert it into iterator -- eg - int (cannot use for loop over it)

#if something is iterator you can convert into iterable





################################################################################

#generator function


#generator for cube of numbers

def cube(a):
    for i in range(a):
        yield i**3


print(cube(3))

# generator is iterable object

a = iter(cube(3))
print(next(a))
print(next(a))
print(next(a))

# since generator is iterable so we can use for loop over it

for i in cube(5):
    print(i)



## lambda function

a=[1,2,3,4]
b=[6,7,8,9]
c=[10,11,12,13]

# sum of all ele of three list row wise

print(list(map(lambda x,y,z:x+y+z,a,b,c)))
