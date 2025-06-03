# Ashley's Python Calculator

import tkinter as tk
from tkinter import ttk, messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        else:
            result = "Please select an operation."

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# GUI Setup
root = tk.Tk()
root.title("Ashley's Python Calculator")
root.geometry("350x300")
root.config(bg="#f5f5f5")
root.resizable(False, False)

# Title Label
tk.Label(root, text="Ashley's Calculator", font=("Arial", 16, "bold"), bg="#f5f5f5").pack(pady=10)

# Input Frame
input_frame = tk.Frame(root, bg="#f5f5f5")
input_frame.pack(pady=5)

tk.Label(input_frame, text="First Number:", bg="#f5f5f5").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry1 = tk.Entry(input_frame, width=15)
entry1.grid(row=0, column=1, pady=5)

tk.Label(input_frame, text="Second Number:", bg="#f5f5f5").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry2 = tk.Entry(input_frame, width=15)
entry2.grid(row=1, column=1, pady=5)

# Operation Dropdown
operation_var = tk.StringVar()
operation_var.set("Select Operation")

operation_dropdown = ttk.Combobox(root, textvariable=operation_var, values=["Add", "Subtract", "Multiply", "Divide"], state="readonly", width=20)
operation_dropdown.pack(pady=10)

# Calculate Button
tk.Button(root, text="Calculate", command=calculate, bg="#4caf50", fg="white", width=20).pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Result: ", font=("Arial", 12), bg="#f5f5f5")
result_label.pack(pady=10)

# Run the GUI
root.mainloop()