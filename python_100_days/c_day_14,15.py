
# This code demonstrates the use of if-else statements in Python.
# If-else

a = int(input("Enter your age: "))
print("Your age is:", a)

if (a >=18): # If it's true then only this block will execute
    print("You are eligible to vote") #here space is important which is known as indentation
else:
    print("You are not eligible to vote")
print("Thank you for using our service")



#If-elif-else
b = int(input("Enter your marks: "))
if (b >= 90):
    print("Grade A")
elif (b >= 80):
    print("Grade B")
elif (b >= 70):
    print("Grade C")
elif (b >= 60):
    print("Grade D")
else:
    print("Grade F")
print("Thank you for using our service")



#nested if-else
c = int(input("Enter your age: "))
if (c >= 18):
    print("You are eligible to vote")
    if (c >= 21):
        print("You are eligible to drink alcohol")
    else:
        print("You are not eligible to drink alcohol")  
else:
    print("You are not eligible to vote")
print("Thank you for using our service")   

import time
# Good morning, Sir/Madam
timestamp = (time.strftime("%H:%M:%S")) #strft = string from time
print(timestamp)
timestamp1 = int(time.strftime("%H"))
print(timestamp1)
timestamp2 = int(time.strftime("%M"))
print(timestamp2)
timestamp3 = int(time.strftime("%S"))
print(timestamp3)
if int(timestamp1) < 12:
    print("Good morning, Sir/Madam")   
elif int(timestamp1) < 17:
    print("Good afternoon, Sir/Madam")
elif int(timestamp1) < 20:
    print("Good evening, Sir/Madam")     