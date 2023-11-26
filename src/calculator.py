class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed"
        else:
            return a / b

    def power(self, a, b):
        return a ** b

    def square(self, a):
        return a ** 2


def main():
    calculator = Calculator()

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square")

    while True:
        operation = input("Enter the number of the operation you want to perform: ")

        if operation in ['1', '2', '3', '4', '5', '6']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == '1':
                print("Result: ", calculator.add(num1, num2))
            elif operation == '2':
                print("Result: ", calculator.subtract(num1, num2))
            elif operation == '3':
                print("Result: ", calculator.multiply(num1, num2))
            elif operation == '4':
                print("Result: ", calculator.divide(num1, num2))
            elif operation == '5':
                print("Result: ", calculator.power(num1, num2))
            elif operation == '6':
                print("Result: ", calculator.square(num1))

            next_calculation = input("Do you want to continue calculating? (yes/no): ")
            if next_calculation == "no":
                break
        else:
            print("Invalid input, please try again.")


if __name__ == "__main__":
    main()
