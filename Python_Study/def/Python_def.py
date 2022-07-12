
# 파이썬 함수의 구조

# def 함수명(매개변수):
#      <수행할 문장1>
#      <수행할 문장2>
#      .....


# 간단한 더하기 함수
# def add(a, b):
#     return a + b

# 위의 더하기 함수 사용해 보기
# a = 3
# b = 4
# c = add(a, b)
# print(c)


# 매개변수와 인수
# 매개변수와 인수는 혼용해서 사용되는 헷갈리는 용어이므로 잘 기억
# 매개변수는 함수에 입력으로 전달된 값을 받는 변수를 의미하고
# 인수는 함수를 호출할 때 전달하는 입력값을 의미한다.
# < ex >
# def add(a, b):    # a, b는 매개변수
#     return a + b

# print(add(3, 4))  # 3, 4는 인수



# 입력값과 결괏값에 따른 함수의 형태 #
# 함수는 들어온 입력값을 받아 어떤 처리를 하여 적절한 결괏값을 돌려준다.
# 입력값 ---> 함수 ----> 결과값




# 일반적인 함수
# def 함수이름(매개변수):
#     <수행할 문장>
#     .....
#     return 결과값

# 일반 함수의 전형적인 예
# def add(a, b):
#     result = a + b
#     return result

# a = add(3, 4)
# print(a)
# 출력 : 7




# 입력값이 없는 함수
# def say():
#     return 'Hi'

# 입력값이 없는 함수 사용 예제
# a = say()
# print(a)
# 출력 : Hi




# 결과값이 없는 함수
# def add(a, b):
#     print("%d, %d의 합은 %d입니다." % (a, b, a + b))

# add(3, 4)
# 출력 : 3, 4의 합은 7입니다.




# 입력값도 결괏값도 없는 함수
# def say():
#     print('Hi')

# say();
# 출력 : Hi




# 여러 개의 입력값을 받는 함수 만들기
# def add_many(*args):
#     result = 0
#     for i in args:
#         result = result + i
#     return result

# result = add_many(1, 2, 3)
# print(result)
# 출력 : 6

# result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(result)
# 출력 : 55

# 매개변수입력받는 은어 >> argc : 단독일때   ,   args : 여러개일때

# < ex >
# def add_mul(choice, *args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result = result + i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result = result * i
#     return result

# result = add_mul("add", 1, 2, 3, 4, 5)
# print(result)
# 출력 : 15

# result = add_mul("mul", 1, 2, 3, 4, 5)
# print(result)
# 출력 : 120




# 매개변수에 초깃값 미리 설정하기
# def say_myself(name, old, man = True):
#     print("나의 이름은 %s입니다." % name)
#     print("현제 나이는 %d입니다." % old)
#     if man:
#         print("남자 입니다.")
#     else:
#         print("여자입니다.")

# say_myself("가나다", 25, True)

# 출력 : 나의 이름은 가나다입니다.
#        현제 나이는 25입니다.
#        남자 입니다.