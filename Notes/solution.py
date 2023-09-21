import numpy as np

# 1D array from 0 to 9
print(np.arange(10))

# 3x3 array of all True
print(np.full((3, 3), True, dtype=bool))

# arr에서 홀수만 출력
arr = np.arange(10)
print(arr[arr % 2 == 1])

# arr에서 홀수만 -1로 바꾸기
arr = np.arange(10)
arr[arr % 2 == 1] = -1
print(arr)

# arr은 그대로 두고 홀수만 -1로 바꾸기
arr = np.arange(10)
res = np.where(arr % 2 == 1, -1, arr)
print(arr)
print(res)

# 1D 배열 -> 2D 배열 with 2행
arr = np.arange(10)
print(arr.reshape((2, -1)))

# 배열 두개 수직으로 쌓기
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

print(np.vstack((a, b)))

# 배열 두개 수평으로 붙이기
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

# array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) 출력
a = np.array([1, 2, 3])
print(np.r_[np.repeat(a, 3), np.tile(a, 3)])

# a랑 b에 모두 포함된 것들만 출력
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

print(np.intersect1d(a, b))

# a에서 b에도 있는 요소 모두 제거
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])

print(np.setdiff1d(a, b))

# a랑 b 겹치는 인덱스 모두 구하기
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

print(np.where(a == b))

# a에서 5~10 사이 모두 출력
a = np.array([2, 6, 1, 9, 10, 3, 27])

print(a[(a >= 5) & (a <= 10)])

# maxx 함수 사용하여 두 배열 중 큰 값으로 구성된 배열 출력
def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

pair_max = np.vectorize(maxx, otypes=[float])
print(pair_max(a, b))

# arr에서 첫번째와 두번째 열 서로 바꾸기
arr = np.arange(9).reshape(3, 3)

print(arr[:, [1, 0, 2]])

# arr에서 첫번째와 두번째 행 서로 바꾸기
arr = np.arange(9).reshape(3, 3)

print(arr[[1, 0, 2], :])

# arr 행 순서 뒤집기
arr = np.arange(9).reshape(3, 3)

print(arr[::-1])

# arr 열 순서 뒤집기
arr = np.arange(9).reshape(3, 3)

print(arr[:, ::-1])

# 5~10 사이 랜덤 소수로 이루어진 5x3 배열 만들기
rand_arr = np.random.uniform(5, 10, size=(5, 3))
print(rand_arr)

# rand_arr 값들 소수점 3자리까지만 출력
rand_arr = np.random.random((5, 3))
np.set_printoptions(precision=3)
print(rand_arr)

# 수학적 표기법 없애기
np.random.seed(100)
rand_arr = np.random.random([3, 3])/1e3

np.set_printoptions(suppress=True, precision=6)
print(rand_arr)

# a 배열에서 앞뒤로 3개씩만 출력되고 나머지는 ...으로 처리
a = np.arange(15) # [0, 1, 2, ..., 12, 13, 14] 이렇게

np.set_printoptions(threshold=6)
print(a)

# iris 데이터 그대로 가져오기
# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# iris = np.genfromtxt(url, delimiter=',', dtype='object')
# names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')

# print(iris[:3])

# iris에서 species 열만 추출
# species = np.array([row[4] for row in iris])
# print(species[:5])

# species 열 빼고 2차원 배열로 바꾸기 (iris_2d)
# iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0, 1, 2, 3])
# print(iris_2d[:4])

# iris의 sepallength 열의 mean, median, std 구하기
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
mu, med, sd = np.mean(sepallength), np.median(sepallength), np.std(sepallength)
print(mu, med, sd)

# iris의 sepallength 열 정규화시키기 (값들이 0에서 1사이)
## 공식 모르면 못함
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

Smax, Smin = sepallength.max(), sepallength.min()
S = (sepallength - Smin) / (Smax - Smin)
print(S)

# sepallength의 softmax score 계산
## 공식 모르면 못함
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

print(softmax(sepallength))