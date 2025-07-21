## 1. Python Code for Adding Two Numbers


# --- Method 1: Direct Addition ---
print("--- Python: Direct Addition ---")
num1_a = 10
num2_a = 5
sum_a = num1_a + num2_a
print(f"The sum of {num1_a} and {num2_a} is: {sum_a}") # Output: The sum of 10 and 5 is: 15

print("\n") # Add a newline for separation

# --- Method 2: Using a Function ---
print("--- Python: Using a Function ---")
def add_numbers(a, b):
  """
  This function takes two numbers as arguments and returns their sum.
  """
  return a + b

# Call the function with specific values
result_b = add_numbers(25, 15)
print(f"The sum of 25 and 15 (using a function) is: {result_b}") # Output: The sum of 25 and 15 (using a function) is: 40

# You can also use variables
x = 7
y = 3
result_c = add_numbers(x, y)
print(f"The sum of {x} and {y} (using a function) is: {result_c}") # Output: The sum of 7 and 3 (using a function) is: 10

print("\n") # Add a newline for separation

# --- Method 3: With User Input ---
print("--- Python: With User Input ---")
try:
  # Get input from the user
  input_str1 = input("Enter the first number: ")
  input_str2 = input("Enter the second number: ")

  # Convert the input strings to numbers (float for decimals, int for whole numbers)
  # Using float() is generally safer as it handles both integers and decimals.
  number1 = float(input_str1)
  number2 = float(input_str2)

  # Calculate the sum
  total = number1 + number2

  # Print the result
  print(f"The sum of {number1} and {number2} is: {total}")

except ValueError:
  print("Invalid input. Please enter valid numbers.")


# ### Explanation for Python Code:

# 1.  **Direct Addition:**
#     *   We define two variables (`num1_a`, `num2_a`) and directly add them using the `+` operator.
#     *   `print(f"...")` uses an f-string, which is a convenient way to embed variables directly into strings.

# 2.  **Using a Function (`def add_numbers(a, b):`)**:
#     *   `def` is used to define a function named `add_numbers`.
#     *   `a` and `b` are parameters (placeholders for the values that will be passed into the function).
#     *   `return a + b` calculates the sum and sends that value back whenever the function is called.
#     *   Functions are good for reusable code.

# 3.  **With User Input (`input()`)**:
#     *   `input("prompt")` displays a message to the user and waits for them to type something and press Enter. Whatever they type is returned as a **string**.
#     *   `float()` (or `int()`) is crucial here. Since `input()` returns a string, you *must* convert it to a number type (`float` for decimals, `int` for whole numbers) before you can perform mathematical operations on it. If you try to add two strings, Python would concatenate them (e.g., "5" + "3" becomes "53").
#     *   `try...except ValueError` is a basic form of error handling. If the user types something that cannot be converted to a number (like "hello"), `float()` would raise a `ValueError`, and the `except` block would catch it and print a friendly message instead of crashing the program.