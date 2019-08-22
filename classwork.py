### Problem 1:
#Write some Python code that has three variables called ```greeting```, ```my_name```, and ```my_age```. Intialize each of the 3 variables with an appropriate value, then rint out the example below using the 3 variables and two different approaches for formatting Strings.

#1) Using concatenation and the ```+``` and 2) Using an ```f-string```. Sample output:
#YOUR_GREETING_VARIABLE YOUR_NAME_VARIABLE!!! I hear that you are YOUR_MY_AGE_VARIABLE today!

#greeting = "hello"
#my_name = "marcus"
#my_age = 39

#print(f"{greeting} {my_name}!!! I hear that you are {my_age} today")

#print(greeting + " " + my_name + "!!! I hear that you are " + str(my_age) + " today")

### Problem 2:
#Write some Python code that asks the user for a secret password. Create a loop that quits with the user's quit word. If the user doesn't enter that word, ask them to guess again.

userInput = input("enter a password")
userInput2 = input("enter password again")
while userInput != userInput2 and userInput2 != "q":
    userInput2 = input("enter password again or q to quit")

### Problem 3:
#Write some Python code using ```f-strings``` that prints 0 to 50 three times in a row (vertically).

#for i in range(0, 50 +1, 1):
 #   print(f"{i} {i} {i}")

### Problem 4:
#Write some Python code that create a random number and stores it in a variable. Ask the user to guess the random number. Keep letting the user guess until they get it right, then quit.
#import random
#randomNum = random.randint(1, 10 + 1)
#userInput = 0

#while userInput != randomNum:
   # userInput = int(input("guess the random number"))



