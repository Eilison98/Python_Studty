# 집합 자료형


# # 교집합, 합집합, 차집합 구하기
# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([4, 5, 6, 7, 8, 9])

# # 교집합
# print(s1 & s2)
# print(s1.intersection(s2))

# # {4, 5, 6}

# # 합집합
# print(s1 | s2)
# print(s1.union(s2))

# # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# # 차집합
# print(s1 - s2)
# print(s1.difference(s2))

# # {1, 2, 3}

# print(s2 - s1)
# print(s2.difference(s1))

# # {8, 9, 7}



# # 집합 자료형 관련 함수들
# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([4, 5, 6, 7, 8, 9])

# # 값 1개 추가하기(add)
# s1 = set([1, 2, 3])
# s1.add(4)
# print(s1)

# # {1, 2, 3, 4}

# # 값 여러 개 추가하기 (update)
# s1 = set([1, 2, 3])
# s1.update([4, 5, 6])
# print(s1)

# # {1, 2, 3, 4, 5, 6}

# # 특정 값 제거하기 (remove)
# s1 = set([1, 2, 3])
# s1.remove(2)
# print(s1)

# # {1, 3}

