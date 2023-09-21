# String Operations

## `add`, `multiply`, `mod`

- 기본적인 문자열 연산: 앞에 `np.char` 붙여주기

```python
# add: 문자열 결합
x = np.array(["a", "b", "c"])
y = np.array(["d", "e", "f"])
res = np.char.add(x, y)
print(res)

# multiply: 2-D에도 가능
x = np.array(["a", "b", "c"])
print(np.char.multiply(x, 3))

i = np.array([1, 2, 3]) # index
print(np.char.multiply(x, i))

# mod: '%' 이거랑 똑같은거, 잘 안 씀
vals = np.array([10, 20, 30])
fstring = 'Value: %d'
res = np.char.mod(fstring, vals)

for fs in res:
    print(fs)
```

## 꾸미기

```python
c = np.array(['a1b2', '1b2a', 'b2a1', '2a1b'])

print(np.char.capitalize(c))

print(np.char.center(c, width=9))
print(np.char.center(c, width=9, fillchar='*'))
print(np.char.center(c, width=2))

print(np.char.encode(c, encoding='UTF8'))

print(np.char.join('-', 'abc'))
print(np.char.join(['-', '.'], ['abc', 'def']))
```
