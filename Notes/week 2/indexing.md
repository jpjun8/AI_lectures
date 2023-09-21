# 심화 Indexing

## 인덱스 배열로 인덱싱

- 알면 알수록 신기한 NumPy 배열 인덱싱
- [  ] 안에 배열을 넣어서 인덱싱을 한다...

```python
a = np.arange(12) ** 2
i = np.array([1, 1, 3, 8, 5]) # 인덱스 배열
print(a[i]) # ?

j = np.array([[3, 4], [9, 7]]) # 2차원 인덱스 배열
print(a[j]) # ?
```

- 어려운거

```python
palette = np.array([[0, 0, 0],
                    [255, 0, 0],
                    [0, 255, 0],
                    [0, 0, 255],
                    [255, 255, 255]])
image = np.array([[0, 1, 2, 0],
                  [0, 3, 4, 0]])
print(palette[image]) # ?
```

- 더 어려운거

```python
a = np.arange(12).reshape(3, 4)
i = np.array([[0, 1], [1, 2]])
j = np.array([[2, 1], [3, 3]])

print(a[i, j]) # ?
print(a[:, j]) # ???
```

## 골라서 할당

- 인덱스로 골라서 원하는 인덱스값만 한번에 바꿀 수 있다

```python
a = np.arange(5)
a[[1, 3, 4]] = 0
print(a)

a[[0, 0, 2]] = [1, 2, 3] # 중복되면 마지막값으로 할당
print(a)
```

## `boolean`으로 인덱싱

- 인덱싱 GOAT. 개편함. 
- 조건문 필요가 없어짐
  
```python
a = np.arange(12).reshape(3, 4)
b = a > 4
print(b)

print(a[b])

# 조건에 맞는 값만 변경할때도
a[b] = 0
print(a)
```
