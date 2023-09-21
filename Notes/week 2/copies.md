# Copies & Views

## 복사 X

- 단순 할당은 새로운 객체를 생성하지 않는다
- 함수 실행도 복사 X

```python
a = np.arange(10)
b = a
print(b is a) # a랑 b는 같은 ndarry 객체의 다른 이름

def f(x):
    print(id(x))
print(id(a))
f(a)
```

## `View`

- 얕은 복사
- 새로운 객체 생성 &rarr; 같은 데이터 포인팅
- 배열의 슬라이싱한 것도 `View`

```python
c = a.view()
print(c is a)
print(c.base is a)
print(c.flags.owndata) # c 변수가 자기 자신의 데이터 가지고 있는지

c = c.reshape((2, 5)) # c 변수 shape만 바뀜
print(a)
print(c)

c[0, 4] = 1234 # 데이터는 같기 때문에 건드리면 바뀜
print(a)
print(c)
```

## 깊은 복사

- 자신만의 이름, 데이터 그대로 복사
- 데이터 값만 같을 뿐 다른 객체
- 새로운 객체, 새로운 데이터를 생성하기 때문에 메모리를 많이 잡아먹어 필요없는 배열은 `del`로 삭제해주는게 좋다
  
```python
d = a.copy()
print(d is a)
print(d.base is a)

d[0, 0] = 9999 # d 배열 값 변경
print(a)
```