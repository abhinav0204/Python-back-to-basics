
#oops

# classic method of creating a class -- not a good way

class Person:
    pass

john_doe = Person()
john_doe.name  ="Abhinav"
john_doe.surname = "Surname"
john_doe.dob=1996

suman = Person()
suman.age = 56
suman.occupation = "banker"

print("the created object is  :",john_doe)
print("%s %s was born in %d"%(john_doe.name,john_doe.surname,john_doe.dob))
print("suman's age is %s and profession is %s"%(suman.age,suman.occupation))




#methods

class Boy:
    def __init__(a,name,surname,dob):
        a.name = name
        a.surname = surname
        a.dob = dob
    def age(a,current_yr):
        return current_yr - a.dob

    def __str__(a):
        return "%s %s was born in %d"%(a.name,a.surname,a.dob)

alec = Boy("rohan","prasad",1996)
print(alec)
print(alec.age(2020))



# bad practise == creating function for each variable is bad practise

class Human:
    def set_name(self,name):
        self.name = name
    def set_surname(self,surname):
        self.surname = surname
    def set_dob(self,dob):
        self.dob = dob
    def age(self,current_year):
        return current_year -self.dob

    def __str__(self):
        return "%s %s was born in %d"\
        %(self.name,self.surname,self.dob)


president = Human()
president.set_name("Joe")
president.set_surname("biden")
president.set_dob(1958)



print(president.name)
print(president.surname)
print(president.age(2021))
print(president)


## good way of creating a class -- class should have predifned variables

#class skeleton should not change

class Person:
    def __init__(self,first_name,last_name,dob):
        self.first_name1 = first_name
        self.last_name1 = last_name
        self.dob1 = dob

alec = Person("abhinav","suman",1996)
print(alec)

print(" %s %s was born in %d"%(alec.first_name1,alec.last_name1,alec.dob1))



#  no public,private ,protected keyword in python
# abstraction

# single underscore -- protected
# double underscore -- private
# without underscore -- public



class Person:
    def __init__(self,first_name,last_name,dob):
        self._first_name1 = first_name # pulbic variable
        self.__last_name1 = last_name # private variable
        self._dob1 = dob

alec = Person("abhinav","suman",1996)
print(alec._first_name1)  ## accessing public variable
print(alec._Person__last_name1)  ## accessing private variable




## inheritence

class Student(Person):
    def __init__(self,student_id,*args):  # all args of parents class
        super(Student,self).__init__(*args) #trying to initialise student class using super method
        self._student_id = student_id

charlie = Student(1,'Charlie','Brown',2006)
print(charlie._student_id)

print(type(charlie))

print(isinstance(charlie,Person))
print(isinstance(charlie,object))


#multiple inheritence

class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def test(self):
        print("this is my class A print statement")

class B:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def test(self):
        print("this is my class B print statement")


class C(A,B):
    obja = A("sf",12)
    objb = B("ds",1123)
    obja.test()
    objb.test()


abhi = C("abhi","s")


print(abhi.x)
print(abhi.__dict__)   # predefined method  -- display data as dict


## method overrriding -- to override a method just define it again

class Student(Person):
    def __init__(self,student_id,*args):  # all args of parents class
        super(Student,self).__init__(*args) #trying to initialise student class using super method
        self._student_id = student_id

    def __str__(self):
        return super(Student,self).__str__()+" And has ID: %d"  % self._student_id  # method overriding

charlie = Student(1,'Charlie','Brown',2006)
print(charlie)



# encapsulation  -- binding data and methods together

# two main reasons to use
#composition
#dynamic extension


# composotion == car is composed of tyres ,engine and body  -- model is described in simple concepts

class Tyres:
    def __init__(self,branch,belted_bias,opt_pressure):
        self.branch = branch
        self.belted_bias = belted_bias
        self.opt_pressure = opt_pressure

    def __str__(self):
        return (" Tyres : \n \tBranch : " +self.branch +
                 "\n \tBelted bias : " +str(self.belted_bias)+
                 "\n \t Optimal pressure" + str(self.opt_pressure))

class Engine:
    def __init__(self,fuel_type,noise_level):
        self.fuel_type = fuel_type
        self.noise_level = noise_level

    def __str__(self):
        return ("Engine \n \t fuel type : "  +self.fuel_type +
                "\n \t Noise level: " +str(self.noise_level))



class Body:
    def __init__(self,size):
        self.size = size

    def __str__(self):
        return "Body \n \t Size : " +self.size

class Car:
    def __init__(self,tyres,engine,body):
        self.tyres = tyres
        self.engine = engine
        self.body = body

    def __str__(self):
        return str(self.tyres) + "\n" + str(self.engine) +"\n" +str(self.body)


t = Tyres('Piralle','True',2.0)
e = Engine('Diesel',3)
b = Body("Medium")
c = Car(t,e,b)                     # composite encapsulation

print(c)



## dynamic encapsulation

class Dog:
    def __init__(self,name,yob,breed):
        self._name = name
        self._yob = yob
        self._breed = breed

    def __str__(self):
        return "%s is a %s born in %d" %(self._name,self._breed,self._yob)

kudrajavka = Dog("kudrajavka",1954,"Lalka")
print(kudrajavka)


class Student:
    def __init__(self,anagraphic,id):
        self._anagraphic = anagraphic
        self._id = id

    def __str__(self):
        return str(self._anagraphic) + " Student Id : %d" %self._id


alec_student = Student("dfds",1)   #overriding

kudrajavka_student = Student(kudrajavka,2)  #inheritence

print(alec_student)
print(kudrajavka_student)



#polymorphism -- same method -- different operations

def summer(a,b):
    return a+b



print(summer(1,1))
print(summer(["a","b","c"],["d","e"]))
print(summer("abra","cadabra"))


################################################################################


# file operations

# opening the test.txt (if present)

my_file = open('my_file.txt')

print(my_file)

print(my_file.read())  # read the data of the files (return as stream)

print(my_file.readlines()) # return list of lines in the file (return as list)


print(my_file.seek(20)) #seek the location to the start of the file


#writing to a file

#w stands for write

my_file = open('test1.txt','w+')


# write to the file

my_file.write('this is a new line')


#seek to the start of the file

print(my_file.seek(0))

# read the file

print(my_file.read())


## iterating through a file

my_file = open('test1.txt')
print(my_file.read())
