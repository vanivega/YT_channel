
# coding: utf-8

# # Methods and Attributes in a Python Class

# In[2]:


"""Part1:init method is a special function which gets called
whenever a new object of that class is instantiated"""

"""In “init” method, we have set the instance variables (self, first, last, sal). 
Self is the instance which means whenever we write self.fname=first, it is same
as emp_1.first=’fname1’. Then we have created instances of employee class 
where we can pass the values specified in the init method. 
This method takes the instances as arguments.
Instead of doing it manually, it will be done automatically now."""

class employee:
    def __init__(self, first, last, pay):
        self.fname=first
        self.lname=last
        self.pay=pay
        self.email=first + '.' + last + '@company.com'
 

#create objects emp_1, emp_2
emp_1=employee('fname1','lname1',350000)
emp_2=employee('fname2','lname2',100000)
print(emp_1.email)
print(emp_2.email)
print(emp_2.pay)
print(emp_2.fname)


# In[13]:


""" Part2:Methods and Attributes in a Python Class"""
"""Define a method called “full name” within a class. 
So each method inside a python class automatically takes the instance 
as the first argument.
This method prints full name and return this instead of 
emp_1 first name and last name.
“self” is used to work with all the instances. 
Therefore to print this every time, we use a method."""

class employee:
    def __init__(self, first, last, sal):
        self.fname=first
        self.lname=last
        self.sal=sal
        self.email=first + '.' + last + '@company.com'
 
    def fullname(self):
            return '{}{}'.format(self.fname,self.lname)
        
        
#create objects emp_1, emp_2
emp_1=employee('fname1','lname1',350000)
emp_2=employee('fname2','lname2',100000)

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(emp_2.fullname())


# In[10]:



""""Part3: There are variables which are shared among all the instances 
of a class. These are called as class variables.
Instance variables can be unique for each instance like 
names, email, sal etc. 
Program: write function to find  the annual rise in the salary.""" 

class employee:
   perc_raise =1.05 # define a class variable
   def __init__(self, first, last, sal):
       self.fname=first
       self.lname=last
       self.sal=sal
       self.email=first + '.' + last + '@company.com'

   def fullname(self):
           return '{}{}{}'.format(self.fname,'*',self.lname)
     
   #function to find annual raise of salary 
   def apply_raise(self):
       self.sal=int(self.sal*self.perc_raise)
       
       
#create objects emp_1, emp_2
emp_1=employee('fname1','lname1',350000)
emp_2=employee('fname2','lname2',100000)

print(emp_1.sal)#salary before raise
emp_1.apply_raise()
print(emp_1.sal)#salary after raise
emp_1.fullname()

