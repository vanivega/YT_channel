
# coding: utf-8

# In[11]:


#create class without attributes and methods
class employee:
   #first #class variable
 pass



#instantiate the class. Create objects emp_1 and emp_2   
emp_1=employee()
emp_2=employee()
   
#instance variable can be created manually
emp_1.first='fname1'
emp_1.last='lname1'
emp_1.email='xyz@email.com'
emp_1.pay=10000

emp_2.first='fname2'
emp_2.last='lname2'
emp_2.email='abc@email.com'
emp_2.pay=20000
   
print(emp_1.email)
print(emp_2.email)
   
"""This code manually sets the variables.
   You will see a lot of code and also it is prone to error. 
   So to make it automatic, we can use “init” method. 
   For that, let’s understand what exactly are methods 
   and attributes in a python class."""

