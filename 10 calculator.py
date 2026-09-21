# Simple calculator Write a function calculate(a, b, op) where op is one of "+", "-", "*", "/", returning the result. Handle division by zero gracefully.

def calculate(a,b, op):
    match op:
        case "-":
            return a-b
        case "+":
            return a+b
        case "*":
            return a*b
        case "/":
            if b == 0:
                return "Division by 0 not permitted"
            return a/b
    return "Please enter correct operator: + - * /"


print(calculate(5, 0, ""))