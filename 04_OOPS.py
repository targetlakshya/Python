a = 1
print(type(a)) # class 'int'
b = "pwskills"
print(type(b)) # class 'string'
print(type([82.2,4,4,32,2])) # class 'list'

# How to make a class in python

class test :
    pass # Blank class creation

a = test()
print(type(a))

class pwskills :
    def welcome_msg(self) :
        print("Welcome to PW skills")
rohan = pwskills()
print(type(rohan))
rohan.welcome_msg()
gaurav = pwskills()
gaurav.welcome_msg()

class pwskills1 :   
    def __init__(self, phone_no, email_id, student_id):
        self.phone_number = phone_no
        self.email_id = email_id
        self.student_id = student_id
    def return_student_details(self):
        return self.student_id,self.phone_number,self.email_id
rohan = pwskills1(9859363921,"rohan@gmail.com",101)
print(rohan.email_id)

print(rohan.return_student_details())
gaurav = pwskills1(949826622,'gaurav@gmail.com',1511)
print(gaurav.return_student_details())

# Polymorphism


def test(a,b) :
    return a + b

d = test(3,4)
print(d)
e = test("Sudh" , " Kumar")
print(e)
d = test([1,2,3,4],[4,3,2,2])
print(d)

class data_science:
    def syllabus(self):
        print("This is my syllabysus of data science batch")
    
class web_dev:
    def syllabus(self):
        print("This is my syllabus for web dev")

def class_parcer(class_obj):
    for i in class_obj:
        i.syllabus()
data_science = data_science()
web_dev = web_dev()
class_obj = [data_science, web_dev]
class_parcer(class_obj)

# Encapsulation


class test:
    def __init__(self,a,b) :
        self.a = a
        self.b = b

t = test(32,45)
t.a = 23456
print(t.a)

class car :
    def __init__(self,year,make,model,speed) :
        self.__year = year
        self.__model = model
        self.make = make
        self.__speed = speed

        def set_spped(self,speed):
            self.speed = 0 if speed < 0 else speed
        def get_speed(self):
            return self.speed
c = car(2021,"toyota","innova",12)
print(c._car__model)

print("''''''''Bank account'''''''''''''")
class Bank_account :
    def __init__(self, balance) :
        self.__balance = balance
    def deposit(self,amount) :
        self.__balance = self.__balance + amount
    
    def withdraw (self,amount) :
        if self.__balance >= amount :
            self.__balance = self.__balance - amount
            return True
        else :
            return False
    def get_balance (self) :
        return self.__balance

lakshya = Bank_account(1000)
lakshya.deposit(500)
lakshya.withdraw(600)
print(lakshya.get_balance())


# Inheritance

class test :
    def test_math(self) :
        return "this is my my first class"

class child_test(test) :
    pass

child_test_obj = child_test()
print (child_test_obj.test_math())

# Multilevel Inheritance

class class1 :
    def test_class1(self) :
        return "This is method for class 1" 
class class2(class1) :
    def test_class2(self) :
        return "This is method for class 2"

class class3(class2):
    pass

obj_class3 = class3()
print(obj_class3.test_class1())
print(obj_class3.test_class2())

# Multiple Inheritance

class papa :
    def test_class1(self):
        return "This is papa"

class mumma :
    def test_class2(self):
        return "This is mumma"

class child(papa,mumma) : 
    pass

obj_child = child()
print(obj_child.test_class2())
print(obj_child.test_class1())

# Abstract class

import abc
class pwskills :
    @abc.abstractmethod
    def student_details(self) :
        pass
    @abc.abstractmethod
    def student_assignment(self) :
        pass
    @abc.abstractmethod
    def student_marks(self) :
        pass

class student_details(pwskills) :
    def student_details(self):
        return "This is  method for taking student details"
    def student_assignment(self):
        return "This is  method for taking student assignment"
    def student_marks(self):
        return "This is  method for taking student marks"

class data_science_masters(pwskills) :
    def student_details(self):
        return "this will return a student of data science master"
    def student_assignment(self):
        return "This will return a assignments of data science masters"
    def student_marks(self):
        return "this will return  a marks of student of data science masters"
    
dsm = data_science_masters()
print(dsm.student_assignment())
print(dsm.student_details())

# Decorators
print("'''''decorators'''''")

# def test() :
#     print('This is start of my function')
#     print('This is my function to test')
#     print('This is end of my function')

# test()

def dec(func):
    def inner_dec() :
        print('this is the start of my fun ')
        func()
        print('this is the mid of my func')
        func() 
        print('this is the end of my func')
    return inner_dec

@dec
def test1() :
    print(6+7)

test1()

import time

def timer_test(func):
    def time_test_inner() :
        start = time.time()
        func() 
        end = time.time()
        print(end - start)
    return time_test_inner
    
@timer_test
def test2 () :
    print(45+78)

test2() 

@timer_test
def test3():
    for i in range(1000000):
        pass

test3()

# Class Methods

print("''''Class Methods''''''")

class pwskills :
    def __init__(self,name,email):

        self.name = name
        self.email = email

    def studentts_details (self) :
        print(self.name,self.email)
