

# 사용자 입력과 출력
 
# input의 사용 #
# >>> a = input()
# Life is too short, you need python
# >>> a
# 'Life is too short, you need python'
# >>>

# < ex >
# >>> number = input("숫자를 입력하세요: ")
# 숫자를 입력하세요:


# >>> number = input("숫자를 입력하세요: ")
# 숫자를 입력하세요: 3
# >>> print(number)
# 3
# >>>


# >>> type(number)
# <class 'str'>
# >>>




# print 자세히 알기 # 
# >>> a = 123
# >>> print(a)
# 123
# >>> a = "Python"
# >>> print(a)
# Python
# >>> a = [1, 2, 3]
# >>> print(a)
# [1, 2, 3]



# 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다 #
# >>> print("life" "is" "too short") # ①
# lifeistoo short
# >>> print("life"+"is"+"too short") # ②
# lifeistoo short



# 문자열 띄어쓰기는 콤마로 한다 #
# >>> print("life", "is", "too short")
# life is too short



# 한 줄에 결괏값 출력하기 #
# >>> for i in range(10):
# ...     print(i, end=' ')
# ...
# 0 1 2 3 4 5 6 7 8 9


