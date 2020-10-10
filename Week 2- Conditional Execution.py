#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Exercise 3.1

"""""
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use input to read a string and float() to convert the string to a number. 
Do not worry about error checking the user input - assume the user types numbers properly.
"""""

hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

if hrs > 40:
    reg = hrs * rate
    ot = (hrs-40) * (rate * 0.5)
    print ("Pay:",(ot+reg))
else:
    pay = hrs * rate
    print("Pay:",pay)


# In[17]:


#Exercise 3.3

"""""
Write a program to prompt for a score between 0.0 and 1.0. 
If the score is out of range, print an error. 
If the score is between 0.0 and 1.0, print a grade using the following table:
    Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F

If the user enters a value out of range, print a suitable error message and exit. 
For the test, enter a score of 0.85. 
"""""

score = float(input("Enter Score: "))

if 1 > score >= 0.9:
    print("A")
elif 1 > score >= 0.8:
    print("B")
elif 1 > score >= 0.7:
    print("C")
elif 1 > score >= 0.6:
    print("D")
elif 1 > score < 0.6:
    print("F")
else:
    print("Error! Score is out of range. Please try again")


# In[ ]:





# In[ ]:




