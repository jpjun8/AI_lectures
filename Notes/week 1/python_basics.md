# Python 유용한 concepts

## `yield`

- 함수에서 많이 사용됨
- 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보

```python
def number_generator():
    yield 0 
    yield 1
    yield 2

g = number_generator()

a = next(g) # yield를 사용하여 함수 바깥으로 전달한 값은 next의 반환값이 됨
print(a) # 0

b = next(g)
print(b) # 1

c = next(g)
print(c) # 2
```

## `with`

- 파일 handling이나 DB 연결에 많이 사용됨

```python
with open('example.txt', 'r') as file:
    data = file.read()
    # with 문 종료와 함께 열린 파일은 자동으로 닫힘
```

## `try` and `except`

- 오류 검사

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
```

## `enumerate`

- 반복자료형 iterate 할 때 사용
- index도 같이 사용하고 싶을 때 유용

```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f'Index {index}: {fruit}')
```

## `zip`

- 2개 이상 반복자료형 묶을 때 사용
- 튜플로 return

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [28, 24, 32]

zipped_data = zip(names, ages)

for name, age in zipped_data:
    print(f'Name: {name}, Age: {age}')
```

## `filter`

- 함수를 통한 반복자료형 안 요소 필터링

```python
numbers = [1, 2, 3, 4, 5, 6]

def is_even(x):
    return x % 2 == 0

even_numbers = filter(is_even, numbers)

for num in even_numbers:
    print(num)
```

## `sort` & `sorted`

- `sort`는 리스트에만 사용 가능, original 값이 변함

```python
def sortSecond(val):
    return val[1]

list1 = [(1, 2), (3, 3), (1, 1)]
list1.sort(key=sortSecond)
print(list1) # [(1, 1), (1, 2), (3, 3)]
list1.sort(key=sortSecond, reverse=True)
print(list1) # [(3, 3), (1, 2), (1, 1)]
```

- `sorted`는 모든 반복자료형 정렬 가능, sorted list를 return

```python
L = ['aaaa', 'bbb', 'cc', 'd]
print(sorted(L)) # ['aaaa', 'bbb', 'cc', 'd']
print(sorted(L, key=len)) # ['d', 'cc', 'bbb', 'aaaa']
```

## `pass`

- 조건문이나 반복문 열었는데 아무것도 안하고 넘기고 싶을 때

```python
score = 85
if score >= 80:
    pass
else:
    print("성적이...")
```

## 리스트 Comprehension

- 파이썬에서는 대괄호 안에 조건문과 반복문을 넣어 리스트 초기화 가능
- 2차원 이상 리스트는 Comprehension 사용하여 초기화하는 것이 좋음 (O(n) 따질 때도 Comprehension이 훨씬 효과적임)
- 한줄충

```python
array = [i for i in range(20) if i % 2 == 1]

array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)

array = [[0] * 4 for _ in range(3)]
```

## `os`를 할까 말까

## `reduce`와 `map` (까먹음)

- `reduce` 진짜 편합니다 꼭 써보세요
- 특정 함수 반복자료형에 적용시킬 때
- 첫번째 요소부터 차례대로 함수에 대입시켜 실행 후 대체
- `map`도 진짜 트렌디한 코딩이 하고싶다? 무조건 써야됩니다
- `for`이나 `while`은 시간복잡도가 쓰레기라서 반복문 없이 반복자료형에 무언가 해야될 때 유용
- 보통 `map` &rarr; `filter` &rarr; `reduce` 순으로 데이터 가공
- `map`: return값이 하나가 될 수 없음, 일괄적용
- `reduce`: return값이 누적값이기 때문에 하나임, 순차적용

```python
import functools

x = [1, 3, 5, 6, 2]

print(functools.reduce(lambda a, b: a+b, x))

print(functools.reduce(lambda a, b: a if a > b else b, x))

# map
def powers(x):
    return x ** 2, x ** 3

numbers = [1, 2, 3, 4]
print(list(map(powers, numbers))) # ?
```