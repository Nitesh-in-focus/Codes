#matchcase : similar to switch case in other languages
x = int(input("Enter a number: ")) 
match x:
    case 0 :
        print("x is zero")
    case 1 :
        print("x is one")
    case 2 :
        print("x is two")
    case 3 :
        print("x is three") #break not needed
    case 4 :
        print("x is four")
    case _ if x < 0:  # Default ka Conditional case
        print("x is negative")
    case _ if x > 4:  # Conditional case
        print("x is greater than four")








#For-Loop
name  = "Python"
for i in name:
    print(i, end=' ')
    if i == 't':
        print("\nFound 't' in the string, breaking the loop.")
        break


colors = ["red", "green", "blue", "yellow"]
for x in colors:
    if x == "blue":
        print("Found blue, skipping to next iteration.")
        continue
    print(x)


for k in range(1,20,2): #range(start, stop, step)
    print(k)

    






# While-Loop
i = 6
while i < 5:
    print(i)
    i += 1
else:
    print("Loop completed successfully.") #it runs even if the loop condition is false

# emulate a do-while loop
i = 6
while True:
    print(i)
    i += 1
    if i > 5:
        break
        






#Functions
def calculateGmean(a, b): #fuction definition
    return (a * b) / (a + b)

def calculateHmean(a, b):
    pass #function definition, but no implementation


a = 9
b = 8
gmean = calculateGmean(a, b) #function call
print("gmean of", a, "and", b, "is:", gmean)

c= 10
d = 20
gmean = calculateGmean(c, d)
print("gmean of", c, "and", d, "is:", gmean)


# Function Arguments
def average(a, b): #required arguments
    print("The average is:", (a + b) / 2)
average(10, 20) 



def average1(a=5, b=2): #default arguments
    print("The average1 is:", (a + b) / 2)
average1(a=30) 



def average3(a, b): #keyword arguments
    print("The average3 is:", (a + b) / 2)
average3(b=10, a=20) 



def average4(*numbers): #variable-length arguments
    sum = 0
    for i in numbers:
        sum = sum + i
    print("The average4 is:", sum / len(numbers))
average4(10, 20, 40, 50, 60) 