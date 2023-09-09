''' 
l = [1,2,3,4,5]
for i in l:
    print(i, type(i))

l1 = ["lakshya", 'krishna', 'Saurabh']
for i in l1:
    print(i)
print("''''For else Loop'''' ")
for i in l1:
    print(i) #if for loop successfully executed then else will execute
else :
    print("Do something")  

print("''''Break''''")
for  i in l1:
    if i == "krishna":
        break
    print(i)

print("''''Break with For Else''''")
for i in l1:
    if i == "Saurabh":
        break
    print(i)
else : 
    print("Execute this if for loop is able to complete itself")

print("''''Continue''''")
for i in l1:
    if i == "krishna":
        continue
    print(i)
else : 
    print("Execute this if for loop is able to complete itself")

print("''''Range function''''")

print(list(range(0,5)))
print(list(range(0,20,2)))
print(list(range(-10,0,2)))

for i in range(len(l1)):
    print(l1[i])

print("''''L3 list Reverse''''")
l3 = [1,2,3,5,6]
for i in range(len(l3)-1,-1,-1):
    print(l3[i])

print("''''L1 list Reverse''''")
for i in range(len(l1)-1,-1,-1):
    print(l1[i])

print("''''Only even index print''''")
l2 = [23,4,4,32,4,5,7,65,43,2,5,5,4,32,11]
for i  in range(0,len(l2),2):
    print(l2[i])

print("''''Sum of all elements''''")
l = [1,2,3,4,5,5,7,8]
result = 0 
for i in l:
    result = result + i
print(result)

print("''''For Tuples''''")
t = (1,2,2,3,4,5,4,6)
result = 0
for i in t:
    result = result + i
print(result)

print("''''For sets''''")
s = {1,2,3,4,5}
for i in s:
    print(i)

print("''''For string''''")
s1 = "PWSKILLS"
for i in s1:
    print(i)

print("''''Dictionaries''''")
d = {"name" : "Lakshya", "Class" : "Data Science", "Topic" : ["Python", "Stats", "Machine Learning", "DL", "CV"]}
for i in d.keys() :
    print(i)
for i in d.values() :
    print(i)
for i in d.items() :
    print(i)
'''

# While Loop

a = 1
while a <= 10:
    print(a)
    a = a + 1

''' print("''''Sum up the number till some point'''''")
n = int(input("Enter your range\n"))
starting_point = 0
count = 1
while count <= n:
    starting_point += count
    count += 1
print(starting_point) '''

'''print("''''Factorial'''''")
n = int(input("Enter your number\n"))
fact = 1
while n > 0:
    fact = fact * n
    n = n - 1
print(fact)
'''

'''print("''''Fibonaaci Series''''")
n = int(input("Enter the number \n"))
a,b = 0,1
count = 0
while count < n:
    print(a)
    c = a + b
    a = b 
    b = c
    count = count + 1
'''

''' print("''''String Reverse''''")
# s = "SUdh"
word = input("String enter\n")
reverse = ""
length = len(word)
while length > 0:
    reverse = reverse + word[length - 1]
    length = length - 1
print(reverse) '''

'''print("''''Table of number''''")
n = int(input("ENter your no.\n"))
i = 1
while i <= 10:
    result = n * i 
    print(f"{n} * {i} = {result}")
    i = i + 1'''

'''print("''''While else''''")
n = 5 
i = 1
while i < n:
    print(i)
    i = i + 1
else :
    print("THIs will be executed when while executed successfully")
    '''

'''print("''''While else break''''")
n = 5 
i = 1
while i < n:
    print(i)
    if i == 3:
        break
    i = i + 1
else :
    print("THIs will be executed when while executed successfully")
    '''
