# 자료형의 값을 저장하는 공간, 변수

# 변수란?
# 파이썬에서 사용하는 변수는 객체를 가리키는 것이라고도 말할 수 있다. 객체란 우리가 지금껏 보아 온 자료형과 같은 것을 의미하는 말이다.
# >>> a = [1, 2, 3]

# a 변수가 가리키는 메모리의 주소는 다음과 같이 확인할 수 있다.
# >>> a = [1, 2, 3]
# >>> id(a)
# 4303029896


# 리스트를 복사하고자 할 때
# >>> a = [1,2,3]
# >>> b = a

# >>> id(a)
# 4303029896
# >>> id(b)
# 4303029896

# >>> a is b  # a와 b가 가리키는 객체는 동일한가?
# True


# 1. [:] 이용
# >>> a = [1, 2, 3]
# >>> b = a[:]
# >>> a[1] = 4
# >>> a
# [1, 4, 3]
# >>> b
# [1, 2, 3]


# 2. copy 모듈 이용
# >>> from copy import copy
# >>> a = [1, 2, 3]
# >>> b = copy(a)

# >>> b is a
# False


# 변수를 만드는 여러 가지 방법
# >>> a, b = ('python', 'life')
# >>> (a, b) = 'python', 'life'
# >>> [a,b] = ['python', 'life']
# >>> a = b = 'python'

# 파이썬에서는 위 방법을 사용하여 두 변수의 값을 아주 간단히 바꿀 수 있다.
# >>> a = 3
# >>> b = 5
# >>> a, b = b, a
# >>> a
# 5
# >>> b
# 3
