def intro():
    print("\n------ CS112: COMPUTER PROGRAMMING 1 ------\n"
          "Created by: Kurt Andre L. Olaer\n")
    print("Type [1] to find the smallest factor of n\n"
          "Type [2] to find the prime numbers of range\n"
          "Type [3] to terminate program\n")
    while True:
        try:
            selection = int(input("Choose an option: "))
            if 1 <= selection <= 3:
                break
            else:
                print("Invalid input. Choose only between [1] or [2]\n")
        except ValueError:
            print("Invalid input. Choose only between [1] or [2]\n")

    if selection == 1:
        opt1()
    elif selection == 2:
        opt2()
    else:
        print("\n- Program Terminated -")
        exit()


def input_again():
    while True:
        try:
            response = int(input("[1] To input again, [2] To change function, [3] To terminate program\n"
                                 "Choose an option: "))
            if 1 <= response <= 3:
                break
            else:
                print("Invalid input. Please choose between [1], [2], or [3].\n")
        except ValueError:
            print("Invalid input. Please choose between [1], [2], or [3].\n")

    if response == 1:
        print("")
    elif response == 2:
        print("")
        intro()
    else:
        print("\n- Program Terminated -")
        exit()


def opt1_input():
    while True:
        try:
            num = int(input("Enter an integer greater than or equal to 2: "))
            if num >= 2:  # Check if the number is less than or greater than 2
                return num
            else:
                print("Invalid input. Enter a number greater than or equal to 2.\n")
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")


def opt1_factor(n):
    # Check for divisibility from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i  # Found a factor
    return n  # If no factor is found, n is a prime number


def opt1():
    while True:
        opt1_number = opt1_input()
        opt1_result = opt1_factor(opt1_number)
        print("The smallest factor of", str(opt1_number), "other than 1 is", str(opt1_result), "\n")
        input_again()


def opt2_input():
    while True:
        try:
            while True:
                start_input = int(input("Enter a number [start]: "))
                if start_input <= 0:
                    print("Enter a non-negative number.\n")
                else:
                    break
            while True:
                end_input = int(input("Enter a number [end]: "))
                if end_input <= start_input:
                    print("Enter a number greater than " + str(start_input) + ".\n")
                else:
                    break

            return start_input, end_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")


def opt2_check_primes(value):  # Check if the number is a prime number
    if value < 2:
        return False
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            return False
    return True


def opt2_primes(start_value, end_value, primes_per_line=10, width=4):
    primes_list = []
    for num in range(start_value, end_value + 1):
        if opt2_check_primes(num):
            primes_list.append(num)

    print(f"\nPrime numbers between {start_value} and {end_value} are:")

    # Unpack and print primes_list with right-aligned formatting
    for i in range(0, len(primes_list), primes_per_line):
        line = primes_list[i:i + primes_per_line]
        formatted_line = [str(prime).rjust(width) for prime in line]
        print(", ".join(formatted_line))

    print("")


def opt2():
    while True:
        start_value, end_value = opt2_input()
        opt2_primes(start_value, end_value, primes_per_line=10, width=4)
        input_again()


if __name__ == "__main__":
    intro()
