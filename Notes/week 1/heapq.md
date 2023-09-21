# `heapq` 모듈: heap 기능 사용

- 다익스트라에 많이 씀 (heapq > PriorityQueue)
- 트리 구조에 적합
- 최소 힙 구조에 많이 사용됨 (가장 작은 요소가 항상 root에 있음)

## `heapify(iterable)`

- 반복자료형 &rarr; 힙

```python
import heapq

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
heapq.heapify(data)

print(data)
```

## `heappush(heap, item)`

- `heap`에 새로운 `item` 추가

```python
import heapq

heap = [3, 1, 4, 1, 5]
heapq.heapify(heap)
print(heap)
heapq.heappush(heap, 2)

print(heap)
```

## `heappop(heap)`

- 최소 요소 return & remove

```python
import heapq

heap = [1, 1, 2, 3, 3, 9, 4, 6, 5, 5, 5]
smallest = heapq.heappop(heap)

print(f"The smallest element is: {smallest}")
```

## `heapreplace(heap, item)`

- pop and return 최소 요소
- push 새로운 요소 to heap

```python
import heapq

heap = [1, 2, 3, 4, 5]
smallest = heapq.heapreplace(heap, 0)

print(f"Smallest element popped: {smallest}")
print(f"Heap after replacement: {heap}")
```

## `nlargest(n, iterable)` and `nsmallest(n, iterable)`

- return `n` largest & smallest 요소들 (중복가능)

```python
import heapq

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
largest_three = heapq.nlargest(3, data)
smallest_three = heapq.nsmallest(3, data)

print(f"Largest three elements: {largest_three}")
print(f"Smallest three elements: {smallest_three}")
```

## `heapq.merge(*iterables, key=None, reverse=False)`

- 힙 여러개 결합

```python
import heapq

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

merged = heapq.merge(list1, list2)

print(list(merged))
```
