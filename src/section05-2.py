# section05-2
# 파이썬 흐름 제어(반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

v1 = 1
while v1 < 11:
    print('v1 is :', v1)
    v1 += 1

for v2 in range(10):
    print('v2 is :', v2)

for v3 in range(1,11):
    print('v3 is :', v3)

# 1 ~ 100 합
sum1 = 0
for i in range(1, 101):
    sum1 += i
print('1 ~ 100', sum1)
print('1 ~ 100', sum(range(1, 101)))
print('1 ~ 100', sum(range(1, 101, 2)))

print()

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable : range, reversed, enumrate, filter, map, zip

names = ["kim", "park", "cho", "choi", "yoo"]
for i in names:
    print("your are :", i)

word = 'dreams'
for s in word:
    print('word :', s)

my_info = {
    "name" : "kim",
    "age" : 33,
    "city" : "seoul"
}
# 기본값은 키 출력
for i in my_info:
    print("my_info", i)

# 값
for i in my_info.values():
    print("my_info", i)

# 키
for i in my_info.keys():
    print("my_info", i)

# 키 and 값
for k,v in my_info.items():
    print("my_info", k, v)

name = "JWooni"
for i in name:
    if i.islower():
        print(i.upper())
    else:
        print(i.lower())


# break
numbers = [13, 4, 3, 5, 7, 33, 89, 15, 39, 66, 2, 10]

for i in numbers:
    if i == 33:
        print('found : 33!')
        break
    else:
        print('not found : 33!')

# for - else 구문(반복문이 정상적으로 수행된 경우 else 블럭 수행)
for i in numbers:
    if i == 33:
        print('found : 33!')
        break
    else:
        print('not found : 33!')
else:
    print('not found 33.......')

print()

# continue
lt = ["1", 2, 5, True, 4.5, complex(4)]
for i in lt:
    if type(i) is float:
        print("찾았다!")
        continue
    print('타입 :', type(i))


name = "Niceman"
print(reversed(name))
    