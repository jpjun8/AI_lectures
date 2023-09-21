# 잡기술 모음집

## "Automatic" Reshaping

- `-1` 이거 한번 쓰면 다른거 못씀

```python
a = np.arange(30)
b = a.reshape((2, -1, 3))
print(b.shape)
print(b)
```

## Vector 스택

- `vstack`, `hstack`, `dstack`, `column_stack` 등등

```python
x = np.arange(0, 10, 2)
y = np.arange(5)
m = np.vstack([x, y])
print(m)
xy = np.hstack([x, y])
print(xy)
```

## Vectorize

- 인수로 받은 함수 적용 후 하나의 배열로 return

```python
def myfunc(a, b):
    if a > b:
        return a - b
    else:
        return a + b

vfunc = np.vectorize(myfunc)
print(vfunc([1, 2, 3, 4], 2))
```

## Diff

- 배열 안 요소끼리 얼마나 차이나는 지 알고 싶을 때

```python
x = np.array([1, 2, 4, 7, 0])

print(np.diff(x))
print(np.diff(x, n=2))

y = np.array([[1, 3, 6, 10], [0, 5, 6, 8]])

print(np.diff(y))
print(np.diff(y, axis=0))
```

## `lcm` & `gcd`

- 최소공배수 & 최대공약수

```python
print(np.lcm(12, 20))
print(np.lcm.reduce([3, 12, 20]))
print(np.lcm(np.arange(6), 20))

print(np.gcd(12, 20))
print(np.gcd.reduce([15, 25, 35]))
print(np.gcd(np.arange(6), 20))
```

## `reciprocal`

- 분수화

```python
print(np.reciprocal(2.)) # 1/2 = 0.5
```

## `set_printoptions`

- 출력 형태 변경

```python
np.set_printoptions(precision=4)
print(np.array([1.123456789]))

np.set_printoptions(threshold=5)
print(np.arange(10))

eps = np.finfo(float).eps
x = np.arange(4.)
print(x**2 - (x + eps) ** 2)
np.set_printoptions(suppress=True)
print(x**2 - (x + eps) ** 2)
```

## `where`

- 조건부 인덱싱 + 조건에 따라 True, False일 때 각각 다르게 execution
- 직관적, 편리함, 자주 사용

```python
[xv if c else yv for c, xv, yv in zip(condition, x, y)]

a = np.arange(10)
print(np.where(a < 5, a, 10*a))

print(np.where([[True, False], [True, True]],
                [[1, 2], [3, 4]],
                [[9, 8], [7, 6]]))

# broadcasting with `where`
a = np.array([[0, 1, 2],
              [0, 2, 4],
              [0, 3, 6]])
print(np.where(a < 4, a, -1))
```

## `intersect1d` & `setdiff1d`

- 겹치는 요소와 겹치지 않는 요소 구별

```python
print(np.intersect1d([1, 3, 4, 3], [3, 1, 2, 1]))

# 3개 이상 비교하려면 `functools`에서 `reduce` 사용
from functools import reduce
print(reduce(np.intersect1d, ([1, 3, 4, 3], [3, 1, 2, 1], [6, 3, 4, 2])))

# 겹치는 요소의 인덱스 출력
x = np.array([1, 1, 2, 3, 4])
y = np.array([2, 1, 4, 6])
xy, x_ind, y_ind = np.intersect1d(x, y, return_indices=True)
print(x_ind, y_ind)
print(xy, x[x_ind], y[y_ind])

# 첫번째 배열에만 존재하는 요소 return
a = np.array([1, 2, 3, 2, 4, 1])
b = np.array([3, 4, 5, 6])
print(np.setdiff1d(a, b))
```
