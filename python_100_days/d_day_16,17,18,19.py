'''
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


'''



'''

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

    
'''



'''

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
        
'''


#Functions