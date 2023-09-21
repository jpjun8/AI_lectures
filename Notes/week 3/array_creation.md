# Array Creation Routine (advanced)

- `empty`, `zeros` 이런거 말고 **심화** 기능

## `empty_like`, `ones_like`, `zeros_like`

- 뒤에 `like` 붙은 애들은 참조할 배열 (또는 배열 같은 거, *리스트*, *튜플*) 하나를 인수로 받아서 그 배열의 `shape`으로 생성함

```python
a = np.array([1., 2., 3.], [4., 5., 6.])
print(np.empty_like(a))

a = ([1, 2, 3], [4, 5, 6])
print(np.empty_like(a))
```

## `eye`, `identity`

- 대각선에만 뭐 채우고 싶을 때
- 지금은 어디다 쓰는지 모르지만 AI 들어가면 알게됨
- 행렬 곱 할 때 유용
- `eye`는 행과 열 갯수 조절 가능 <> `identity`는 불가

```python
print(np.eye(2, dtype=int))
print(np.eye(3, k=1))

print(np.identity(3))
```

## `diag`

- 대각선만 빼오고 싶을때
  
```python
x = np.arange(9).reshape((3, 3))
print(np.diag(x))
print(np.diag(x, k=1))
print(np.diag(np.diag(x)))
```

## `tri`

- 원하는 대각선과 그 밑에는 다 1로 채우고 나머지는 0

```python
print(np.tri(N=3, M=5, k=2, dtype=int))
print(np.tri(N=3, M=5, k=-1, dtype=int))
```
