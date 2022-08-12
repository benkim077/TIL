# str -> int
st1 = '1234'
sm = 0
for char in st1:
    sm = sm*10 + ord(char)-ord('0')
print(sm)

# int -> str , 0보다 클 때
i = 123
st = ''
while i>0:
    st = chr(i%10 + ord('0')) + st
    i //= 10
print(st)