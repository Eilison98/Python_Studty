
# if문 #

# if문의 기본 구조 #
# if 조건문:
#     수행할 문장1
#     수행할 문장2
#     ...
# else:
#     수행할 문장A
#     수행할 문장B
#     ...


# 조건문이란 무엇인가? #
# >>> money = True
# >>> if money:



# 비교연산자설명 #
# 비교연산자(<, >, ==, !=, >=, <=) #
# x < y	    x가 y보다 작다
# x > y	    x가 y보다 크다
# x == y	x와 y가 같다
# x != y	x와 y가 같지 않다
# x >= y	x가 y보다 크거나 같다
# x <= y	x가 y보다 작거나 같다



# "만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라." #
# money = 2000
# if money >= 3000:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# 출력 : 걸어라가


# and, or, not #
# 연산자	설명 #
# x or y	x와 y 둘중에 하나만 참이어도 참이다
# x and y	x와 y 모두 참이어야 참이다
# not x	x가 거짓이면 참이다



# "돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라." #
# money = 2000
# card = True
# if money >= 3000 or card:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# 출력 : 택시를 타고 가라



# 다양한 조건을 판단하는 elif #
# "주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어 가라." #
# pocket = ['paper', 'handphone']
# card = True
# if 'money' in pocket:
#     print('택시를 타고 가라')
# elif card:
#         print('택시를 타고 가라')
#     else:
#         print('걸어가라')

# # 출력 : 택시를 타고 가라



# 조건부 표현식 #
# if score >= 60:
#     message = "success"
# else:
#     message = "failure"


