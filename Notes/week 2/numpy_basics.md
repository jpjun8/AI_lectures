# NumPy Basics

## Array (배열)

- NumPy는 Python 모듈이지만 리스트가 아닌 array, 배열이라고 부름
- 이유는 그냥 배열에 하나의 type밖에 저장을 못해서...
- 어케만듬?

```python
import numpy as np

# np.array()
a = np.array([1, 2, 3])
print(a) # [1 2 3] -- 리스트랑 다르게 콤마 대신 공백으로 구분함

# np.zeros()
b = np.zeros(2)
print(b)

# np.ones()
c = np.ones(2)
print(c)

# np.empty() -- np.zeros() 대신 쓰는 이유 : 속도가 빠름
d = np.empty(2)
print(d)

# np.arange()
e = np.arange(4)
print(e)

# np.linspace(start, end, n)
f = np.linspace(0, 10, num=5)
print(f)

# 많이 쓰는 예제: 사인 값 그래프 그릴 때 데이터 생성
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
print(y)

# dtype 설정
g = np.ones(2, dtype=np.int64)
print(g)
```

- 인덱싱으로도 만들어보자

```python
print(np.r_[1:4, 0, 4])
print(np.c_[np.array([1, 2, 3]), np.array([4, 5, 6])])
```

## Elements

- 배열 안에 있는 애들 가지고 할 수 있는거

```python
# np.sort()
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(np.sort(arr)) # sorted랑 비슷: 원래 배열 안바뀜
# argsort, lexsort, searchsorted, partition 등등

# np.concatenate(): 이어붙이기
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(np.concatenate((a, b)))

# 심화
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]]) # 대괄호 2개임
print(np.concatenate((x, y), axis=0)) 
# axis 0: 1차원(row), axis 1: 2차원(col), ...
```

## 배열 차원, 크기, 몇행몇열 등

- 나중에 `reshape`할 때 용이함

```python
arr = np.array([[[0, 1, 2, 3],
                [4, 5, 6, 7]],
                
                [[0, 1, 2, 3],
                [4, 5, 6, 7]],

                [[0, 1, 2, 3],
                [4, 5, 6, 7]]])

print(arr.ndim, arr.size, arr.shape)
# 보통 shape을 많이 씀
```

## 그럼 `reshape`가 뭐냐

- 저딴식으로 만든 배열 내맘대로 조정하기

```python
a = np.arange(6) # [0, 1, 2, 3, 4, 5]
b = a.reshape(3, 2) # 3행 2열로 바꿔라
print(b)

# np.reshape() 함수로도 사용가능
print(np.reshape(a, newshape=(1, 6), order='C')) # 기존 array는 안바뀜

# 치트: -1
ar = np.array([[3, 7, 3, 4, 1, 4], [2, 2, 7, 2, 4, 9]])
print(ar.reshape(3, -1))

# resize: 기존 배열이 변경됨
ar.resize((3, 4))
print(ar)
```

## 1차원 &rarr; 2차원 배열

- `np.newaxis`: axis 배열에 추가
- `np.expand_dims`: 차원 추가

```python
a = np.array([1, 2, 3, 4, 5, 6])
row_vector = a[np.newaxis, :]
print(row_vector, row_vector.shape)

col_vector = a[:, np.newaxis]
print(col_vector, col_vector.shape)

b = np.expand_dims(a, axis=1) # axis=1 은 뭐다?
print(b, b.shape)

c = np.expand_dims(a, axis=0) # axis=0 은 뭐다?
print(c, c.shape)
```

## 인덱싱

- 제일 많이 쓰고 제일 중요하다
- 제일 귀찮지만 에러가 제일 많이 나는 부분
- 기본 문법은 기본 파이썬 인덱싱, 슬라이싱이랑 똑같음

```python
# 그냥 파이썬이랑 똑같음 여기는
data = np.array([1, 2, 3])
print(data[1], data[0:2], data[1:], data[-2:])

# 2차원부터가 진짜
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a < 5]) # a의 모든 값들 중에 5보다 작은거만 필터링

cond = (a >= 5)
print(a[cond]) # 조건변수 만들어서 필터링도 가능
print(a[a % 2 == 0])
print(a[(a > 2) & (a < 11>)]) # and: &, or: |
print((a > 5) | (a == 5)) # 각 요소가 조건에 맞으면 True, 아니면 False

# 조건에 맞는 인덱스 뽑기
# 첫번째 배열: 행 index, 두번째 배열: 열 index
b = np.nonzero(a < 5)
print(b)

# `zip`과 연계: 몇행 몇열에 있는지 확인용
coords = list(zip(b[0], b[1]))
for coord in coords:
    print(coord)

# 조건에 맞는 요소 출력
print(a[b]) # print(a[a < 5])랑 똑같음
```

## 슬라이싱 + 잡지식

- 인덱싱보다 많이 쓸지도?
- 간단.

```python
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr1 = a[3:8]

# 배열 결합
a1 = np.array([[1, 1], [2, 2]])
a2 = np.array([[3, 3], [4, 4]])
print(np.vstack((a1, a2))) # 수직
print(np.hstack((a1, a2))) # 수평

# 배열 결합인데 이제 column_stack을 사용한..
a = np.array([4, 3])
b = np.array([2, 8])
print(np.column_stack((a, b)))
# == np.hstack((a[:, newaxis], b[:, newaxis]))
# == np.vstack((a, b)).T

# 배열 분할
x = np.arange(1, 25).reshape(2, 12)
print(np.hsplit(x, 3)) # 세로로 3분할
print(np.hsplit(x, (3, 4))) # 3열과 4열에서 분할
```

