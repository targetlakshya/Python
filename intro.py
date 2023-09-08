# variables

# Integer Variable
laks = 10
print(laks)

vik = 19
print(laks + vik )

print(type(laks))

# Float Variable
b = 2.09 
print(type(b))

# String Variable
d = "Lakshya"
print(type(d))

e = "This is my tech  class"
print(type(e))

# Boolean Variable
n = True
print(type(n))

m = False 
print(type(m))

print(n + m)
print(n*m) 
# print(n/m)  # --> Division By zero error

# Complex Variable
v = 5 + 8j # here j is the notation which can coclude it is imaginary
print(type(v))
print(v.real) # throw real value of the complex 
print(v.imag) #throw imaginary value of the complex

# How to Print
print("My name is Lakshya")
print(v)

s = "PWskills"
print(s[0]) # Indexing (Index always starting from 0 [Forward])

print(s[-1]) # Backward indexing
print(s[-7])

print(s[0:3]) # Slicing [Starting : End - 1]

print(s[0:8:2]) # [Start : end -1 : jump]
print(s[::2])

# Reverse Direction
print(s[::-1])

c = 200
# Function in string
s1 = "this is my string class"
print(len(s1)) #length
print(s1.find('s')) # find() finds the first index of the word you give
print(s1.count('s')) #count the word
print(s1.upper()) #uppercase
print(s1.title()) #first word capital
print(s1.capitalize()) #first letter capital
print(s*3) #sting duplicacy

# "don't do copy and paste in my class"

# List

l = [1,345,45,"laks",True,5+7j,345.456]

print(type(l))
print(l[0])
print(l[4])
print(type(l[5]))

print(l[::-1])
print(l[::2])

s = "pwskills"
# print(list(s) + l)

# print(l[3][0:2])
l1 = [3,4,5]
print(l + l1)
print(l1*3)

l.append(5)
l.append(s)
l.append(l1)
l[-1][1]
print(l)

l.extend("lakshya") # only for iterable object such as string
# l.append("Lakshhya")
l.extend([7,8,9,10])
print(l)

l1.insert(1,"Lakshya")
l1.insert(3,"saurabh")
print(l1)

# l1.pop() # last element deleted  
l1.pop(0) # works on index

l1.remove("Lakshya")
l1.append([3,4,5])
l1[3].remove(3)
print(l1)

l1.reverse()
print(l1)

l2 = [3,4,5,6,3,5,67,2,0]
l2.sort()
print(l2)

l3 = ["lakshya", "saurabh", "pawan"]
l3.sort()
print(l3)

l2.sort(reverse=True) #reverse
print(l2)

print(l3.index("lakshya"))

l4 = [3,4,5,6]
l4[0] = 30
print(l4)

s = "laakshya"
s.replace("l", 'a')
print(s) # --> laakshya nvz str is immutable

# Tuples

t = (2,3,4,5,"lakshya",45.56,False, 45+456j, [2,3,4])
print(t)

# print(type(t))
print(len(t))
print(t[0])
print(t[::-1])
print(t.count(5))
print(t.index(False))

# Sets

# s2 = {2,3,4,5}
# print(type(s2))
s2 = {2,3,4,5,"lakshya",45.56,False, 45+456j, (2,3,4)}
print(s2)

s3 = {2,3,4,2,4,5,6,6,5,4,3,3,2,4,5,6,5,4,2,1,4,6,7,8,9,6,5,4,}
print(s3)

# print(s3[::-1])

s4 = {12,2,23,234,342,4,45,456,567,789,'abc'}
s4.remove(2)
print(s4)













