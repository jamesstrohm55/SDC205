# functionOne() prints the Student ID and returns nothing.
def functionOne():
    print("My Student ID is jamstr4441.")


# functionTwo() asks for two numbers, prints their sum, and returns the sum.
def functionTwo():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    total = num1 + num2
    print("The sum of", num1, "and", num2, "is", total)
    return total


# functionThree() checks the sum against 5 and returns the numeric part of the Student ID.
def functionThree(theSum):
    if theSum > 5:
        print("The sum is greater than 5.")
    else:
        print("The sum is 5 or less.")
    return 4441


def main():
    functionOne()                                  # Call functionOne() to display the Student ID.
    theSum = functionTwo()                          # Call functionTwo() and store the returned sum.
    studentNumber = functionThree(theSum)           # Pass the sum to functionThree() and store its return value.
    print("functionThree returned the value of", studentNumber)  # Print the numeric part of the Student ID.


main()  # Start the program by calling main().
