## 예시

```python
numbers = [1, 2, 3]
# 위의 변수 numbers를 문자열 '123'으로 만드세요. (join 메서드 활용)

for i in range(3):
    numbers[i] = str(numbers[i])

print(numbers)

numbers = ''.join(numbers)

print(numbers)
print(type(numbers))
```

# Syntax
string.join(iterable)

iterable	Required. Any iterable object where all the returned values are strings

