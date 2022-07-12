
# for문 #

# for문의 기본 구조 #
# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할 문장1
#     수행할 문장2
#     ...



# 예제를 통해 for문 이해하기 #
# 1. 전형적인 for문 #
# >>> test_list = ['one', 'two', 'three'] 
# >>> for i in test_list: 
# ...     print(i)
# ... 
# one 
# two 
# three

# 2. 다양한 for문의 사용 #
# >>> a = [(1,2), (3,4), (5,6)]
# >>> for (first, last) in a:
# ...     print(first + last)
# ...
# 3
# 7
# 11

# 3. for문의 응용 #
# "총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여 주시오." #
# marks1.py
# marks = [90, 25, 67, 45, 80]

# number = 0 
# for mark in marks: 
#     number = number +1 
#     if mark >= 60: 
#         print("%d번 학생은 합격입니다." % number)
#     else: 
#         print("%d번 학생은 불합격입니다." % number)

#C:\doit>python marks1.py
# 1번 학생은 합격입니다.
# 2번 학생은 불합격입니다.
# 3번 학생은 합격입니다.
# 4번 학생은 불합격입니다.
# 5번 학생은 합격입니다.



# for문과 함께 자주 사용하는 range 함수 #
# >>> a = range(10)
# >>> a
# range(0, 10)

# >>> a = range(1, 11)
# >>> a
# range(1, 11)


# range 함수의 예시 살펴보기 #
# >>> add = 0 
# >>> for i in range(1, 11): 
# ...     add = add + i 
# ... 
# >>> print(add)
# 55


# #marks3.py
# marks = [90, 25, 67, 45, 80]
# for number in range(len(marks)):
#     if marks[number] < 60: 
#         continue
#     print("%d번 학생 축하합니다. 합격입니다." % (number+1))



# for와 range를 이용한 구구단 #
# >>> for i in range(2,10):        # ①번 for문
# ...     for j in range(1, 10):   # ②번 for문
# ...         print(i*j, end=" ") 
# ...     print('') 
# ... 
# 2 4 6 8 10 12 14 16 18 
# 3 6 9 12 15 18 21 24 27 
# 4 8 12 16 20 24 28 32 36
# 5 10 15 20 25 30 35 40 45
# 6 12 18 24 30 36 42 48 54 
# 7 14 21 28 35 42 49 56 63 
# 8 16 24 32 40 48 56 64 72 
# 9 18 27 36 45 54 63 72 81



# 리스트 내포 사용하기 #
# >>> a = [1,2,3,4]
# >>> result = []
# >>> for num in a:
# ...     result.append(num*3)
# ...
# >>> print(result)
# [3, 6, 9, 12]


# >>> a = [1,2,3,4]
# >>> result = [num * 3 for num in a]
# >>> print(result)
# [3, 6, 9, 12]


# >>> a = [1,2,3,4]
# >>> result = [num * 3 for num in a if num % 2 == 0]
# >>> print(result)
# [6, 12]

# [표현식 for 항목 in 반복가능객체 if 조건문] #

# [표현식 for 항목1 in 반복가능객체1 if 조건문1
#         for 항목2 in 반복가능객체2 if 조건문2
#         ...
#         for 항목n in 반복가능객체n if 조건문n]


# 만약 구구단의 모든 결과를 리스트에 담고 싶다면 리스트 내포를 사용하여 다음과 같이 간단하게 구현할 수도 있다. #
# >>> result = [x*y for x in range(2,10)
# ...               for y in range(1,10)]
# >>> print(result)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16,
# 20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42
# , 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72,
# 9, 18, 27, 36, 45, 54, 63, 72, 81]

