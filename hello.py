def add(x, y) :
    return x + y

def subtract(x, y) :
    return x - y

def multiply(x, y) :
    return x * y

def divide(x, y) :
    return x / y

def user_input():
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    operator = input("연산자를 입력하세요 (+, -, *, /): ")
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    return num1, operator, num2

def calculate(num1, operator, num2) :
    if(operator == "+") :
        return add(num1, num2)
    if(operator == "-") :
        return subtract(num1, num2)
    if(operator == "*") :
        return multiply(num1, num2)
    if(operator == "/") :
        return divide(num1, num2)

def main() :
    while(1) :
        num1, operator, num2 = user_input()
        res = calculate(num1, operator, num2)
        print(f"{res}")

if(__name__ == "__main__") :
    main()