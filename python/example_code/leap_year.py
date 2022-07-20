# 윤년 계산기

thisYear = int(input('연도를 입력하세요:'))

print('윤년O') if (not (thisYear % 400) or (not (thisYear % 4) and (thisYear % 100))) else print('윤년X')