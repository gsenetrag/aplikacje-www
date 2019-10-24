class Calculator:
    def add(a, b):
        return a + b
    
    def difference(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a / b


class ScienceCalculator(Calculator):
    def exponentiation(a, b):
        return a ** b

    def roots(a, b):
        return a ** (1 / b)


print(Calculator.divide(5,10))
print(ScienceCalculator.exponentiation(5,3))
print(ScienceCalculator.roots(16,4))