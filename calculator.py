from fractions import Fraction

def add(x, y) :
    return x + y

def substract(x, y) :
    return x - y

def multiply(x, y) :
    return x * y

def divide(x, y) :
    if (y == 0) :
        return "0으로 나눌 수 없습니다."
    return x / y

def absolute(x) :
    if (x >= 0) :
        return x
    else :
        return -x

def userInput() :
    value = input("입력(숫자 연산자 숫자 / C / = / history / exit) : ").strip()

    if (value.lower() == "c") :
        return None, "C", None
    elif (value == "=") :
        return None, "=", None
    elif (value.lower() == "history") :
        return None, "history", None
    elif (value.lower() == "exit") :
        return None, "exit", None
    else :
        valueList = value.split()

        if (len(valueList) == 3) :
            try :
                x = float(valueList[0])
                operator = valueList[1]
                y = float(valueList[2])
                return x, operator, y
            except :
                print("올바른 숫자 형식을 사용해주세요.")
                return None, None, None
        elif (len(valueList) == 2 and valueList[1].lower() == "abs") :
            try :
                x = float(valueList[0])
                return x, "abs", None
            except :
                print("절댓값은 숫자 하나만 입력해주세요.")
                return None, None, None
        else :
            print("형식이 올바르지 않습니다.")
            return None, None, None
        
def calculate(x, operator, y) :
    if (operator == "+") :
        return add(x, y)
    elif (operator == "-") :
        return substract(x, y)
    elif (operator == "*") :
        return multiply(x, y)
    elif (operator == "/") :
        return divide(x, y)
    elif (operator == "abs") :
        return absolute(x)
    else :
        return "지원하지 않는 연산자입니다."

def printResult(result) :
    print(f'결과 : {result}')

    print(f'분수 표현 : {Fraction(result).limit_denominator()}')

def main() :
    value = 0

    history = []

    while True :
        x, operator, y = userInput()

        if (operator == "exit") :
            print("계산기 프로그램을 종료합니다.")
            break
        elif (operator == "C") :
            x = None
            operator = None
            y = None
            value = None

            history.clear()

            print("계산 기록 초기화")
            continue
        elif (operator == "=") :
            if (not history) :
                print("계산 기록이 없습니다.")
            else :
                temp = history[0].split(" ")
                x = float(temp[-1])
                y = float(temp[2])
                operator = temp[1]
                value = calculate(x, operator, y)
        elif (operator == "history") :
            if (not history) :
                print("계산 기록이 없습니다.")
            else :
                print("최근 계산 기록(최대 5개) : ")
                i = 1
                for v in history[-5:] :
                    print(f'{i}. {v}')
                    i += 1
            continue
        elif (x == None) :
            continue
        
        if (operator != "=") :
            value = calculate(x, operator, y)

        if (type(value) == str) :
            print(value)
            continue

        result = 0
        if (operator == "abs") :
            result = f'{operator}({x})'
        else :
            result = f'{x} {operator} {y}'

        if (operator != "abs" and value != None) :
            history.insert(0, f'{result} = {value}')

        if (len(history) > 5) :
            history.pop()
        
        if (value != None) :
            printResult(value)

if (__name__ == "__main__") :
    main()