pw = pwskills("mohan","abc@gmail.com")
print(pw.name)
pw.studentts_details()

# Using @classmethods
print("'''' Using @classmethods''''")
class pwskills2 :
    def __init__(self,name,email):

        self.name = name
        self.email = email
    @classmethod
    def details(cls, name, email):
        return cls(name, email)
    
    def studentts_details (self) :
        print(self.name,self.email)

pw1 = pwskills2.details("Sudh", "Sudh@gmail.com")
print(pw1.name)
print(pw1.email)
pw1.studentts_details()

class pwskills3 :

    mobileNo = 9131252946

    def __init__(self,name,email):

        self.name = name
        self.email = email
    @classmethod
    def change_no(cls, mobile):
        pwskills3.mobileNo = mobile
    @classmethod
    def details(cls, name, email):
        return cls(name, email)
    
    def studentts_details (self) :
        print(self.name,self.email, pwskills3.mobileNo)
pwskills3.change_no(9179380302)
print(pwskills3.mobileNo)
pw_obj = pwskills3("Saurabh","Bac@gmail.com")
pw_obj.studentts_details()

pw = pwskills3.details("rohan","rohan@gmail.com")
pw.studentts_details()

def course_details(cls,course_name) :
    print("Course name is ", course_name)

pwskills3.course_details = classmethod(course_details)
pwskills3.course_details("Data Science")

def mentor(cls, mentor_name):
    print("mentor name is",mentor_name)
pwskills3.mentor = classmethod(mentor)
pwskills3.mentor("Sudhakar Singh")




class pwskills4 :

    mobileNo = 9131252946

    def __init__(self,name,email):

        self.name = name
        self.email = email
    @classmethod
    def change_no(cls, mobile):
        pwskills3.mobileNo = mobile
    @classmethod
    def details(cls, name, email):
        return cls(name, email)
    
    def studentts_details (self) :
        print(self.name,self.email, pwskills3.mobileNo)
# del pwskills4.change_no

# print(pwskills4.change_no(9875352332))
# delattr(pwskills4,"details")
# print(pwskills4.details("Lakshya",'ABX@gmail.com'))
# delattr(pwskills4, "student_details")
# pwskills4.studentts_details()
# delattr(pwskills4,"mobileNo")
# pwskills4.mobileNo

# Static Methods
print("'''''Static Method'''''")

class pwskills :
    def student_details(self, name, mail_id, number):
        print(name, mail_id, number)
pw = pwskills()
pw.student_details("lakshya","abc@gmail.com",9172654244)

class pwskills1 :
    def student_details(self, name, mail_id, number):
        print(name, mail_id, number)

    @staticmethod
    def mentor_class(list_mentor):
        print(list_mentor)
pwskills1.mentor_class(["lakshya","sidh","Anubhav"])
stu1 = pwskills1()
stu2 = pwskills1()
stu3 = pwskills1()

class pwskills2 :
    def student_details(self, name, mail_id, number):
        print(name, mail_id, number)

    @staticmethod #statis method is used to print multiple time one thing
    def mentor_mailid(mail_id_mentor):
        print(mail_id_mentor) 
        
 
    @staticmethod
    def mentor_class(list_mentor):
        pwskills2.mentor_mailid(["sudh@gmail.com","krish@hjakjh.com"])
        print(list_mentor) 
    
    @classmethod
    def class_name(cls) :
        cls.mentor_class(["sudh","Krish"])
    
    def mentor(self,mentor_list):
        print(mentor_list) 
        self.mentor_class(["krish","sudh"])
pwskills2.mentor_class(["krish","sudh"])
pwskills2.class_name()

pw = pwskills2()
pw.mentor(["kanhga","kaj"])


# Special and (magic OR dunder) methods

print("''''''Special and (magic OR dunder) methods''''''")

print(dir(int))
print(dir(str))

a = 100
print(a+5) 

print(a.__add__(5)) # Dunder

class pwskills:

    def __new__(cls):
        print("THis is my new")

    def __init__(self) :
        print("This is my INIT func")
        self.mobile = 98762543567
pw = pwskills()

class pwskills1:

    def __init__(self) :


        self.mobile = 98762543567

    def __str__(self) :
        return "This is my magic call for str"
pw1 = pwskills1()
print(pw1)

# Magic and dunder func is available but it caanot use so wisely bcz internally it is available

# property decorators - Getter and Setter

class pwskills:
    def __init__(self, course_price, course_name) :
        self.__course_price = course_price # _  means protected and __ means private
        self.course_name = course_name
# Private ka acccess user ko dena
    @property
    def course_price_access(self):
        return self.__course_price

    @course_price_access.setter
    def course_price_set(self,price):
        if price <= 3500:
            pass
        else :
            self.__course_price = price
    @course_price_access.deleter
    def delete_course_price(self):
        del self.__course_price

pw = pwskills(3500, "data_science")
# pw.__course_price # it cannnot access
print(pw._pwskills__course_price)
print(pw.course_name)

# Private ka acccess user ko dena
print(pw.course_price_access)
pw.course_price_set = 4500
print(pw.course_price_access) 
del pw.delete_course_price
print(pw.course_price_access) 






 












