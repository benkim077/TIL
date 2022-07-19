# Lambda Function

람다 함수는 작은 **익명 함수**이다.
쓰고 버리는 일시적인 함수다.

## Syntax

```python
lambda arguments : expression
```

**여러 인자**를 가질 수 있지만, **하나의 표현식**을 갖는다.

## Usage

람다 함수를 사용하는 방법

1. 비슷한 **함수를 만드는 공장**

```python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
```
2. filter(), map(), reduce()와 함께 사용

map, filter, reduce 함수는 첫 인자로 함수를 받는다. 
이 위치에 임시로 lambda 함수를 사용한다.

```python
# 이전 가격
oldPrice = [['mbp', 1200], ['ipad', 500], ['iphone', 900]] 
# 새 가격. 10% 인상
newPrice = list(map((lambda x: [x[0],int(x[1] * 1.1)]), oldPrice))
print(newPrice) # [['mbp', 1320], ['ipad', 550], ['iphone', 990]]
```
3. sort(), sorted()와 사용

- list.sort(reverse=Boolean, key=function)
- sorted(iterable, key=function, reverse=Boolean)

```python
# 필기구 리스트
cropList = [('샤프',3000), ('포스트잇',2000), ('노트',4500),('연필',1000)]

# 리스트 가격(x[1])을 기준으로 내림차순 정렬
cropList.sort(key=lambda x : -x[1]) # 내림차순
cropList.sort(key-lambda x : x[1]) # 오름차순

# 가장 낮은 가격의 필기구 이름 출력
print(cropList[-1][0]) # '연필'
```

## Reference

- [W3School - Python Lambda](https://www.w3schools.com/python/python_lambda.asp)