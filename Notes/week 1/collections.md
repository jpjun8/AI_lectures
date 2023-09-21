# `collections` 모듈

- 특수자료형, custom 자료형 만들어서 문제풀이에 많이 쓰임
- 다차원 리스트나 배열 다룰 때 사용하기 쉽게 가공용으로도 쓰임
  
## `Counter`

- 딕셔너리 subclass
- 요소 카운팅

```python
from collections import Counter

word_list = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
word_counts = Counter(word_list)

print(word_counts)
```

- `most_common(n)`: 가장 빈도 수가 많은 값 `n`개 찾기

```python
print(word_counts.most_common(2))
```

## `defaultdict`

- 딕셔너리 subclass
- key 없을 때 default 값 return (일반 딕셔너리는 에러)

```python
from collections import defaultdict

fruit_counts = defaultdict(int)
fruit_list = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']

for fruit in fruit_list:
    fruit_counts[fruit] += 1

print(fruit_counts)
```

## `deque` (double-ended queue)

- 리스트랑 비슷한 양쪽 큐

```python
from collections import deque

queue = deque(['apple', 'banana', 'cherry'])
queue.append('date') # 오른쪽에 추가
queue.appendleft('apricot') # 왼쪽에 추가

print(queue)
```

- `rotate()`, `extendleft()`, `extend()` 등등

```python
d = deque([1, 2, 3, 4, 5])
d.rotate(2) # 요소들 오른쪽으로 2칸만큼 회전
print(d)

d.extend([6, 7, 8]) # d 오른쪽에 6, 7, 8 순서대로 추가
print(d)

d.extendleft([6, 7, 8]) # d 왼쪽에 6, 7, 8 순서대로 추가
print(d)
```

## `namedtuple`

- 튜플 subclass
- 이름으로 접근 가능한 tuple 생성

```python
from collections import namedtuple

Point = namedtuple('Amber', ['x', 'y'])
p = Point(1, 2)

print(p.x) # 이름 접근
print(p[1]) # 인덱스 접근
print(p, type(p)) # 자료형 이름 지정 가능
```

- `_fields`, `_replace()`

```python
print(p._fields) # 필드 이름 출력
p = p._replace(x=10) # p의 x값 변경 X, 새로운 Point 생성
print(p)
```

## `OrderedDict`

- 딕셔너리 subclass
- 요소 추가된 순서 기억함

```python
from collections import OrderedDict

fruit_dict = OrderedDict()
fruit_dict['apple'] = 3
fruit_dict['banana'] = 2
fruit_dict['cherry'] = 1

print(fruit_dict)
```

## `ChainMap`

- 여러개 딕셔너리 결합
- 첫번째 딕셔너리 값이 우선

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
combined_dict = ChainMap(dict1, dict2)

print(combined_dict['a'])
print(combined_dict['b']) # from dict1
print(combined_dict['c']) # from dict2
```
