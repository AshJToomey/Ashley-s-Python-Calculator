# Ashley's Python Calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # Prevent division by zero
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

print("Choice of operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Choose between (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
        except ValueError:
            print("Wrong input. Please enter valid numbers.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        next_calculation = input("Another Calculation? (yes/no): ").lower()
        if next_calculation != "yes":
            print("Exiting calculator. Goodbye!")
            break
    else:
        print("Invalid input. Please select 1, 2, 3, or 4.")
