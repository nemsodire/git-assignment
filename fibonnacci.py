def fibonacci():
    print("Welcome to the Fibonacci Sequence Program!")
    while True:
        try:
            n = int(input("How many Fibonacci terms would you like to generate? "))
            if n > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    if n == 1:
        fib_seq = [0]
    elif n == 2:
        fib_seq = [0, 1]
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            next_term = fib_seq[i-1] + fib_seq[i-2]
            fib_seq += [next_term]

    print(f"Fibonacci sequence up to", n, "terms:", fib_seq)

# Call the function to run the program
fibonacci()

    




