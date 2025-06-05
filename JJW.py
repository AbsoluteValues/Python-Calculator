# 자판기 제작
# 4,5,6번 

list_History = list()
dict_History = dict()

def Selection():    # 계산기가 켜지고 가장 먼저 나오는 선택지
    print("선택지")
    print("1. 계산기")
    print("2. 기록 보기")
    print("3. 초기화")
    print("4. 이전 수식 반복")

    choice = int(input("선택할 번호: "))

    return choice

def input_History(num1,num2,sign,result):   # 계산기 사용 시 기록 넣기
    dict_History.update(
        {
            "첫 번째 숫자: ":num1,
            "두 번째 숫자: ":num2,
            "연산 기호: ":sign,
            "결과:":result
        }
    )

    temp = dict_History.copy()

    list_History.insert(0,temp)

    if(len(list_History) > 5):  # 기록 개수
        list_History.pop()   # 가장 마지막 기록 삭제


def show_History():   # 값 저장은 list 속에 Dict 사용하면 될 듯
    for i in range(len(list_History)):
        print(f"{i+1}번째 기록.")
        print(f"{list_History[i]}")

def reset_History():    # list안의 값 초기화
    while(len(list_History)):
        del list_History[0]


def Plus(num1, num2):
    return num1 + num2

def Minus(num1, num2):
    return num1 - num2

def Mul(num1, num2):
    return num1 * num2

def Dev(num1, num2):
    return num1 / num2

def Calculation(num1,num2,sign):
    
    result = 0

    if(sign == "+"):
        result = Plus(num1,num2)
    elif(sign == "-"):
        result = Minus(num1,num2)
    elif(sign == "*"):
        result = Mul(num1,num2)
    elif(sign == "/"):
        result = Dev(num1,num2)
    input_History(num1,num2,sign,result)

    print(f"{num1} {sign} {num2} = {result}")

def input_Cal():
    num1 = 0
    num2 = 0
    sign = "\0"

    num1 = int(input("숫자1 입력: "))
    num2 = int(input("숫자2 입력: "))
    sign = input("연산 기호 입력: ")

    Calculation(num1,num2,sign)

# def input_Cal():
#     list_Equation = list()
#     num1 = 0
#     num2 = 0
#     sign = '\0'
#     temp_Int = 0
#     temp_Str = "\0"

#     list_Equation = input("수식 입력: ")
#     for i in range(len(list_Equation)):
#         if(list_Equation[i] == '+'):
#             sign = '+'
#             temp_Int = i
#             break
#         elif(list_Equation[i] == '-'):
#             sign = '-'
#             temp_Int = i
#             break
#         elif(list_Equation[i] == '*'):
#             sign = '*'
#             temp_Int = i
#             break
#         elif(list_Equation[i] == '/'):
#             sign = '/'
#             temp_Int = i
#             break

#     for i in range(temp_Int-1):       # 기호 앞에 있는 숫자 받기
#         temp_Str += list_Equation[i]
#     # num1 = int(temp_Str)
#     print(int(temp_Str))

#     temp_Str = "\0"

#     for i in range(temp_Int + 1,len(list_Equation)):    # 기호 뒤에 있는 숫자 받기
#         temp_Str += list_Equation[i]
#     # num2 = int(temp_Str)
#     print(int(temp_Str))

#     return num1, num2, sign


def repeat_Cal():   # 이전 수식 반복
    num1 = dict_History["결과:"]
    num2 = dict_History["두 번째 숫자: "]   # 가해지는 숫자
    sign = dict_History["연산 기호: "]   # 연산 기호
    
    Calculation(num1,num2,sign)

def main():
    select = 0

    while(True):
        select = Selection();    

        if(select == 1):
            # num1 = 0
            # num2 = 0
            # sign = "\0"

            # num1 = int(input("숫자1 입력: "))
            # num2 = int(input("숫자2 입력: "))
            # sign = input("연산 기호 입력: ")

            # Calculation(num1,num2,sign)
            # num1,num2,sign = input_Cal()
            # Calculation(num1,num2,sign)
            input_Cal()
        elif(select == 2):
            show_History()
        elif(select == 3):
            reset_History()
        elif(select == 4):
            repeat_Cal()

        else:
            print("not correct Number")
            print("try again")


if(__name__=="__main__"):
    main()
