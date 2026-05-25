# James Strohm
# May 24, 2026
# SDC205 - Assignment 2.7: Number Guessing Game
# This program greets the user by name, then challenges them to guess
# a secret number between 1 and 10. After a correct guess, a while loop
# and a for loop each display the guessed value incremented by 1, five times.

userName = input("Please enter your name: ")
studentId = input("Please enter your Student ID: ")

print(f"\nHello, {userName}! Welcome to the number guessing game.")
print(f"Student ID: {studentId}")

secretNumber = 5
numTries = 0

print("\nI am thinking of a number between 1 and 10. Can you guess what it is?")

userGuess = 0
while userGuess != secretNumber:
    userGuess = int(input("\nEnter your guess (1-10): "))
    numTries += 1

    if userGuess > secretNumber:
        print("Too high! Try again.")
    elif userGuess < secretNumber:
        print("Too low! Try again.")
    else:
        print(f"\nCongratulations, {userName}! You guessed the correct number!")

print(f"\nIt took you {numTries} {'try' if numTries == 1 else 'tries'} to guess correctly.")
print(f"Student ID: {studentId}")

print("\n--- Output from the 'while' loop: ---")
whileValue = userGuess
whileCount = 0
while whileCount < 5:
    incrementedValue = whileValue + 1
    print(f"{whileValue} incremented by 1 is {incrementedValue}")
    whileValue = incrementedValue
    whileCount += 1

print("\n--- Output from the 'for' loop: ---")
forValue = userGuess
for i in range(5):
    incrementedValue = forValue + 1
    print(f"{forValue} incremented by 1 is {incrementedValue}")
    forValue = incrementedValue
