def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")

while True:
        operation = input("\nChoose an operation (or q to quit): ").strip()

if operation.lower() == "q":
            print("Goodbye!")
            break

if operation not in ("+", "-", "*", "/"):
            print("Invalid operation. Choose +, -, *, or /.")
            continue

try:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

if operation == "+":
            result = number1 + number2
        elif operation == "-":
            result = number1 - number2
        elif operation == "*":
            result = number1 * number2
        else:
            if number2 == 0:
                print("Error: Cannot divide by zero.")
                continue
            result = number1 / number2

print(f"Result: {number1} {operation} {number2} = {result}")

if __name__ == "__main__":
    calculator()
