#Tyler Harbert

# math_operations.py

def divide_numbers(a, b):
    """Divides two numbers and returns the result."""
    try:
        return a / b  # Potential division by zero error
    except ZeroDivisionError:
        print("Cannot divide by 0.")
        quit()
        

def multiply_number(a,b):
    """Mutlplies two numbers"""
    return a * b

if __name__ == "__main__":
    x = 10
    y = 0
    result = divide_numbers(x, y)
    print(f"The result of division is: {result}")

    a = 10
    b = 5
    result = multiply_number(a, b)
    print(f"The result of multiply is: {result}")
