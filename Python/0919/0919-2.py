# for 문 이용
result = []
for i in range(10):
    result.append(i ** 2)
print(result)

# map 함수 이용
result = map(lambda x : x ** 2, list(range(10)))
print(list(result))

# list comprehension 이용
# for 앞에 식이 list를 만들 연산식이고 뒤에는 필러링 조건이 온다.
result = [ i ** 2 for i in range(10)]
print(result)

# comprehension 뒤에 if문을 추가하여 필터링을 할 수 있다.
singers = ["BTS", "아이유", "블랙핑크", "트와이스", "마마무"]
result = [ i for i in singers if len(i) > 3]
print(result)

# 이중 for문을 이용한 list comprehension
li1 = [1, 2, 3, 4, 5]
li2 = [6, 7, 8, 9, 10]
result = [ i + j for i in li1 for j in li2]
print(result)

# 2차원 리스트를 1차원 리스트로 변환
li = [[1, 2], [3, 4], [5, 6]]
result = [j for i in li for j in i]
print(result)