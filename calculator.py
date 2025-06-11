from fractions import Fraction

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "오류: 0으로 나눌 수 없습니다."
    return x / y

def absolute(x):
    return abs(x)

def user_input():
    user_in = input("입력 (형식: 숫자 연산자 숫자 / C / = / history / exit): ").strip()

    if user_in.lower() == "c":
        return "C", None, None
    elif user_in == "=":
        return "=", None, None
    elif user_in.lower() == "history":
        return "history", None, None
    elif user_in.lower() == "exit":
        return "exit", None, None
    else:
        parts = user_in.split()
        if len(parts) == 3:
            try:
                num1 = float(parts[0])
                operator = parts[1]
                num2 = float(parts[2])
                return num1, operator, num2
            except:
                print("입력 오류: 올바른 숫자 형식을 사용해주세요.")
                return None, None, None
        elif len(parts) == 2 and parts[1].lower() == "abs":
            try:
                num1 = float(parts[0])
                return num1, "abs", None
            except:
                print("입력 오류: 절댓값은 숫자 하나만 입력해주세요.")
                return None, None, None
        else:
            print("입력 오류: 형식이 올바르지 않습니다.")
            return None, None, None

def calculate(num1, operator, num2):
    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return subtract(num1, num2)
    elif operator == "*":
        return multiply(num1, num2)
    elif operator == "/":
        return divide(num1, num2)
    elif operator == "abs":
        return absolute(num1)
    else:
        return "오류: 지원하지 않는 연산자입니다."

def print_result(result):
    print(f"결과: {result}")
    if isinstance(result, float) and not result.is_integer():
        try:
            frac = Fraction(result).limit_denominator()
            print(f"분수 표현: {frac}")
        except:
            pass

def main():
    history = []
    last_num1, last_op, last_num2 = None, None, None

    while True:
        num1, operator, num2 = user_input()

        if num1 == "exit":
            print("계산기를 종료합니다.")
            break

        elif num1 == "C":
            history.clear()
            last_num1, last_op, last_num2 = None, None, None
            print("계산 초기화 완료.")
            continue

        elif num1 == "=":
            if last_op is None:
                print("이전 수식이 없습니다.")
                continue
            num1, operator, num2 = last_num1, last_op, last_num2
            print(f"이전 수식 반복: {num1} {operator} {num2}")

        elif num1 == "history":
            if not history:
                print("계산 기록이 없습니다.")
            else:
                print("최근 계산 기록 (최대 5개):")
                for i, h in enumerate(history[-5:], start=1):
                    print(f"{i}. {h}")
            continue

        elif num1 is None:
            continue

        result = calculate(num1, operator, num2)

        if isinstance(result, str) and result.startswith("오류"):
            print(result)
            continue

        print_result(result)

        # 기록 저장
        expr_str = f"{num1} {operator} {num2}" if operator != "abs" else f"{operator}({num1})"
        result_str = f"{result}"
        history.append(f"{expr_str} = {result_str}")
        if len(history) > 5:
            history.pop(0)

        # 마지막 연산 저장
        if operator != "abs":
            last_num1, last_op, last_num2 = num1, operator, num2
        else:
            last_num1, last_op, last_num2 = num1, "abs", None

if __name__ == "__main__":
    main()
