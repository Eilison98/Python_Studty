

# # 문자
# 'A'


# # 문자열
# "Life is too short, You Need Python"
 
# """Life is too short, You Need Python"""

# '''Life is too short, You Need Python '''


# # 문자열에 작은따옴표 (') 포함시키기    # 큰따옴표 (") 사용
# food = "Python's favorite food is perl"
# print(food)


# # 문자열에 큰따옴표 (") 포함시키기      # 작은따옴표 (') 사용
# say = '"Python is very easy." He Says'
# print(say)


# # 백슬래시 (\)를 사용해서 작은따옴표 (')와 큰따옴표 (")를 문자열에 포함시키기
# food = 'Python\'s favorite food is perl'
# say = "\"Python is very easy.\" He Says"
# print(food)
# print(say)


# # 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기
# multiline = "Life is too short\nYou need Python"
# print(multiline)


# 문자열 더해서 연결하기
# head = "Python"
# tail = " is Fun!"
# Concatenation = head + tail
# print(Concatenation)


# # 문자열 곱하기
# A = "Python"
# P = A * 2
# print(P)


# # 문자열 곱하기 응용
# print("=" * 50)
# print("My Program")
# print("=" * 50)

# # 터미널에 출력시
# # ==================================================
# # My Program
# # ==================================================


# # 문자열 길이 구하기
# A = "Life is too Short"
# L = len(A)
# print(L)

# # 터미널에 출력시
# # 17


# # 문자열 인덱싱
# A = "Life is too short, You need Python"
# print(A[3])

# # 파이썬은 0부터 숫자를 센다.
# # 터미널에 출력시
# # e


# # 문자열 인덱싱 활용하기
# A = "Life is too short, You need Python"
# print(A[0])
# # L

# print(A[12])
# # s

# print(A[33])
# # n

# print(A[-1])
# # n

# print(A[-2])
# # o


# # 문자열 슬라이싱
# A = "Life is too short, You need Python"
# B = A[0] + A[1] + A[2] + A[3]
# print(B)

# # 터미널에 출력시
# # Life

# # 좀더 편하게 사용하기
# # 0번방 부터 4번방 앞에까지 출력
# C = A[0:4]
# print(C)

# # 터미널에 출력시
# # Life


# # 슬라이싱으로 문자열 나누기
# A = "19980501Rainy"
# Year = A[:4]
# Day = A[4:8]
# Weather = A[8:]
# print(Year)
# # 1998

# print(Day)
# # 0501

# print(Weather)
# # Rainy

