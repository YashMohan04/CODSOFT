print("choose an operation:")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
    result = num1 + num2
    print("Result:", result)
elif choice == '2':
    result = num1 - num2
    print("Result:", result)
elif choice == '3':
    result = num1 * num2
    print("Result:", result)
elif choice == '4':
    if num2 == 0:
        print("Error! Division by zero.")
    else:
        result = num1 / num2
        print("Result:", result)
else:
    print("Invalid input")
