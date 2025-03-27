def factorial():
    print("Welcome to the Factorial Calculation Program!")
    while True:
        try:
            n = int(input("Which factorial would you like to calculate? "))
            if n >= 0:
                break
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")

    result = 1
    for i in range(1, n + 1):
        result *= i

    print(f"The factorial of {n} is {result}")

# Call the function to run the program
factorial()
