import random
# Conditional
# Method evaluate data
# if then else

#ask the user to select the upper bound
upperBound = input("what is the upper bound? ")
upperBound = int(upperBound)
#generate a random integer starting at 1 and going to upperBound
randomNumber = random.randint(1, upperBound)
print(randomNumber)

userGuess = None
#start and loop here
while userGuess != randomNumber: 
    #ask the user to guess
    userGuess = input("type a number between 1 and " + str(upperBound) + ": ")
    #check if user guess is = to random number
    if int(userGuess) == randomNumber:
        print("you win!")
        #exit the loop
    #if user guess is not == to random number
    else: 
        print("YOU LOSE!")
print("Game Over")


# high_range = 100
# middle_number = int(high_range/2)
# my_guess = middle_number
# number_guesses = 0
# highOrLow = "lower"
# output = "{} is {} than {}"

# my_random_number = random.randint(1, high_range)

# print(my_random_number)
# print(my_guess)

# #evaluate the radom number and compare it to middle number
# if my_guess < my_random_number:
#     highOrLow = "lower"
# if my_guess > my_random_number :
#     highOrLow = "higher"

# print(output.format(my_guess, highOrLow, my_random_number))