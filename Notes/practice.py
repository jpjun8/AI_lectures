import numpy as np

# 1D array from 0 to 9

# 3x3 array of all True

# arr에서 홀수만 출력
arr = np.arange(10)

# arr에서 홀수만 -1로 바꾸기
arr = np.arange(10)

# arr은 그대로 두고 홀수만 -1로 바꾸기
arr = np.arange(10)

# 1D 배열 -> 2D 배열 with 2행
a = np.arange(10)

# 배열 두개 수직으로 쌓기
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

# 배열 두개 수평으로 붙이기
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

# array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) 출력
a = np.array([1, 2, 3])

# a랑 b에 모두 포함된 것들만 출력
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

# a에서 b에도 있는 요소 모두 제거
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])

# a랑 b 겹치는 인덱스 모두 구하기
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

# a에서 5~10 사이 모두 출력
a = np.array([2, 6, 1, 9, 10, 3, 27])

# maxx 함수 사용하여 두 배열 중 큰 값으로 구성된 배열 출력
def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

# arr에서 첫번째와 두번째 열 서로 바꾸기
arr = np.arange(9).reshape(3, 3)

# arr에서 첫번째와 두번째 행 서로 바꾸기
arr = np.arange(9).reshape(3, 3)

# arr 행 순서 뒤집기
arr = np.arange(9).reshape(3, 3)

# arr 열 순서 뒤집기
arr = np.arange(9).reshape(3, 3)

# 5~10 사이 랜덤 소수로 이루어진 5x3 배열 만들기

# rand_arr 값들 소수점 3자리까지만 출력
rand_arr = np.random.random((5, 3))

# 수학적 표기법 없애기
np.random.seed(100)
rand_arr = np.random.random([3, 3])/1e3

# a 배열에서 앞뒤로 3개씩만 출력되고 나머지는 ...으로 처리
a = np.arange(15) # [0, 1, 2, ..., 12, 13, 14] 이렇게

# iris 데이터 그대로 가져오기
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')

# print(iris[:3])

# iris에서 species 열만 추출

# iris의 sepallength 열의 mean, median, std 구하기

# iris의 sepallength 열 정규화시키기 (값들이 0에서 1사이)
## 공식 모르면 못함

# sepallength의 softmax score 계산
## 공식 모르면 못함
