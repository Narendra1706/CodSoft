# Task - 2 CALCULATOR

while True:
    print("\nSimple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == '1':
            result = num1 + num2
            operation = '+'
        elif choice == '2':
            result = num1 - num2
            operation = '-'
        elif choice == '3':
            result = num1 * num2
            operation = '*'
        elif choice == '4':
            if num2 == 0:
                result = "Error! Division by zero."
                operation = '/'
            else:
                result = num1 / num2
                operation = '/'

        if isinstance(result, str):
            print(result)
        else:
            print(f"{num1} {operation} {num2} = {result}")
    else:
        print("Invalid choice! Please select a valid operation.")
