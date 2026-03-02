import math

class Calculator:
    @staticmethod
    def greet():
        print("Hello!")
    def square(x):
        return x*x
    def cube(x):
        return x*x*x
    def squrt(x):
        return math.sqrt(x)

Calculator.greet()
n = int(input("Enter number: "))

print(f"Square: {Calculator.square(n)}")
print(f"Cube: {Calculator.cube(n)}")
print(f"Square root: {Calculator.squrt(n)}")