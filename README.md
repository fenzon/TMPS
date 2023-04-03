# TMPS
# Lab_1_TMPS - Calculator App in Python

## by Borta Nicolae
## Task : Build an app that will follow SOLID Principles using an OOP programing language

## General Theory : 
### S - Single Responsibility Principle: a class should have only one reason to change.

### O - Open/Closed Principle: entities should be open for extension but closed for modification.

### L - Liskov Substitution Principle: subtypes must be substitutable for their base types.

### I - Interface Segregation Principle: clients should not be forced to depend on interfaces they do not use.

### D - Dependency Inversion Principle: high-level modules should not depend on low-level modules. Both should depend on abstractions.

### SRP: The Calculator class has a single responsibility of performing mathematical operations.
```
class Calculator:
    def __init__(self, operation):
        self.operation = operation
    def calculate(self, x, y):
        return self.operation.operate(x, y)
```
        
        
### OCP: The mathematical operations are implemented as separate classes that implement the same interface, which allows for easy extension.
### LSP: The mathematical operations are substitutable for each other, as they all implement the same interface and follow the same contract.
```
class Operation:
    def operate(self, x, y):
        pass
class Addition(Operation):
    def operate(self, x, y):
        return x + y
```
### ISP: The InputHandler and ResultDisplayer interfaces only expose the necessary methods for each operation to function correctly.
```
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
```
### DIP: The Calculator class depends on abstractions (Operation interface) rather than concrete implementations, which makes it more flexible and reusable.
```
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
```
