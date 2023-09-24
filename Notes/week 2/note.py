import numpy as np
import functools

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