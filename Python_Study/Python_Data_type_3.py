

# # Pithon 이라는 문자열을 임시적인 방법으로 Python 봐꾸기
# A = "Pithon"
# AA = A[:1] + 'y' + A[2:]
# print(AA)

# # Python


# # 문자열 포매팅 따라 하기
# # 숫자 바로 대입
# A = "I eat %d apples." % 3
# print(A)

# # I eat 3 apples.

# # 문자열 바로 대입
# B = "I eat %s apples." % "Five"
# print(B)

# # I eat Five apples.

# # 숫자 값을 나타내는 변수로 대입
# Number = 3
# A = "I eat %d apples." % Number
# print(A)

# # I eat 3 apples.

# # 2개 이상의 값 넣기
# Number = 10
# Day = "Three"
# A = "I ate %d apples. So I was sick for %s Days." % (Number, Day)
# print(A)

# # I ate 10 apples. So I was sick for Three Days.


# # 정렬과 공백
# A = "%10s" % "Hi"
# print(A)

# #         Hi

# B = "%-10sJane." % "Hi"
# print(B)

# # Hi        Jane.


# # 소숫점 표현하기
# A = "%0.4f" % 3.42134234
# print(A)

# # 3.4213

# B = "%10.4f" % 3.42134234
# print(B)

# #     3.4213


# # format 함수를 사용한 포매팅
# A = "I eat {0} Apples".format(3)
# print(A)

# # I eat 3 Apples

# B = "I eat {0} Apples".format("Five")
# print(B)

# # I eat Five Apples

# number = 3
# C = "I eat {0} Apples".format(number)
# print(C)

# A = "I ate {Number} Apples. So I was sick for {Day} day.".format(Number = 10, Day = 3)
# print(A)

# # I ate 10 Apples. So I was sick for 3 day.


# # 왼쪽 정렬
# A = "{0:<10}".format("Hi")
# print(A)

# # Hi        

# # 오른쪽 정렬
# B = "{0:>10}".format("Hi")
# print(B)

# #         Hi

# # 가운데 정렬
# C = "{0:^10}".format("Hi")
# print(C)

# #    Hi

# # 공백 채우기
# D = "{0:=^10}".format("Hi")
# print(D)

# # ====Hi====

# E = "{0:!<10}".format("Hi")
# print(E)

# # Hi!!!!!!!!

# # 소숫점 표현하기
# Y = 3.42134234
# X = "{0:0.4f}".format(Y)
# print(X)

# # 3.4213


# # { 또는 } 문자 표현하기
# A = "{{ and }}".format()
# print(A)

# # { and }


# # f 문자열 포매팅
# Name = '홍길동'
# Age = 30
# print(f'나의 이름은 {Name}입니다. 나이는 {Age}입니다.')

# # 나의 이름은 홍길동입니다. 나이는 30입니다.

# Age = 30
# print(f'나는 내년이면 {Age+1}살이 된다.')

# # 나는 내년이면 31살이 된다.


# # 딕셔너리
# D = {'Name':'홍길동', 'Age':30}
# print(f'나의 이름은 {D["Name"]}입니다. 나이는 {D["Age"]}입니다.')

# # 나의 이름은 홍길동입니다. 나이는 30입니다.


# # 문자 개수 세기 (count)
# A = "Hobby"
# print(A.count('b'))

# # 문자열 중의 문자 b의 개수를 돌려준다.
# # 2


# # 위치 알려주기1 (find)
# B = "Python is the best choice"
# print(B.find('b'))
# print(B.find('k'))

# # 문자열 중의 문자 b가 처음으로 나온 위치를 반환한다.
# # 14

# # 만약 찾는 문자나 문자열이 존재하지 않는다면 -1을 반환한다.
# # -1


# # 위치 알려주기2 (index)
# A = "Life is too short"
# print(A.index('t'))
# print(A.index('k'))

# # 문자열 위치를 알려줌
# # 8

# # 앞의 find와 다른점은 찾는 문자나 문자열이 없으면 Error발생
# # Traceback (most recent call last):
# # File "d:\Sources\Python_Study\Python_Study\Python_Data_type_3.py", line 172, in <module>
# #   print(A.index('k'))
# # ValueError: substring not found


# # 문자열 삽입 (join)
# A = ",".join("abcd")
# print(A)

# # a,b,c,d


# # 소문자를 대문자로 바꾸기 (upper)
# A = "Hi"
# print(A.upper())

# # HI


# # 대문자를 소문자로 바꾸기 (lower)
# B = "Hi"
# print(A.lower())

# # hi


# # 왼쪽 공백 지우기(lstrip)
# A = " hi "
# print(A.lstrip())

# # hi


# # 오른쪽 공백 지우기(rstrip)
# A = " hi "
# print(A.rsplit)

# #  hi


# # 양쪽 공백 지우기(strip)
# A = " hi "
# print(A.strip())

# # hi


# # 문자열 바꾸기(replace)
# A = "Life is too short"
# print(A.replace("Life", "Your leg"))

# # Your leg is too short


# # 문자열 나누기(split)
# A = "Life is too short"
# print(A.split())

# # ['Life', 'is', 'too', 'short']

# B = "a:b:c:d"
# print(B.split(':'))

# # ['a', 'b', 'c', 'd']

