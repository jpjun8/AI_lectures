# Array Manipulation Routine (advanced)

## `transpose`

- `T` 랑 하는 일은 똑같은데 **깊은 복사**
- 보통 `T`를 쓰지만 값을 변경해야되거나 객체가 따로 필요할 땐 `transpose` 사용
- `T`랑 똑같이 1-D 배열은 해도 변경점 없음

```python
a = np.array([[1, 2], [3, 4]])
print(np.transpose(a))

a = np.ones((1, 2, 3))
print(np.transpose(a, (1, 0, 2)))
```

## `squeeze`

- 길이 하나짜리 dimension은 flatten 해버리기

```python
x = np.array([[0], [1], [2]])

print(np.squeeze(x))
print(np.squeeze(x, axis=0))
# print(np.squeeze(x, axis=1))
print(np.squeeze(x, axis=2))
```

## `array_split`

- `split`이랑 똑같으나 꼭 나누어 떨어지지 않아도 분할 가능

```python
x = np.arange(8.0)
print(np.array_split(x, 3))

x = np.arange(9)
print(np.array_split(x, 4))
```

## `tile`

- 배열 값 원하는 횟수와 `shape`에 맞춰서 반복

```python
a = np.array([0, 1, 2])

print(np.tile(a, 2))
print(np.tile(a, (2, 2)))
print(np.tile(a, (2, 1, 2)))

b = np.array([[1, 2], [3, 4]])

print(np.tile(b, 2))
print(np.tile(b, (2, 1)))
```

## `flip`

- 뒤집기 (원하는대로)

```python
A = np.arange(8).reshape((2, 2, 2))

print(np.flip(A, 0))
print(np.flip(A, 1))
print(np.flip(A))
print(np.flip(A, (0, 2)))
```

## `roll`

- 굴리기 (원하는대로)
- 이미지 processing 할 때 자주 사용
- shifting? 이라고 생각하면 될 듯

```python
x = np.arange(10)

print(np.roll(x, 2)) # 오른 2칸
print(np.roll(x, -2)) # 왼 2칸

x2 = np.reshape(x, (2, 5))

print(np.roll(x2, 1))
print(np.roll(x2, -1))

print(np.roll(x2, 1, axis=0))
print(np.roll(x2, -1, axis=0))

print(np.roll(x2, 1, axis=1))
print(np.roll(x2, -1, axis=1))

print(np.roll(x2, (1, 1), axis=(1, 0)))
print(np.roll(x2, (2, 1), axis=(1, 0)))
```