- 지금까지 나온 거의 모든 인덱싱과 슬라이싱 방법은 `view` (얕은 복사) 형식으로 진행
- 베이스가 되는 배열이 바뀔 수 있음

```python
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = a[0, :] 
b[0] = 99 
print(b)
print(a) 

# 그럼 어케함? 복사하면됨 (깊은 복사)
ex = a.copy()[0, :]
ex[0] = 1 
print(ex) 
print(a) 
```

## Array Operations

- 배열끼리 사칙연산이 된다
- 다른 여러가지 계산(합, 제곱, ...)도 된다
- 당연히 `np.max()`, `np.min()`도 있다

```python
data = np.array([1, 2])
ones = np.ones(2, dtype=int)

# 같은 자리에 있는 애들끼리 연산
print(data + ones)
print(data - ones)
print(data * data)
print(data / data)

# 합: np.sum()
a = np.array([1, 2, 3, 4])
print(a.sum())

# 누적합: np.cumsum()
x = np.arange(12).reshape(3, 4)
print(x.cumsum(axis=1))

# 'e'의 제곱, 그냥 제곱, 루트, 더하기 함수
A = np.arange(3)
print(np.exp(A))
print(np.power(A, 3)) # 그냥 ** 써도됨
print(np.sqrt(A))
B = np.array([2., -1., 4.])
print(np.add(A, B))

# 2차원 배열의 합
b = np.array([[1, 1], [2, 2]])
print(b.sum(axis=0))
print(b.sum(axis=1))
```

## Broadcasting

- 배열에 전체적으로 몇씩 더하기, 빼기, 곱하기, 나누기
- 심화하면 어려움

```python
data = np.array([1., 2.])
print(data * 1.6)
```

## 문제

```python
data = np.array([[1, 2], [3, 4], [5, 6]])
print(data[0, 1])
print(data[1:3])
print(data[1:3, :])
print(data[0:2, 0])

data = np.array([[1, 2], [5, 3], [4, 6]])
print(data.max(axis=0))
print(data.max(axis=1))
```

## 다른 shape 배열끼리 연산

- 둘 중 하나는 1행이던지 1열이어야 가능

```python
data = np.array([[1, 2], [3, 4], [5, 6]])
ones = np.array([[1, 1]])
print(data + ones)
```

## 잡 functions

```python
# np.unique(): 중복값 빼기
# `return_index`: True이면 unique값 index들 array로 return
a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
print(np.unique(a), np.unique(a, return_index=True))
```

## Transposing & Reshaping

- 제일 많이 하는거
- 가로세로 바꾸기, shape 맞추기
- 쉬운데 어려움

```python
data = np.array([[1, 2], [3, 4], [5, 6]])
print(data.reshape(2, 3))
print(data.reshape(3, 2))

# transpose
arr = np.arange(6).reshape((2, 3))
print(arr.transpose(), '\n', arr.T)
```

## 뒤집기

- 1차원보다 2차원에서 할 때 조금 헷갈림

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(np.flip(arr))

# 2차원
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(np.flip(arr_2d))
print(np.flip(arr_2d, axis=0))
print(np.flip(arr_2d, axis=1))
print(np.flip(arr_2d[1]))
print(np.flip(arr_2d[:, 1]))
```

## 다차원 &rarr; 1차원

- 3차원 이상으로 가면 다루기 어려워서 많이 씀
- `flatten()`: 1차원의 복사본 생성 (깊은 복사, `copy`)
- `ravel()`: 그냥 1차원으로 바꾸기 (얕은 복사, `view`)

```python
x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(x.flatten())
```

## NumPy 사용할 때 가장 오류 많이 나는 곳

- 배열 `reshape`과 연산
- 배열 연산하려면 `shape`을 맞춰줘야한다..
- 그럴려면 `reshape`을 잘 해야한다..
- 그럴려면 1차원 &rarr; 다차원 or 다차원 &rarr; 1차원 왔다갔다 하는 걸 잘해야한다..
- `pandas`랑 `matplotlib`이랑 같이 쓸 때

## 행렬 (matrix) 연산

- NumPy에서는 주로 2차원 배열을 많이 쓰기 때문에 2차원 배열끼리의 연산이 많다
- 2차원 배열은 행렬로 취급해서 연산
- **스칼라 곱과 행렬 곱**

```python
A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])

# 스칼라 곱
print(A * B)

# 행렬 곱 1
print(A @ B)

# 행렬 곱 2
print(A.dot(B))
```

## 기타 잡설

- NumPy에서는 2차원 배열이 기본, 3차원 배열도 익숙해져야 된다 (이미지 프로세싱에 많이 사용함)
- [1 2 3 4 5].T 는 Transpose가 되지 않으니 `np.newaxis` 추가해서 `reshape`이던 `T`이던 활용해야된다
- 항상 내가 사용하고 있는 변수가 복사본인지, 복사본이면 `View`인지 `Copy`인지 알고 사용할 것
- 오류 메시지가 굉장히 친절하니 잘 읽어보면 거의 다 해결 가능
- 통계학, 수학 공식 많이 알면 좋음: Moore's Law, Laplace, Gaussian, Markov Chain, etc.
