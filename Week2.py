#!/usr/bin/env python
# coding: utf-8

# # Assignment2
# ## 19.02.2023
# Zhenliang Hao

# In[1]:


var1=100
var2=29
result=(var1+var2)*3
exp2_result=result**2
print("The result of the calculation was:",exp2_result)


# In[ ]:


name = input("JOHN:")
year_of_birth = int(input("1995: "))
age = int(input("26"))
year_digits = str(year_of_birth)[-2:]
name_letters = name[:3]
age_squared = str(age ** 2)
password = year_digits + name_letters + age_squared
print("password:", password)


# In[ ]:


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 % 2 == 0 and num2 % 2 == 0:
print("Both numbers are even.")
elif num1 % 2 == 0 or num2 % 2 == 0:
print("One of the numbers is even.")
print("Both numbers are odd.")


# In[ ]:




