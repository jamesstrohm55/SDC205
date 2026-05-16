name = input("Please enter your name: ")
student_id = input("Please enter your Student ID: ")

while True:
    try:
        num1 = int(input("Enter the first whole number: "))
        num2 = int(input("Enter the second whole number: "))
        if num1 == num2:
            print("The two numbers must be different. Please try again.\n")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter whole numbers only.\n")

addition = num1 + num2
multiplication = num1 * num2
division = num1 / num2

print("\n--- Calculation Results ---")
print(f"{num1} + {num2} = {addition:.2f}")
print(f"{num1} * {num2} = {multiplication:.2f}")
print(f"{num1} / {num2} = {division:.2f}")

print("\n--- Number Comparison ---")
if num1 > num2:
    print(f"The first number ({num1}) is larger than the second number ({num2}).")
else:
    print(f"The first number ({num1}) is smaller than the second number ({num2}).")

print("\n--- User Information ---")
print(f"Name: {name}")
print(f"Student ID: {student_id}")
