# Random number Game By "Andy q" text me for suggestions
# 239-961-7723

# Welcome, here we will learn how to make a random generator game

# First we need to make sure the computer knows to make a random number

import random

# Now we set the range for the generation, in this case 1-10

x = random.randint(1,1)

# Next we convert our variable "x" from an integer to a string that way we show
# the user the number that the computer chose after his or her answer

num = str(x)

# Now we set the variable for the user input, in this case the variable "guess"
# Will contain our user input

guess = input('Enter : ')

# Then we have the brain of the operation; here the computer will evaluate if
#the number the user picked is equal to the number the computer chose.

if guess == num:
    print('you guessed it! The answer was : ' + str(x))

    print('Congratz')
else:
    print('Sorry the answer is : ' + str(x))
    
    print('try again')

# Now we run the code
