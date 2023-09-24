f = open('test.txt','w') # File Creation

f.write("This is my first file to write") # write in File

f.close()

f = open('test.txt','w')
f.write("This is my File") # Truncate krega pehle ka data remove kr k new data file me lana 
f.close() 

# A mode ---> Open For writing and appending new things
f = open('test.txt','a') # data Add ho Gya
f.write("\tHello world")

f = open('test.txt','r')
print(f.read()) # pointer is in last index of stirng

# so we have to use seek function 
f.seek(0) # index --> 0
print(f.readline())

data1 = open('test.txt','r')
for i in data1:
   print(i)

# getting file size in bytes
import os
s = os.path.getsize("test.txt")
print(s)

# Remove file
# os.remove("test.txt")

# Rename
# os.rename("test.txt","new.text")

# Multiple copies creating

import shutil
shutil.copy("test.txt",'copy.txt')

# One more method
with open("test.txt","r") as f:
   print(f.read())

data = {
   "name" : "lakshya",
   "Mail-id" : "abc@gmail.com",
    "subject" : ["data science", "big data", "data analytics"]
}
# This is also called JSON (JavaScript Object Notation)
# How to write JSON file in our new file
import json
with open("data.json","w") as f:
   json.dump(data,f)

with open("data.json", "r") as f:
   print(json.load(f))
   print(data['subject'])

# Comma Separeted value (CSB)

import csv
data = [["name","email_id","Phone"],
        ["lakshya","abc@gmail.com",7365736733],
        ["Saurabh","helo@gmail.com",9176525662]
]

with open ("data.csv","w") as f:
   writer = csv.writer(f)

   for i in data:
      writer.writerow(i)

with open("data.csv",'r') as f:
   readData = csv.reader(f)

   for i in readData:
      print(i)

# Binary Data

with open("test.bin",'wb') as f:
   bin = f.write(b"\x01\x02\x03/x9837625563")

with open ("test.bin","rb") as f :
   print(f.read())

# Buffer Read and write
import io
with open("test1.txt","wb") as f:
   file = io.BufferedWriter(f)

   file.write(b"this is my first line\n")
   file.write(b"this is my  second line")
   file.flush()

with open("test1.txt","rb") as f:
   file = io.BufferedReader(f)
   data = file.read()
   print(data)

# Logging

import logging

# logging.basicConfig(filename = "test.log",level = logging.INFO)
# logging.info("this is my print")
# logging.info("log this line of execution")
# logging.debug("this is myy msg")
# logging.warning("Thiss is my warning MEssage")
# logging.error("Thiss is my ERRor")
# logging.shutdown()
# How to define info

import logging  
# logging.basicConfig(filename = "Hello.log" , level = logging.DEBUG, format = '%(asctime)s %(message)s')
# logging.info("This is my info looging")
# logging.critical("This is my critical looging")
# logging.error("This is my error looging")
# logging.shutdown()

logging.basicConfig(filename='test2.log', level = logging.DEBUG, format= '%(asctime)s %(name)s %(levelname)s %(message)s')
logging.info("This is my info looging")
logging.critical("This is my critical looging")
logging.error("This is my error looging") 

l = [1,2,43,4,5,[3,2,3],"lakshya","kumar"]
l1INT = []
l2str = []
for i in l:
   logging.info("we are iterating throwing our list and our local var is i {}".format(l) )
   if  type(i) == list :
      logging.info("i am inside in if statement and i am trying to check list type" + str(i))
      for j in i:
         logging.info("I am in another for loop for list inside list element " + str(j))
         if type(j) == int:
            logging.info("I am inside if statement")
            l1INT.append(j)
   elif type(i) == int:
      l1INT.append(i)
   else : 
      if type(i) == str:        
         l2str.append(i)
logging.info(f"my final result for int is {l1INT} and str is {l2str}")
















