# 튜플 (Tuple)

# 리스트는 []으로 둘러싸지만 튜플은 ()으로 둘러싼다.
# 리스트는 그 값을 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
# 튜플은 상수라고 보면됨

# t1 = ()
# t2 = (1,)
# t3 = (1, 2, 3)
# t4 = 1, 2, 3
# t5 = ('a', 'b', ('ab', 'cd'))

# 괄호()와 (,)는 생략해도 무방하다

# 삭제가 안되며 에러가 발생한다.
# t1 = (1, 2, 3)
# del t1[0]
# print(t1)

# #Traceback (most recent call last):
# #  File "d:\Sources\Python_Study\Python_Study\Tuple_DataType\Python_Tuple.py", line 17, in <module>
# #    del t1[0]
# #TypeError: 'tuple' object doesn't support item deletion
# #PS D:\Sources\Python_Study\Python_Study\Tuple_DataType> 


# # 인덱싱하기
# t1 = (1, 2, 'a', 'b')
# print(t1[0])

# # 1

# print(t1[3])

# # b


# # 튜플 더하기
# t1 = (1, 2, 'a', 'b')
# t2 = (3, 4)
# print(t1 + t2)

# # (1, 2, 'a', 'b', 3, 4)


# # 튜플 곱하기
# t2 = (3, 4)
# print(t2 * 3)

# #(3, 4, 3, 4, 3, 4)


# # 튜플 길이 구하기
# t1 = (1, 2, 'a', 'b')
# print(len(t1))

# # 4
