# id number를 입력받아 뒷자리는 비식별화 하여 출력하는 코드
idNumber = input('주민번호 입력:')

# string method, translate()를 사용해서 '-'를 제거
translateTable = idNumber.maketrans({
    '-': ''
})
idNumber = idNumber.translate(translateTable)

deIdNumber = idNumber[0:6] + '*******'

print(deIdNumber)