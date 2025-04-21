# Ashley's Python Calculator

# add function
def add(x, y):
    return x + y

# subtract function
def subtract(x, y):
    return x - y

# multiply function
def multiply(x, y):
    return x * y

# divide function
def divide(x, y):
    return x / y

print("choice of operation.")
print("1. Add")
print("2. Subtract")
print("3.Multiply")
print("4. Divide")

while True:
    # user input
    choice = input("Choose between(1/2/3/4): ")

    # check choice
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input(" First number is: "))
            num2 = float(input("second number is: "))
        except ValueError:
            print("Wrong input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2 "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", mulitply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # Check for another operation
        # break while loop if no more calculations need to happen
        next_calculation = input("Another Calculation? (yes/no): ")
        if next_calculation == "no":
            break
        else:
            print("Wrong input")
