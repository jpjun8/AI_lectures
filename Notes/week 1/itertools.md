# itertools 모듈: iterable 생성에 용이

## `itertools.count(start=0, step=1)`

- 무한 sequence 생성 from `start` with a step of `step`

```python
from itertools import count

for i in count(1, 2):
    print(i)
```

## `itertools.cycle(iterable)`

- 무한 반복자 생성 with 주어진 반복자료형 (`iterable`)

```python
from itertools import cycle

colors = cycle(['red', 'green', 'blue'])

for _ in range(5):
    print(next(colors))
```

## `itertools.repeat(elem, n)`

- `elem`을 `n`만큼 가지고 있는 iterable 생성

```python
from itertools import repeat

for num in repeat(10, 3):
    print(num)
```

## `itertools.islice(iterable, start, stop, step)`

- 주어진 `iterable` 슬라이싱

```python
from itertools import islice

data = range(10)
sliced_data = islice(data, 2, 7, 2)

for item in sliced_data:
    print(item)
```

## `itertools.chain(iterable1, iterable2, ...)`

- 여러개 iterable 하나로 결합 (자료형 달라도 괜찮)

```python
from itertools import chain

list1 = [1, 2, 3]
tuple1 = ('a', 'b', 'c')

combined = chain(list1, tuple1)

for item in combined:
    print(item)
```

## `itertools.combinations(iterable, r)`

- 코테에 많이 씀, 한국어로 `조합`
- 주어진 iterable 안에서 만들 수 있는 모든 `r` 길이의 조합 생성

```python
from itertools import combinations

data = [1, 2, 3, 4]
combo = combinations(data, 2)

for c in combo:
    print(c)
```

## `itertools.permutations(iterable, r)`

- 코테에 많이 씀, 한국어로 `순열`
- 주어진 iterable 안에서 만들 수 있는 모든 `r` 길이의 순열 생성
- 순서가 있을 때, 중복이 없을 때 사용하는 편

```python
from itertools import permutations

data = [1, 2, 3]
perm = permutations(data, 2)

for p in perm:
    print(p)
```

### `combinations`와 `permutations` 팁

- `print(list(map("".join, w)))` 형식으로 `map` 사용하면 보기 편하게 출력 가능 (단, value들이 string일 때만)
- `itertools` 모듈로 만든 iterable들은 그냥 `print`로 출력 X
- `list`로 바꾸거나 반복문, `map` 같은 거 사용해서 출력

## `itertools.product(*iterables, repeat=1)`

- 입력받은 iterables들의 Cartesian Product 출력
- 매트릭스라고 해야되나 이걸
- 한국어로 모르겠음

```python
from itertools import product

A = [1, 2]
B = ['a', 'b']

cartesian_product = product(A, B)

for item in cartesian_product:
    print(item)
```

## `itertools.compress(data, selectors)`

- `selectors` 적용시켜서 `data` 요소 필터링

```python
from itertools import compress

data = [1, 2, 3, 4, 5]
selectors = [True, False, True, False, True]

filtered_data = compress(data, selectors)

for item in filtered_data:
    print(item)
```

## `itertools.dropwhile(predicate, iterable)`

- `predicate` 함수에 적용되는 요소 `iterable`에서 drop

```python
from itertools import dropwhile

data = [1, 3, 5, 2, 4, 6]

filtered_data = dropwhile(lambda x: x < 5, data)

for item in filtered_data:
    print(item)
```

## `itertools.takewhile(predicate, iterable)`

- `dropwhile` 반대

```python
from itertools import takewhile

data = [1, 3, 5, 2, 4, 6]

filtered_data = takewhile(lambda x: x < 5, data)

for item in filtered_data:
    print(item)
```

## `itertools.groupby(iterable, key=None)`

- `key` 결과에 따른 iterable 그룹화
- (`key`, `group`) 페어로 return

```python
from itertools import groupby

data = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']

def key_func(item):
    return len(item)

grouped_data = groupby(data, key=key_func)

for key, group in grouped_data:
    print(f'Words with {key} letters:', list(group))
```

## `itertools.tee(iterable, n=2)`

- `n` 갯수만큼 `iterable` 생성

```python
from itertools import tee

data = [1, 2, 3, 4, 5]

iterators = tee(data, 3)

for i, iterator in enumerate(iterators, 1):
    print(f'Iterator {i}:', list(iterator))
```

## `itertools.starmap(function, iterable)`

- `iterable`의 각 요소 `function`으로 넘겨 결과값 iterable로 return

```python
from itertools import starmap

data = [(2, 3), (4, 5), (6, 7)]

result = starmap(lambda x, y: x * y, data)

for item in result:
    print(item)
```

## `itertools.zip_longest(iterable1, iterable2, fillvalue=None)`

- 2개 이상 iterable zip
- 없는 요소는 `fillvalue` 값으로 채움

```python
from itertools import zip_longest

a = [1, 2, 3]
b = ['a', 'b']

zipped = zip_longest(a, b, fillvalue=None)

for item in zipped:
    print(item)
```
