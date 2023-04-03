3
# SRP: Calculator class has single responsibility of performing mathematical operations
class Calculator:
    def __init__(self, operation):
        self.operation = operation

    def calculate(self, x, y):
        return self.operation.operate(x, y)

# OCP, LSP: Mathematical operations are implemented as separate classes that implement the same interface
class Operation:
    def operate(self, x, y):
        pass

class Addition(Operation):
    def operate(self, x, y):
        return x + y

class Subtraction(Operation):
    def operate(self, x, y):
        return x - y

class Multiplication(Operation):
    def operate(self, x, y):
        return x * y

class Division(Operation):
    def operate(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y

# ISP: Operation interface only exposes the methods necessary for it to function correctly
class InputHandler:
    def getOperands(self):
        pass

class ConsoleInputHandler(InputHandler):
    def getOperands(self):
        x = int(input("Enter the first number : "))
        y = int(input("Enter the second number : "))
        return (x, y)

class ResultDisplayer:
    def displayResult(self, result):
        pass

class ConsoleResultDisplayer(ResultDisplayer):
    def displayResult(self, result):
        print("The result is:", result)

# DIP: Calculator class depends on abstractions, not on concrete implementations
if __name__ == "__main__":
    operationCode = int(input("Choose the operation 1 - Addition, 2 - Subtraction, 3 - Multiplication, 4 - Division : "))
    if operationCode == 1:
        operation = Addition()
    elif operationCode == 2:
        operation = Subtraction()
    elif operationCode == 3:
        operation = Multiplication()
    elif operationCode == 4:
        operation = Division()
    else:
        print("Invalid opeation!")
        exit(0)
    calculator = Calculator(operation)
    inputHandler = ConsoleInputHandler()
    resultDisplayer = ConsoleResultDisplayer()
    operands = inputHandler.getOperands()
    result = calculator.calculate(operands[0], operands[1])
    resultDisplayer.displayResult(result)
