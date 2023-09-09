# List Comprehension

print("''''Square root of elements in list''''")
l = [1,2,3,4,5,6]
'''l1 = []
for i in l:
    l1.append(i**2)
print(l1)
'''
'''print([i**2 for i in l])

print("''''Separate Even no. in iist''''")
print([i for i in l if i % 2 == 0])

l1 = ["sudh",'kumar','pwskills','data scinence']
print([i.upper() for i in l1 ]) # upperacse
'''
# Dictionary comprehension

'''d = {"key1": 1, "key2" : 2, "key3" : 3}
print({k:v**2 for k,v in d.items()})
print({k:v for k,v in d.items() if v > 1})'''


# Functions

'''print("Helo")
l = [2222.,4,32,11,3]
len(l) 
type(l)

def  test() :
    pass
def test1() :
    print("This is very very  first function")
test1()

def test2() :
    return "This is my vvery first return"
print(test2() + " Lakshya")

def test3() :
    return "sudh",23,32,543,[1,24,4,4]
t = test3()
print(t)

def test4() :
    a = 5+6/7
    return a
a = test4()
print(a)

def test5(a,b,c):
    d = a+b/c
    return d
a,b,c = 5,4,3
d = test5(a,b,c)
print(d) 

def test6(a,b) :
    return a+b
a = "Akshay"
b = " kumar"
print(test6(a,b))

def test7(l) :
    l1 = []
    for i in l :
        if type(i) == int or type(i) == float:
            l1.append(i)
    return l1
l = [1,2,4,4,5,"lakshya","Saurabh",[1,2,4,5,6,6]]
d = test7(l)
print(d)'''
'''Separate Integers'''
'''def test8(a) :
    """ This is my function to Extract Numeric data from a list"""
    l1 = []
    for i in a:
        if type(i) == list:
            for j in i:
                l1.append(i)
        else :
            if type(i) == int or type(i) == float :
                l1.append(i)
    return l1
d = test8(l)
print(d)'''
'''Dynamic arguments'''
'''def test10(a,b):
    return a+b

def test11(*args):
    return args'''
#args is n no. of arguments we can pass in the function, all that pass data is in the form of tuples
'''d = test11(1,2,3,4)
print(d)'''

#if we have to pass multiple arguments with some other arguments then we have to declare that arguments in function
'''def test12(*laks, a) :
    return *laks , a
d = test12(12,45,33,322, a = "you")
print(d)

def test13(d,c ,a=23, b = 1):
    return a,b,c,d
e = test13(3,54)
print(e)
'''
# kwargs (key value arguments) --> they return arguments in the form of dictionary(key,value pairs)
'''def test15(**kwargs) :
    return kwargs
d = test15(a = [1,2,3,4,5], b = "sudh" )
print(d)'''

# Generators Function

print("''''Generators''''")
# Using Yield
def fib(n):
    a,b = 0,1
    for i in range(n) :
        yield a
        a,b = b,a+b
for i in fib(10):
    print(i)

def fib1() :
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b
fibo = fib1()
for i in range(10):
    print(next(fibo))



s = "sudh"
for i in s:
    print(i)
# how the for loop works using next func
s = "sudh"
s1 = iter(s)
print(next(s1))
print(next(s1))
print(next(s1))

# Iterator is an object where we can jump by Next Next (string)
# Iterable is an object that default iterate (integer)

def count(n):
    count = 1
    while count < n:
        yield count
        count = count + 1
c = count(5)
for i in c:
    print(i)

# Lambda Function
# Anonymyous function
print("''''Lambda Function''''")
n = 3
p = 2
def test(n,p):
    return n**p
print(test(3,2))

a = lambda n,p : n**p
print(a(3,8))

add = lambda x,y: x+y
print(add(8,7))

cTof = lambda c : (9/5)*c + 32
print(cTof (45))

findingMax = lambda x,y : x if x>y else y
print(findingMax(4,6))

s = "pwskills"
lenFind = lambda s : len(s)
print(lenFind(s))

# Map , Filter and Reduce Function

l = [2,3,4,5,6]

def test(l):
    l1 = []
    for i in l:
        l1.append(i**2)
    return l1
d = test(l)
print(d)

# by using map function 

def s1(x):
    return x**2
print(list(map(s1,l)))

print(list(map(lambda x : x**2,l) ))

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

print(list(map(lambda x,y : x + y, l1, l2)))
 
def add(x,y):
    return x + y
print(list(map(add,l1,l2)))

s = "pwskills"
print(list(map(lambda s : s.upper(),s)))


# reduce

from functools import reduce
l = [1,2,3,4,5,6]
print(reduce(lambda x,y : x+y, l))

print(reduce(lambda x,y : x * y, l))

print(reduce(lambda x,y : x if x > y else y,l))


# Filter

l = [1,2,3,4,5,6,7]

print(list(filter(lambda x : x % 2 == 0, l)))
print(list(filter(lambda x : x % 2 != 0, l)))

l1 = [-3,2,-24,33,-54]
print(list(filter(lambda x : x < 0, l1)))

l2  = ["sudh", "pwskills","kumar","bangalore","krish"]
print(list(filter(lambda x: len(x) < 6, l2)))



