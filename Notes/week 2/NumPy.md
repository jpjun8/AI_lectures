# `NumPy` 모듈

## 설치

- Python & pip 버전 확인: `python --version`, `pip --version`
- 설치 안되어있으면 설치
- 사용할 Python 버전 맞춰서 `NumPy` 모듈 설치
- `pip install numpy`, 안되면 수동 설치
- `pip list`: 설치된 모듈 확인, `numpy` 보이면 완료

## `NumPy`

- `import numpy as np`: 보통 `np`로 줄여서 사용함
- `NumPy`에서는 `NumPy`만의 반복자료형인 `Array`를 사용 (배열)
- 기본적으로 리스트와 비슷하나 만들 수 있는 방법이 다양하고 행과 열에 초점이 많이 맞추어져 있음
- C 배열처럼 한가지 자료형만 저장 가능 (list와 다른점)
- list보다 훨씬 빠름, vector 연산 가능, 메모리 적게 먹음
- 인덱싱과 슬라이싱 편함
- 내장 함수 매우 많고 지금도 개발되고 있음 (리소스 찾아보면 다 나오는데 영문)
- 데이터분석, 개발 실무 알고리즘, AI 신경망 개발까지 사용됨
- `SciPy`, `pandas`, `Matplotlib`, `scikit-learn`이랑 호환
- list보다 복잡하고 사용하기 어렵지만 실행 속도, 유연성, 범용성 따져보면 데이터나 AI쪽 가려면 입문/필수 (그렇게 어렵지도 않음)

## `Arrays`

- list와 다르게 콤마로 요소 구분 안함
- `[1 2 3 4 5]` 요런 식

```python
# list 활용하여 생성
arr1 = np.array([1, 2, 3])

# 0만 있는 array 생성
arr2 = np.zeros((2, 3)) # 2행 3열

# 1만 있는 array 생성
arr3 = np.ones((3, 2)) # 3행 2열

# arange 활용하여 생성
arr4 = np.arange(0, 10, 2) # [0 2 4 6 8]
```

- 만들어진 `array`는 여러가지 속성도 가지는데 매우 유용
- `shape`, `dtype`, `size`는 필수

```python
arr = np.array([[1, 2, 3], [4, 5, 6]]) # 2차원 배열
print("Shape:", arr.shape)
print("Data Type:", arr.dtype)
print("Size:", arr.size)

print("Dimension:", arr.ndim)
print("Item size:", arr.itemsize)
print("Bytes:", arr.nbytes)
```

## `Array Operations`

- 배열끼리 사칙연산가능!

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

add = arr1 + arr2
sub = arr1 - arr2
mul = arr1 * arr2
divi = arr1 / arr2
```

- 사인 코사인, `e`의 몇제곱 이런것도 가능

```python
arr = np.array([0, np.pi/2, np.pi])
sine_values = np.sin(arr)
```

- 당연히 합, 평균, 최댓값/최솟값 가능

```python
arr = np.array([1, 2, 3, 4, 5])

sum = np.sum(arr)
mean = np.mean(arr)
max = np.max(arr)
min = np.min(arr)
```

- 차원조절 가능 (AI에서 제일 많이씀, 특히 이미지 관련)

```python
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2, 3)
```

- 인덱싱 슬라이싱

```python
arr = np.array([1, 2, 3, 4, 5])
elem = arr[2]
sliced = arr[1:4]
```

- `Broadcasting`: 다른 차원의 배열끼리 연산 가능

```python
arr1 = np.array([1, 2, 3])
arr2 = 2
res = arr1 * arr2 # 배열과 스칼라간 곱연산
```

- `Vectorized` 비교 연산

```python
arr = np.array([1, 2, 3, 4, 5])
gt3 = arr > 3 # return ?
```

## 3차원 이상 배열

- 3차원부터는 머릿속으로 생각하기보다 출력해보면서 코딩하는 편이 편함
- 이미지 processing이나 AI 신경망은 4차원 배열까지도 다루는 편
- 그 이상은 안가봄
- 3차원은 `박스 > 책 > 단원` 이런 식으로 이해하는 편인데 사람마다 달라서 적절한 비유 찾으면 적응되는 편
- `:` 는 슬라이싱, 콤마(`,`)는 차원

```python
x = np.array([[[1], [2], [3]], [[4], [5], [6]]])
print(x.shape)
print(x[1:2]) # x[1:2, :, :] 랑 똑같은 거, x[1] 이랑은 다름
```

- `...` : magic

```python
print(x[..., 0]) # x[:, :, 0]
```
