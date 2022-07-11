# 딕셔너리  # 사전

# Kye를 통해서 Value를 얻는다.

# 기본 딕셔너리의 모습
# {Key1:Value1, Key2:Value2, Key:Value3, ......}


# # 딕셔너리 쌍 추가하기
# a = {1: 'a'}
# a[2] = 'b'
# print(a)

# # # {1: 'a', 2: 'b'}

# a['name'] = 'pey'
# print(a)

# # {1: 'a', 2: 'b', 'name': 'pey'}

# a[3] = [1,2,3]
# print(a)

# # {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# # 딕셔너리 요소 삭제하기
# del a[1]
# print(a)

# # {2: 'b', 'name': 'pey', 3: [1, 2, 3]}


                         # 딕셔너리를 사용하는 방법 #
# {"김연아":"피겨스케이팅", "류현진":"야구", "박지성":"축구", "귀도":"파이썬"} #


# # 딕셔너리에서 Key 사용해 Value 얻기
# grade = {'pey': 10}
# print(grade['pey'])

# # 10


# # Key 리스트 만들기(keys), Value 리스트 만들기(values) , Key, Value 쌍 얻기(items) , Key: Value 쌍 모두 지우기(clear)
# A = {'name':'pey', 'phone':'01012345678', 'birth': '1118'}
# print(A.keys())

# # dict_keys(['name', 'phone', 'birth'])

# print(A.values())

# # dict_values(['pey', '01012345678', '1118'])

# print(A.items())

# # dict_items([('name', 'pey'), ('phone', '01012345678'), ('birth', '1118')])

# print(A.clear())

# # {}


# # Key로 Value얻기(get)
# A = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
# print(A.get('name'))

# # pey

# print(A.get('phone'))

# # 0119993323

