
# Problem


# Q1  다음 코드의 결괏값은 무엇일까?
# a = "Life is too short, you need python"

# if "wife" in a: print("wife")
# elif "python" in a and "you" not in a: print("python")
# elif "shirt" not in a: print("shirt")
# elif "need" in a: print("need")
# else: print("none")

# 출력 : shirt




# Q2  while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

# number = 1
# result = 0
# while number <= 1000:
#     if number % 3 == 0:
#         result += number
#     number += 1

# print(result)

# 출력 : 166833




# Q3  while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
# ======== #
# *        #
# **       #
# ***      #
# ****     #
# *****    #
# ======== #

# i = 0
# while True:
#     i += 1           # while문 수행 시 1씩 증가
#     if i > 5: break  # i 값이 5보다 크면 while문을 벗어난다.
#     print('*' * i)   # i 값 개수만큼 *를 출력한다.




# Q4  for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
# for number in range(1, 101):  # range함수를 사용하여 1부터 101앞에 숫자까지 반복
#     print(number)             # 숫자 출력  근데 이제 +1씩 증가를 곁들인




# Q5
# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for문을 사용하여 A 학급의 평균 점수를 구해 보자.

# student = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# total = 0

# for score in student:
#     total += score              # A학급 학생들의 점수를 모두 더한다.

# average = total / len(student)  # 평균을 구하기 위해 총 점수를 총 학생수로 나눈다.
# print(average)                  # A학급의 평균 점수가 출력된다.

# 출력 : 79.0




# Q6  리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
# ============================= #
# numbers = [1, 2, 3, 4, 5]     #
# result = []                   #
# for n in numbers:             #
#     if n % 2 == 1:            #
#        result.append(n*2)     #
# ============================= #
# 위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.

# 리스트 내포로 표현하면 다음과 같다. #
# numbers = [1, 2, 3, 4, 5]
# result = [n*2 for n in numbers if n%2==1]
# print(result)

# 출력 : [2, 6, 10]

